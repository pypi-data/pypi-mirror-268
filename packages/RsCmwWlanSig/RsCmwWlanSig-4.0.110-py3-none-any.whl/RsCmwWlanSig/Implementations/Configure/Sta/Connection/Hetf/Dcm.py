from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DcmCls:
	"""Dcm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcm", core, parent)

	def set(self, dcm: bool, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:DCM \n
		Snippet: driver.configure.sta.connection.hetf.dcm.set(dcm = False, station = repcap.Station.Default) \n
		Specifies whether the HE TB response uses dual carrier modulation (DCM) . \n
			:param dcm: OFF | ON
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = Conversions.bool_to_str(dcm)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:DCM {param}')

	def get(self, station=repcap.Station.Default) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:DCM \n
		Snippet: value: bool = driver.configure.sta.connection.hetf.dcm.get(station = repcap.Station.Default) \n
		Specifies whether the HE TB response uses dual carrier modulation (DCM) . \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: dcm: OFF | ON"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:DCM?')
		return Conversions.str_to_bool(response)
