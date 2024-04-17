from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StreamsCls:
	"""Streams commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("streams", core, parent)

	def set(self, streams: enums.Streams, station=repcap.Station.Default, user=repcap.User.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:USER<index>:STReams \n
		Snippet: driver.configure.connection.sta.dframe.hemu.user.streams.set(streams = enums.Streams.STR1, station = repcap.Station.Default, user = repcap.User.Default) \n
		Sets the number of streams used by the user for MIMO connections. \n
			:param streams: STR1 | STR2 One or two streams
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(streams, enums.Streams)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:USER{user_cmd_val}:STReams {param}')

	# noinspection PyTypeChecker
	def get(self, station=repcap.Station.Default, user=repcap.User.Default) -> enums.Streams:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:USER<index>:STReams \n
		Snippet: value: enums.Streams = driver.configure.connection.sta.dframe.hemu.user.streams.get(station = repcap.Station.Default, user = repcap.User.Default) \n
		Sets the number of streams used by the user for MIMO connections. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: streams: STR1 | STR2 One or two streams"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:USER{user_cmd_val}:STReams?')
		return Conversions.str_to_scalar_enum(response, enums.Streams)
