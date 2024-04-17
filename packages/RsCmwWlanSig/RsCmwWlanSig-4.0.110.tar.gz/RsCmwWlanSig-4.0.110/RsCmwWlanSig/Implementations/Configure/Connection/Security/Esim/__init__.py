from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsimCls:
	"""Esim commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("esim", core, parent)

	@property
	def ktThree(self):
		"""ktThree commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ktThree'):
			from .KtThree import KtThreeCls
			self._ktThree = KtThreeCls(self._core, self._cmd_group)
		return self._ktThree

	@property
	def ktTwo(self):
		"""ktTwo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ktTwo'):
			from .KtTwo import KtTwoCls
			self._ktTwo = KtTwoCls(self._core, self._cmd_group)
		return self._ktTwo

	@property
	def ktone(self):
		"""ktone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ktone'):
			from .Ktone import KtoneCls
			self._ktone = KtoneCls(self._core, self._cmd_group)
		return self._ktone

	def clone(self) -> 'EsimCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EsimCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
