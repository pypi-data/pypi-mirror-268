from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EtoeCls:
	"""Etoe commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("etoe", core, parent)

	@property
	def irList(self):
		"""irList commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_irList'):
			from .IrList import IrListCls
			self._irList = IrListCls(self._core, self._cmd_group)
		return self._irList

	@property
	def duIp(self):
		"""duIp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duIp'):
			from .DuIp import DuIpCls
			self._duIp = DuIpCls(self._core, self._cmd_group)
		return self._duIp

	def clone(self) -> 'EtoeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EtoeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
