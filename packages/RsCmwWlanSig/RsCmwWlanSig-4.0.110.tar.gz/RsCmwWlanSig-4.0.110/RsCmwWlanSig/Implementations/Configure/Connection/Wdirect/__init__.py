from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WdirectCls:
	"""Wdirect commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wdirect", core, parent)

	@property
	def atype(self):
		"""atype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atype'):
			from .Atype import AtypeCls
			self._atype = AtypeCls(self._core, self._cmd_group)
		return self._atype

	@property
	def wdconf(self):
		"""wdconf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wdconf'):
			from .Wdconf import WdconfCls
			self._wdconf = WdconfCls(self._core, self._cmd_group)
		return self._wdconf

	def clone(self) -> 'WdirectCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = WdirectCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
