from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsrControlCls:
	"""TsrControl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsrControl", core, parent)

	def set(self, pwr_db: int, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:TSRControl \n
		Snippet: driver.configure.sta.connection.hetf.tsrControl.set(pwr_db = 1, station = repcap.Station.Default) \n
		Specifies the value Target RSSI Control for adjustment to the Target_RSSI. This parameter is only relevant in manual mode
		for target RSSI calculation. \n
			:param pwr_db: integer Range: -40 dB to 0 dB
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = Conversions.decimal_value_to_str(pwr_db)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:TSRControl {param}')

	def get(self, station=repcap.Station.Default) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:TSRControl \n
		Snippet: value: int = driver.configure.sta.connection.hetf.tsrControl.get(station = repcap.Station.Default) \n
		Specifies the value Target RSSI Control for adjustment to the Target_RSSI. This parameter is only relevant in manual mode
		for target RSSI calculation. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: pwr_db: integer Range: -40 dB to 0 dB"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:TSRControl?')
		return Conversions.str_to_int(response)
