from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsCls:
	"""Mcs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcs", core, parent)

	def set(self, mcs_index: enums.McsIndex, station=repcap.Station.Default, dummy=repcap.Dummy.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:DUMMy<index>:MCS \n
		Snippet: driver.configure.connection.sta.dframe.hemu.dummy.mcs.set(mcs_index = enums.McsIndex.MCS, station = repcap.Station.Default, dummy = repcap.Dummy.Default) \n
		Sets the modulation and coding scheme for the corresponding dummy user. \n
			:param mcs_index: MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | MCS8 | MCS9 | MCS10 | MCS11 MCS, MCS1,...,MCS11: MCS 0 to MCS 11
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:param dummy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dummy')
		"""
		param = Conversions.enum_scalar_to_str(mcs_index, enums.McsIndex)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		dummy_cmd_val = self._cmd_group.get_repcap_cmd_value(dummy, repcap.Dummy)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:DUMMy{dummy_cmd_val}:MCS {param}')

	# noinspection PyTypeChecker
	def get(self, station=repcap.Station.Default, dummy=repcap.Dummy.Default) -> enums.McsIndex:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:DUMMy<index>:MCS \n
		Snippet: value: enums.McsIndex = driver.configure.connection.sta.dframe.hemu.dummy.mcs.get(station = repcap.Station.Default, dummy = repcap.Dummy.Default) \n
		Sets the modulation and coding scheme for the corresponding dummy user. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:param dummy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dummy')
			:return: mcs_index: MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | MCS8 | MCS9 | MCS10 | MCS11 MCS, MCS1,...,MCS11: MCS 0 to MCS 11"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		dummy_cmd_val = self._cmd_group.get_repcap_cmd_value(dummy, repcap.Dummy)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:DUMMy{dummy_cmd_val}:MCS?')
		return Conversions.str_to_scalar_enum(response, enums.McsIndex)
