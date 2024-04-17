from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrsModeCls:
	"""TrsMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trsMode", core, parent)

	def set(self, mode: enums.TriggerFrmPowerMode, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:TRSMode \n
		Snippet: driver.configure.sta.connection.hetf.trsMode.set(mode = enums.TriggerFrmPowerMode.AUTO, station = repcap.Station.Default) \n
		Specifies the trigger frame power control mode. \n
			:param mode: AUTO | MANual | MAXPower AUTO: AP_TX_Power and Target_RSSI calculated automatically MAN: The value Target RSSI Control defines adjustment to the Target_RSSI calculation MAXP: Sets the Target_RSSI to 127, the UE transmits the HE TB PPDU at maximum Tx power
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TriggerFrmPowerMode)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:TRSMode {param}')

	# noinspection PyTypeChecker
	def get(self, station=repcap.Station.Default) -> enums.TriggerFrmPowerMode:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:TRSMode \n
		Snippet: value: enums.TriggerFrmPowerMode = driver.configure.sta.connection.hetf.trsMode.get(station = repcap.Station.Default) \n
		Specifies the trigger frame power control mode. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: mode: AUTO | MANual | MAXPower AUTO: AP_TX_Power and Target_RSSI calculated automatically MAN: The value Target RSSI Control defines adjustment to the Target_RSSI calculation MAXP: Sets the Target_RSSI to 127, the UE transmits the HE TB PPDU at maximum Tx power"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:TRSMode?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerFrmPowerMode)
