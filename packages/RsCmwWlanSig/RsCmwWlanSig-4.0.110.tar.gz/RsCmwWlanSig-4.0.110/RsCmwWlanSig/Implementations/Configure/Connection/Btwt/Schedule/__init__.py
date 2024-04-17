from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScheduleCls:
	"""Schedule commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("schedule", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def ftype(self):
		"""ftype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ftype'):
			from .Ftype import FtypeCls
			self._ftype = FtypeCls(self._core, self._cmd_group)
		return self._ftype

	@property
	def stime(self):
		"""stime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stime'):
			from .Stime import StimeCls
			self._stime = StimeCls(self._core, self._cmd_group)
		return self._stime

	@property
	def mwDuration(self):
		"""mwDuration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mwDuration'):
			from .MwDuration import MwDurationCls
			self._mwDuration = MwDurationCls(self._core, self._cmd_group)
		return self._mwDuration

	@property
	def tenable(self):
		"""tenable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tenable'):
			from .Tenable import TenableCls
			self._tenable = TenableCls(self._core, self._cmd_group)
		return self._tenable

	def clone(self) -> 'ScheduleCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScheduleCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
