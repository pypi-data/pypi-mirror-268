from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FadingCls:
	"""Fading commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fading", core, parent)

	@property
	def fsimulator(self):
		"""fsimulator commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_fsimulator'):
			from .Fsimulator import FsimulatorCls
			self._fsimulator = FsimulatorCls(self._core, self._cmd_group)
		return self._fsimulator

	@property
	def awgn(self):
		"""awgn commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import AwgnCls
			self._awgn = AwgnCls(self._core, self._cmd_group)
		return self._awgn

	def clone(self) -> 'FadingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FadingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
