from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BtwtCls:
	"""Btwt commands group definition. 6 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btwt", core, parent)

	@property
	def schedule(self):
		"""schedule commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_schedule'):
			from .Schedule import ScheduleCls
			self._schedule = ScheduleCls(self._core, self._cmd_group)
		return self._schedule

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BTWT:ENABle \n
		Snippet: value: bool = driver.configure.connection.btwt.get_enable() \n
		Enables/ disables broadcast target wake time (TWT) operation. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:BTWT:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BTWT:ENABle \n
		Snippet: driver.configure.connection.btwt.set_enable(enable = False) \n
		Enables/ disables broadcast target wake time (TWT) operation. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BTWT:ENABle {param}')

	def clone(self) -> 'BtwtCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BtwtCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
