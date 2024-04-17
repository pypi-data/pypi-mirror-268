from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcodeCls:
	"""Ccode commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccode", core, parent)

	@property
	def ccconf(self):
		"""ccconf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccconf'):
			from .Ccconf import CcconfCls
			self._ccconf = CcconfCls(self._core, self._cmd_group)
		return self._ccconf

	# noinspection PyTypeChecker
	def get_cc_state(self) -> enums.EnableState:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:CCODe:CCSTate \n
		Snippet: value: enums.EnableState = driver.configure.connection.ccode.get_cc_state() \n
		Enables/disables the broadcast of regulatory domain information in beacon frames. \n
			:return: state: DISable | ENABle
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:CCODe:CCSTate?')
		return Conversions.str_to_scalar_enum(response, enums.EnableState)

	def set_cc_state(self, state: enums.EnableState) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:CCODe:CCSTate \n
		Snippet: driver.configure.connection.ccode.set_cc_state(state = enums.EnableState.DISable) \n
		Enables/disables the broadcast of regulatory domain information in beacon frames. \n
			:param state: DISable | ENABle
		"""
		param = Conversions.enum_scalar_to_str(state, enums.EnableState)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:CCODe:CCSTate {param}')

	def clone(self) -> 'CcodeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcodeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
