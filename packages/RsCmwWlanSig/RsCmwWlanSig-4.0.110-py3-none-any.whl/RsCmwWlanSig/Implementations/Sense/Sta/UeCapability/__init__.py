from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCapabilityCls:
	"""UeCapability commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueCapability", core, parent)

	@property
	def mac(self):
		"""mac commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import MacCls
			self._mac = MacCls(self._core, self._cmd_group)
		return self._mac

	@property
	def he(self):
		"""he commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_he'):
			from .He import HeCls
			self._he = HeCls(self._core, self._cmd_group)
		return self._he

	def clone(self) -> 'UeCapabilityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCapabilityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
