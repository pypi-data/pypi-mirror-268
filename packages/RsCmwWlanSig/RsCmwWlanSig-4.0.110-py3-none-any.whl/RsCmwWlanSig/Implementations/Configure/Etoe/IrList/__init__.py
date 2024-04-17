from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IrListCls:
	"""IrList commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("irList", core, parent)

	@property
	def iprAddress(self):
		"""iprAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iprAddress'):
			from .IprAddress import IprAddressCls
			self._iprAddress = IprAddressCls(self._core, self._cmd_group)
		return self._iprAddress

	def clone(self) -> 'IrListCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IrListCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
