import os
import can
import time
import logging
import cantools
from typing import Literal
from cantools.database.can.signal import NamedSignalValue

dbc_dir = os.path.join(os.path.dirname(__file__)) + "/dbc/"
can_db = cantools.database.Database()
for file in os.listdir(dbc_dir):
    if file.endswith(".dbc"):
        can_db.add_dbc_file(os.path.join(os.getcwd(), dbc_dir + file))


class ContactorBoard:
    """
    Base class for the Loadbox Controller for the Contactor Card
    """
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.getLogger().setLevel(logging.INFO))

    def __init__(self):
        self.bus = None
        self.contactors = 10  # amount of contactor channels on board
        self.shorts = 3  # amount of short channels
        self.contactor_state = {}
        self.short_state = {}
        for contactor in range(self.contactors):
            self.contactor_state[contactor] = {"weld": 0, "stuck_open": 0}
        for short in range(self.shorts):
            self.short_state[short] = {"active": 0}
        return

    def can_connection(self, interface: str, channel: str, bitrate: int) -> None:
        """
        Sets up the CAN connection
        :param interface: Type of interface: 'pcan', 'vector', 'socketcan'
        :param channel: 'PCAN_USBBUSx', '0', 'canx'
        :param bitrate: e.g. 500000
        """
        can.rc['interface'] = interface
        can.rc['channel'] = channel
        can.rc['bitrate'] = bitrate
        self.bus = can.interface.Bus()

    def set_lb_relays(self, device: Literal['contactors', 'shorts'], channel: int, function: Literal['weld', 'stuck_open', 'active'], value: Literal[0, 1]) -> None:
        """
        Set the Contactor card relays
        :param device: 'contactors' or 'shorts' relays
        :param channel: 'contactors' -> 0-9 & 'shorts' -> 0-2
        :param function: 'contactors' -> 'weld'/ 'stuck_open' or 'shorts' -> 'active'
        :param value: 0: Open relay/OFF or 1: Close relay/ON
        """

        if device == "contactors" and channel in self.contactor_state and function in self.contactor_state[channel]:
            try:
                self.contactor_state[channel][function.lower()] = bool(int(value))
                self._send_state_to_board()
            except Exception as e:
                raise Exception(f"ERROR: {e} in setting fault {function} for channel {channel} with value {value}")
        elif device == "shorts" and channel in self.short_state and function in self.short_state[channel]:
            try:
                self.short_state[channel]["active"] = bool(int(value))
                self._send_state_to_board()
            except Exception as e:
                raise Exception(f"ERROR: {e} in setting fault {function} for channel {channel} with value {value}")
        else:
            logging.error("ERROR: Device/Channel/Function not correct")

    @staticmethod
    def _create_payload(card_id, relay_data):
        """
        This will create a list with 8 Data bytes (Total 64 Bits) to control HiL Cards
        Datastructure is as follows: (one based)
        Bit 1-4 -> Card ID
        Bit 5-64 -> Relay Data
        """
        out = [0] * 8
        out[0] = out[0] | (card_id & 0xF)
        out[0] = out[0] | (relay_data & 0xF) << 4
        for i in range(7):
            out[i + 1] = out[i + 1] | ((relay_data >> (i * 8) + 4) & 0xFF)
        return out

    @staticmethod
    def _get_bit(number, position):
        return number >> position & 1

    def _check_card(self, card: int, relays=None) -> None:
        if card > 16:
            logging.debug(f"Card not there: {card}")
            return None
        if relays is None:
            max_relays = [32, 32, 32, 32, 48, 48, 32]  # max relays of cards
            relays = range(max_relays[card])
        for relay_no in relays:
            rly_set = 1 << (relay_no)
            logging.debug(f"Setting Card {card}, relay {relay_no}")
            logging.debug(bin(rly_set))
            self._send_relay_can_message_raw(card, rly_set)
            time.sleep(0.5)
            self._send_relay_can_message_raw(card, 0)
            time.sleep(0.1)

    def _send_state_to_board(self) -> None:
        bytes = 0
        for signal in self.contactor_state:
            chip_offset = (signal // 8) * 16  # Calculate the offset after 8 Signals
            bytes = bytes | (bool(self.contactor_state[signal]["weld"]) << (signal + chip_offset))
            bytes = bytes | (bool(self.contactor_state[signal]["stuck_open"]) << (8 + signal + chip_offset))
        for signal in self.short_state:
            bytes = bytes | (bool(self.short_state[signal]["active"]) << (18 + signal))

        logging.debug(self.contactor_state)
        logging.debug(self.short_state)
        # self._send_relay_can_message_raw(9, bytes)
        self._send_relay_can_message(bytes)

    def _parse_can_state(self, can_state) -> None:
        for signal in self.contactor_state:
            # Calculate the offset after 8 Signals
            chip_offset = (signal // 8) * 16
            self.contactor_state[signal]["weld"] = self._get_bit(can_state, signal + chip_offset)
            self.contactor_state[signal]["stuck_open"] = self._get_bit(can_state, 8 + signal + chip_offset)
        for signal in self.short_state:
            bytes = bytes | (bool(self.short_state[signal]["active"]) << (18 + signal))

    def _send_can_message(self, msg_name: str, commands) -> None:
        """
        Function to send a complete CAN message to the board
        :param msg_name: Message name as in the DBC file
        :param commands: Corresponding CAN command with signal name and value
        """
        try:
            cmd_message = can_db.get_message_by_name(msg_name)
        except Exception as e:
            raise Exception(f"ERROR {e}: Message {msg_name} not found in Databases")

        # Prepare a message with all signals
        signals = {}
        for signal in cmd_message.signals:
            if signal.name in commands:
                signals[signal.name] = commands[signal.name]
            else:
                signals[signal.name] = 0

        message = can.Message(arbitration_id=cmd_message.frame_id,
                              data=cmd_message.encode(signals, strict=False),
                              is_extended_id=False)
        logging.debug(f"Sending message {message}")
        self.bus.send(message)

    def _send_relay_can_message(self, data) -> None:
        """
        Creates a can message out of the state and sends it to the can connector
        CAN Message: RC_Cntrl, ID: 0x210
        Signals :
            RC_mux -> fib Card (9) multiplexer
            RC_cntrlXX -> 60 Bit for the relays XX is multiplexer eg (01 or 00)
        :param data: binary CAN message data
        """
        mux_name = "RC_cntrl09"
        cmd = {'RC_mux': 9, mux_name: data}
        self._send_can_message(f"RC_Cntrl", cmd)

    def _send_relay_can_message_raw(self, card, data) -> None:
        """
        Sends raw CAN message to the card
        :param card: int: card ID
        :param data: bin: data to be sent
        """
        message = can.Message(arbitration_id=528,
                              data=self._create_payload(card, data),
                              is_extended_id=False)
        self.bus.send(message)

    def test_lb_contactor_card(self) -> None:
        """
        Function to test all the Contactor card relays
        """
        used_ports = list(range(21))  # zero based
        self._check_card(9, used_ports)
