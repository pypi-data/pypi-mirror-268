from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ActionCls:
	"""Action commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("action", core, parent)

	@property
	def wps(self):
		"""wps commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wps'):
			from .Wps import WpsCls
			self._wps = WpsCls(self._core, self._cmd_group)
		return self._wps

	@property
	def wdirect(self):
		"""wdirect commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wdirect'):
			from .Wdirect import WdirectCls
			self._wdirect = WdirectCls(self._core, self._cmd_group)
		return self._wdirect

	@property
	def station(self):
		"""station commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_station'):
			from .Station import StationCls
			self._station = StationCls(self._core, self._cmd_group)
		return self._station

	def clone(self) -> 'ActionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ActionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
