from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	@property
	def tcsd(self):
		"""tcsd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcsd'):
			from .Tcsd import TcsdCls
			self._tcsd = TcsdCls(self._core, self._cmd_group)
		return self._tcsd

	# noinspection PyTypeChecker
	def get_tm_mode(self) -> enums.MimoMode:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:MIMO:TMMode \n
		Snippet: value: enums.MimoMode = driver.configure.mimo.get_tm_mode() \n
		Selects the transmission mode for MIMO connections. This command supports only spatial multiplexing and space time block
		coding (STBC) . In addition, to enable STBC in a particular data frame, use the commands: method RsCmwWlanSig.Configure.
		Sta.Connection.Dfdef.set or method RsCmwWlanSig.Configure.Per.fdef \n
			:return: mode: STBC | SMULtiplexin
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:MIMO:TMMode?')
		return Conversions.str_to_scalar_enum(response, enums.MimoMode)

	def set_tm_mode(self, mode: enums.MimoMode) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:MIMO:TMMode \n
		Snippet: driver.configure.mimo.set_tm_mode(mode = enums.MimoMode.SMULtiplexin) \n
		Selects the transmission mode for MIMO connections. This command supports only spatial multiplexing and space time block
		coding (STBC) . In addition, to enable STBC in a particular data frame, use the commands: method RsCmwWlanSig.Configure.
		Sta.Connection.Dfdef.set or method RsCmwWlanSig.Configure.Per.fdef \n
			:param mode: STBC | SMULtiplexin
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.MimoMode)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:MIMO:TMMode {param}')

	def clone(self) -> 'MimoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MimoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
