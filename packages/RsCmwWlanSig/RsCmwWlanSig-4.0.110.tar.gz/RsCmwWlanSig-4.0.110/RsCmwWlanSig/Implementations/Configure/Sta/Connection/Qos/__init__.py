from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QosCls:
	"""Qos commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qos", core, parent)

	@property
	def barMethod(self):
		"""barMethod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_barMethod'):
			from .BarMethod import BarMethodCls
			self._barMethod = BarMethodCls(self._core, self._cmd_group)
		return self._barMethod

	@property
	def black(self):
		"""black commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_black'):
			from .Black import BlackCls
			self._black = BlackCls(self._core, self._cmd_group)
		return self._black

	def clone(self) -> 'QosCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = QosCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
