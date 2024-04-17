from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MuedcaCls:
	"""Muedca commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("muedca", core, parent)

	@property
	def acbe(self):
		"""acbe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acbe'):
			from .Acbe import AcbeCls
			self._acbe = AcbeCls(self._core, self._cmd_group)
		return self._acbe

	@property
	def acbk(self):
		"""acbk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acbk'):
			from .Acbk import AcbkCls
			self._acbk = AcbkCls(self._core, self._cmd_group)
		return self._acbk

	@property
	def acvi(self):
		"""acvi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acvi'):
			from .Acvi import AcviCls
			self._acvi = AcviCls(self._core, self._cmd_group)
		return self._acvi

	@property
	def acvo(self):
		"""acvo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acvo'):
			from .Acvo import AcvoCls
			self._acvo = AcvoCls(self._core, self._cmd_group)
		return self._acvo

	def clone(self) -> 'MuedcaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MuedcaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
