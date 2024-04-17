from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SenseCls:
	"""Sense commands group definition. 21 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def uesInfo(self):
		"""uesInfo commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_uesInfo'):
			from .UesInfo import UesInfoCls
			self._uesInfo = UesInfoCls(self._core, self._cmd_group)
		return self._uesInfo

	@property
	def sta(self):
		"""sta commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sta'):
			from .Sta import StaCls
			self._sta = StaCls(self._core, self._cmd_group)
		return self._sta

	@property
	def pgen(self):
		"""pgen commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pgen'):
			from .Pgen import PgenCls
			self._pgen = PgenCls(self._core, self._cmd_group)
		return self._pgen

	@property
	def sinfo(self):
		"""sinfo commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sinfo'):
			from .Sinfo import SinfoCls
			self._sinfo = SinfoCls(self._core, self._cmd_group)
		return self._sinfo

	@property
	def elogging(self):
		"""elogging commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_elogging'):
			from .Elogging import EloggingCls
			self._elogging = EloggingCls(self._core, self._cmd_group)
		return self._elogging

	def clone(self) -> 'SenseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SenseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
