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

	def set(self, mcs_index: enums.McsIndex, station=repcap.Station.Default, user=repcap.User.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:USER<index>:MCS \n
		Snippet: driver.configure.connection.sta.dframe.hemu.user.mcs.set(mcs_index = enums.McsIndex.MCS, station = repcap.Station.Default, user = repcap.User.Default) \n
		Sets the modulation and coding scheme for user 1 (user data assigned to the DUT) . \n
			:param mcs_index: MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | MCS8 | MCS9 | MCS10 | MCS11 MCS, MCS1,...,MCS11: MCS 0, MCS 1 to MCS 11
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(mcs_index, enums.McsIndex)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:USER{user_cmd_val}:MCS {param}')

	# noinspection PyTypeChecker
	def get(self, station=repcap.Station.Default, user=repcap.User.Default) -> enums.McsIndex:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:USER<index>:MCS \n
		Snippet: value: enums.McsIndex = driver.configure.connection.sta.dframe.hemu.user.mcs.get(station = repcap.Station.Default, user = repcap.User.Default) \n
		Sets the modulation and coding scheme for user 1 (user data assigned to the DUT) . \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: mcs_index: MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | MCS8 | MCS9 | MCS10 | MCS11 MCS, MCS1,...,MCS11: MCS 0, MCS 1 to MCS 11"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:USER{user_cmd_val}:MCS?')
		return Conversions.str_to_scalar_enum(response, enums.McsIndex)
