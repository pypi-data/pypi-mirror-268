
"""connect to MARSH Sim system, see https://marsh-sim.github.io/"""
from argparse import _SubParsersAction, ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace
import json
import msgpack
from multiprocessing import Queue
from pymavlink import mavutil
import socket
from time import time
from typing import Tuple

from ..aircraft import *
from ..config import Config
from .. import mavlink_all as mavlink
from .mytypes import RunFn


def setup(subparsers: _SubParsersAction) -> Tuple[str, RunFn]:
    NAME = 'marsh'
    parser: ArgumentParser = subparsers.add_parser(
        NAME,
        help=__doc__,
        formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--manager',
                        help='MARSH Manager IP addr', default='127.0.0.1')

    return (NAME, run)


def run(q: Queue, args: Namespace, config: Config):

    connection_string = f'udpout:{args.manager}:24400'
    mav = mavlink.MAVLink(mavutil.mavlink_connection(connection_string))
    mav.srcSystem = 1  # default system
    mav.srcComponent = mavlink.MARSH_COMP_ID_INSTRUMENTS
    if args.verbosity >= 0:
        print(f'Connecting to MARSH Manager on {connection_string}')

    last_state = AircraftState()

    # controlling when messages should be sent
    heartbeat_next = 0.0
    heartbeat_interval = 1.0

    # monitoring connection to manager with heartbeat
    timeout_interval = 5.0
    manager_timeout = 0.0
    manager_connected = False

    # the loop goes as fast as it can, relying on the variables above for timing
    while True:
        if time() >= heartbeat_next:
            mav.heartbeat_send(
                mavlink.MAV_TYPE_GENERIC,
                mavlink.MAV_AUTOPILOT_INVALID,
                mavlink.MAV_MODE_FLAG_TEST_ENABLED,
                0,
                mavlink.MAV_STATE_ACTIVE
            )
            heartbeat_next = time() + heartbeat_interval

        state_changed = False

        # handle incoming messages
        try:
            while (message := mav.file.recv_msg()) is not None:
                message: mavlink.MAVLink_message
                if message.get_type() == 'HEARTBEAT':
                    if message.get_srcComponent() == mavlink.MARSH_COMP_ID_MANAGER:
                        if not manager_connected and args.verbosity >= 0:
                            print('Connected to simulation manager')
                        manager_connected = True
                        manager_timeout = time() + timeout_interval
                elif message.get_type() == 'MANUAL_CONTROL':
                    # This line helps with type hints
                    mc: mavlink.MAVLink_manual_control_message = message
                    state_changed = True

                    last_state.ctrl = Controls()
                    # Invalid axes are sent as INT16_MAX
                    INVALID = 0x7FFF
                    if mc.x != INVALID:
                        last_state.ctrl.stick_pull = mc.x / -1000
                    if mc.y != INVALID:
                        last_state.ctrl.stick_right = mc.y / 1000
                    if mc.z != INVALID:
                        last_state.ctrl.throttle = mc.z / 1000
                        last_state.ctrl.collective_up = mc.z / 1000
                    if mc.z != INVALID:
                        last_state.ctrl.pedals_right = mc.r / 1000

                    # TODO: assign buttons

                elif message.get_type() == 'MANUAL_SETPOINT':
                    # This line helps with type hints
                    ms: mavlink.MAVLink_manual_setpoint_message = message
                    state_changed = True

                    last_state.trgt.ctrl = Controls()
                    last_state.trgt.ctrl.stick_right = ms.roll
                    last_state.trgt.ctrl.stick_pull = ms.pitch
                    last_state.trgt.ctrl.pedals_right = ms.yaw
                    last_state.trgt.ctrl.throttle = ms.thrust
                    last_state.trgt.ctrl.collective_up = ms.thrust

                elif message.get_type() == 'SIM_STATE':
                    ss: mavlink.MAVLink_sim_state_message = message
                    state_changed = True

                    last_state.att = Attitude()
                    last_state.att.roll = ss.roll
                    last_state.att.pitch = ss.pitch
                    last_state.att.yaw = ss.yaw

                    last_state.a_body = XYZ()
                    last_state.a_body.x = ss.xacc
                    last_state.a_body.y = ss.yacc
                    last_state.a_body.z = ss.zacc

                    last_state.v_ned = NED()
                    last_state.v_ned.north = ss.vn
                    last_state.v_ned.east = ss.ve
                    last_state.v_ned.down = ss.vd

                    last_state.ned = NED()
                    # TODO: Add argument for reference location, calculate north and east from that
                    last_state.ned.down = -ss.alt

                elif message.get_type() == 'RAW_RPM':
                    rr: mavlink.MAVLink_raw_rpm_message = message
                    state_changed = True

                    if last_state.hrpm is None:
                        last_state.hrpm = HelicopterRPM()

                    if rr.index == 0:
                        last_state.hrpm.rotor = rr.frequency / config.pfd.rpm_r_nominal
                    else:
                        last_state.hrpm.engine = rr.frequency / config.pfd.rpm_e_nominal
        except ConnectionResetError:
            # thrown on Windows when there is no peer listening
            pass

        if manager_connected and time() > manager_timeout:
            manager_connected = False
            if args.verbosity >= 0:
                print('Lost connection to simulation manager')

        if state_changed:
            state = last_state
            state.model_instruments(config)
            if state.trgt is not None:
                state.trgt.model_instruments(config)
            if state.trim is not None:
                state.trim.model_instruments(config)
            q.put(('smol', state.smol()))
