from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CtypCls:
	"""Ctyp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctyp", core, parent)

	def set(self, type_py: enums.CodingType, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:CTYP \n
		Snippet: driver.configure.sta.connection.hetf.ctyp.set(type_py = enums.CodingType.BCC, station = repcap.Station.Default) \n
		Specifies the coding used by the HE TB PPDU. \n
			:param type_py: BCC | LDPC
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.CodingType)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:CTYP {param}')

	# noinspection PyTypeChecker
	def get(self, station=repcap.Station.Default) -> enums.CodingType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:CTYP \n
		Snippet: value: enums.CodingType = driver.configure.sta.connection.hetf.ctyp.get(station = repcap.Station.Default) \n
		Specifies the coding used by the HE TB PPDU. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: type_py: BCC | LDPC"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:CTYP?')
		return Conversions.str_to_scalar_enum(response, enums.CodingType)
