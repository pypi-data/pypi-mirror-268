from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HemuCls:
	"""Hemu commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hemu", core, parent)

	@property
	def alsField(self):
		"""alsField commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alsField'):
			from .AlsField import AlsFieldCls
			self._alsField = AlsFieldCls(self._core, self._cmd_group)
		return self._alsField

	@property
	def ruAllocation(self):
		"""ruAllocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ruAllocation'):
			from .RuAllocation import RuAllocationCls
			self._ruAllocation = RuAllocationCls(self._core, self._cmd_group)
		return self._ruAllocation

	@property
	def blAllocation(self):
		"""blAllocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blAllocation'):
			from .BlAllocation import BlAllocationCls
			self._blAllocation = BlAllocationCls(self._core, self._cmd_group)
		return self._blAllocation

	@property
	def user(self):
		"""user commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import UserCls
			self._user = UserCls(self._core, self._cmd_group)
		return self._user

	@property
	def dummy(self):
		"""dummy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dummy'):
			from .Dummy import DummyCls
			self._dummy = DummyCls(self._core, self._cmd_group)
		return self._dummy

	def clone(self) -> 'HemuCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HemuCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
