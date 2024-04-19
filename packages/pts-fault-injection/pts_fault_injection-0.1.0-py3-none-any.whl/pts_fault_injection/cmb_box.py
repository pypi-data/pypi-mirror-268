import os
import can
import time
import logging
import cantools
from typing import Union, Literal
from cantools.database.can.signal import NamedSignalValue


dbc_dir = os.path.join(os.path.dirname(__file__)) + "/dbc/"
can_db = cantools.database.Database()
for file in os.listdir(dbc_dir):
    if file.endswith(".dbc"):
        can_db.add_dbc_file(os.path.join(os.getcwd(), dbc_dir + file))


class CMBBoxController:
    """
    Base class for the CMB Box Controller
    """
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.getLogger().setLevel(logging.INFO))

    def __init__(self):
        self.bus = None
        self.id = id
        self.state = {}
        # Amount of channels for the board is 19
        self.channels = 19
        for cell in range(self.channels):
            self.state[f"cell{cell}"] = {"open_circuit": 0, "high_impedance": 0}
        self.state["supply_plus"] = {"open_circuit": 0}
        self.state["supply_minus"] = {"open_circuit": 0}
        self.state["communication1"] = {"open_circuit": 0}
        self.state["communication2"] = {"open_circuit": 0}

        # Setup DAC states: 5 DAC chips with 4 channels each, initially set to 0.5V
        self.dacs = {0: [0.5, 0.5, 0.5, 0.5],
                     1: [0.5, 0.5, 0.5, 0.5],
                     2: [0.5, 0.5, 0.5, 0.5],
                     3: [0.5, 0.5, 0.5, 0.5],
                     4: [0.5, 0.5, 0.5, 0.5]}
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

    def set_dac_voltage(self, channel: int, value: Union[int, float]) -> None:
        """
        Sets the DAC voltage for the channel number given
        :param channel: Range 0-19 [DAC: 0-4, each DAC channel: 0-3]
        :param value: Voltage range: 0.5-4.5V
        """
        dac = (channel // 4)
        dac_ch = (channel % 4)
        self.dacs[dac][dac_ch] = float(value)
        self._update_dac(dac, dac_ch)

    def _send_can_message(self, msg_name: str, commands) -> None:
        """
        Function to send a complete CAN message to the board
        :param msg_name: Message name as in the DBC file
        :param commands: Corresponding CAN command with signal name and value
        """
        try:
            cmd_message = can_db.get_message_by_name(msg_name)
        except Exception as e:
            raise Exception(f"ERROR: {e}: Message {msg_name} not found in Databases")

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

    def _update_dac(self, dac_no, ch_no) -> None:
        """
        Updates a Dac with the stored state
            Message ID is 0x22a-e & Message Name is : DAC_CMB_Cntrl_0i
        Signal name is DAC_CMB_Cntrl_0y_0z_Voltage
            where, y = 1-5 for 5 DACs and z = 1-4 for 4 Channels per DAC
        :param dac_no: DACs: 0-4
        :param ch_no: each DAC containing channels: 0-3
        """
        cmd = {}
        msg_name = f"DAC_CMB_Cntrl"
        cmd["DAC_CMB_Cntrl_Channel"] = (dac_no) * 0x10 + ch_no  # set the multiplexor
        signal_name = f"DAC_CMB_Cntrl_{str(dac_no + 1).zfill(2)}_{str(ch_no + 1).zfill(2)}_Voltage"
        cmd[signal_name] = self.dacs[dac_no][ch_no]
        logging.debug(cmd)
        self._send_can_message(f"{msg_name}", cmd)

    def _update_board_status(self) -> None:
        """
        Updates the state of the signals on the CMB Faults board
        """
        data = {}
        for i in range(self.channels):
            # Set open circuit state
            data[f"RCCMBCntrl_CV{i}_OC"] = self.state[f"cell{i}"]["open_circuit"]
            # Set high impedance state
            data[f"RCCMBCntrl_CV{i}_HImp"] = self.state[f"cell{i}"]["high_impedance"]

        data["RCCMBCntrl_SupplyPlus"] = self.state["supply_plus"]["open_circuit"]
        data["RCCMBCntrl_SupplyMinus"] = self.state["supply_minus"]["open_circuit"]
        data["RCCMBCntrl_CommDaisyChain1"] = self.state["communication1"]["open_circuit"]
        data["RCCMBCntrl_CommDaisyChain2"] = self.state["communication2"]["open_circuit"]
        logging.debug(data)
        self._send_can_message(f"RCCMBCntrl", data)

    def set_cmb_relays(self, channel: str, function: Literal['open_circuit', 'high_impedance'], value: Literal[0, 1]) -> None:
        """
        Sets the signals/relays of the CMB board
        :param channel: 'cellx' (x = 0-18), 'supply_plus', 'supply_minus', 'communication1', 'communication2'
        :param function: 'open_circuit' or 'high_impedance'
        :param value: 0: Open relay/OFF or 1: Close relay/ON
        """
        if str(channel) in self.state and str(function) in self.state[channel]:
            try:
                self.state[channel][function] = bool(int(value))
                logging.debug(f"Setting fault {function} for channel {channel} with value {value}")
            except Exception as e:
                raise Exception(f"ERROR {e}: in setting fault {function} for channel {channel} with value {value}")
        else:
            logging.error("ERROR: Channel/Function not correct")
        self._update_board_status()

    def send_cmb_fault_relay_can_message(self, cell: int, function: Literal['OC', 'HImp'], value: Literal[0, 1]) -> None:
        """
        Function sends CAN message to set relays for the cells
        :param cell: Cell numbers from 0-18
        :param function: 'OC': Open circuit or 'HImp': High Impedance
        :param value: 0: Open relay/OFF or 1: Close relay/ON
        """
        cmd = {f'RCCMBCntrl_CV{cell}_{function}': value}
        self._send_can_message("RCCMBCntrl", cmd)

    def send_cmb_additional_can_message(self, signal: str, value: Literal[0, 1]) -> None:
        """
        Function sends CAN message to set relays for the all additional signals
        :param signal: Options: SupplyPlus_HImp, SupplyMinus_HImp,
                                SupplyPlus, SupplyMinus,
                                CommDaisyChain1, CommDaisyChain2,
                                IsoPlus, IsoMinus
        :param value: 0: Open relay/OFF or 1: Close relay/ON
        """
        cmd = {f'RCCMBCntrl_{signal}': value}
        self._send_can_message("RCCMBCntrl", cmd)

    def send_isospi_bridge_can_message(self, value: Literal[1, 0]) -> None:
        """
        Function sends CAN message to set relays for the ISOSPI connection through CMB box
        Can be done for boxes retrofitted to use bridged ISOSPI
        :param value: 0: Open relay/OFF or 1: Close relay/ON
        """
        cmd = {f'RCCMBCntrl_IsoPlus': value, f'RCCMBCntrl_IsoMinus': value}
        self._send_can_message("RCCMBCntrl", cmd)

    def test_cell_fault_board(self) -> None:
        """
        This function switches the OC and HImp relays for all the 19 cell channels
        """
        for cell in range(18):
            print(f"Testing Open Circuit on cell {cell}")
            self.send_cmb_fault_relay_can_message(cell, "OC", 1)
            time.sleep(0.5)
            self.send_cmb_fault_relay_can_message(cell, "OC", 0)
            time.sleep(0.1)

        for cell in range(18):
            print(f"Testing High Impedance on cell {cell}")
            self.send_cmb_fault_relay_can_message(cell, "HImp", 1)
            time.sleep(0.5)
            self.send_cmb_fault_relay_can_message(cell, "HImp", 0)
            time.sleep(0.1)
