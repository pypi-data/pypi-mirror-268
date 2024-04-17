from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NssCls:
	"""Nss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nss", core, parent)

	def set(self, number_ss: int, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:NSS \n
		Snippet: driver.configure.sta.connection.hetf.nss.set(number_ss = 1, station = repcap.Station.Default) \n
		Sets the number of HE TB PPDU spatial streams. \n
			:param number_ss: integer Range: 1 to 8
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = Conversions.decimal_value_to_str(number_ss)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:NSS {param}')

	def get(self, station=repcap.Station.Default) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:NSS \n
		Snippet: value: int = driver.configure.sta.connection.hetf.nss.get(station = repcap.Station.Default) \n
		Sets the number of HE TB PPDU spatial streams. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: number_ss: integer Range: 1 to 8"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:NSS?')
		return Conversions.str_to_int(response)
