from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StreamsCls:
	"""Streams commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("streams", core, parent)

	def set(self, streams: enums.Streams, user=repcap.User.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DFRame:HEMU:USER<index>:STReams \n
		Snippet: driver.configure.per.dframe.hemu.user.streams.set(streams = enums.Streams.STR1, user = repcap.User.Default) \n
		Sets the number of streams for PER measurements used by the user for MIMO connections. \n
			:param streams: STR1 | STR2 One or two streams
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(streams, enums.Streams)
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DFRame:HEMU:USER{user_cmd_val}:STReams {param}')

	# noinspection PyTypeChecker
	def get(self, user=repcap.User.Default) -> enums.Streams:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DFRame:HEMU:USER<index>:STReams \n
		Snippet: value: enums.Streams = driver.configure.per.dframe.hemu.user.streams.get(user = repcap.User.Default) \n
		Sets the number of streams for PER measurements used by the user for MIMO connections. \n
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: streams: STR1 | STR2 One or two streams"""
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DFRame:HEMU:USER{user_cmd_val}:STReams?')
		return Conversions.str_to_scalar_enum(response, enums.Streams)
