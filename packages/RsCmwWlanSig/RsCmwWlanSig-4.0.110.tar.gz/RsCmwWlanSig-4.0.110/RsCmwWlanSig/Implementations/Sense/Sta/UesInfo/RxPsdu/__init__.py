from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxPsduCls:
	"""RxPsdu commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rxPsdu", core, parent)

	@property
	def noNht(self):
		"""noNht commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noNht'):
			from .NoNht import NoNhtCls
			self._noNht = NoNhtCls(self._core, self._cmd_group)
		return self._noNht

	@property
	def ht(self):
		"""ht commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ht'):
			from .Ht import HtCls
			self._ht = HtCls(self._core, self._cmd_group)
		return self._ht

	@property
	def vht(self):
		"""vht commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vht'):
			from .Vht import VhtCls
			self._vht = VhtCls(self._core, self._cmd_group)
		return self._vht

	@property
	def hesu(self):
		"""hesu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hesu'):
			from .Hesu import HesuCls
			self._hesu = HesuCls(self._core, self._cmd_group)
		return self._hesu

	@property
	def hemu(self):
		"""hemu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hemu'):
			from .Hemu import HemuCls
			self._hemu = HemuCls(self._core, self._cmd_group)
		return self._hemu

	@property
	def hetb(self):
		"""hetb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hetb'):
			from .Hetb import HetbCls
			self._hetb = HetbCls(self._core, self._cmd_group)
		return self._hetb

	def clone(self) -> 'RxPsduCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxPsduCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
