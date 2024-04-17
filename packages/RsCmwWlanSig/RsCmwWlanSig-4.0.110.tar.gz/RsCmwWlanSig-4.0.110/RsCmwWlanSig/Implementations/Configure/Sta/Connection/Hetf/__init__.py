from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HetfCls:
	"""Hetf commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hetf", core, parent)

	@property
	def nss(self):
		"""nss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nss'):
			from .Nss import NssCls
			self._nss = NssCls(self._core, self._cmd_group)
		return self._nss

	@property
	def sss(self):
		"""sss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sss'):
			from .Sss import SssCls
			self._sss = SssCls(self._core, self._cmd_group)
		return self._sss

	@property
	def dcm(self):
		"""dcm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcm'):
			from .Dcm import DcmCls
			self._dcm = DcmCls(self._core, self._cmd_group)
		return self._dcm

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import McsCls
			self._mcs = McsCls(self._core, self._cmd_group)
		return self._mcs

	@property
	def ctyp(self):
		"""ctyp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctyp'):
			from .Ctyp import CtypCls
			self._ctyp = CtypCls(self._core, self._cmd_group)
		return self._ctyp

	@property
	def rual(self):
		"""rual commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rual'):
			from .Rual import RualCls
			self._rual = RualCls(self._core, self._cmd_group)
		return self._rual

	@property
	def trssi(self):
		"""trssi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trssi'):
			from .Trssi import TrssiCls
			self._trssi = TrssiCls(self._core, self._cmd_group)
		return self._trssi

	@property
	def trsMode(self):
		"""trsMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trsMode'):
			from .TrsMode import TrsModeCls
			self._trsMode = TrsModeCls(self._core, self._cmd_group)
		return self._trsMode

	@property
	def tsrControl(self):
		"""tsrControl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsrControl'):
			from .TsrControl import TsrControlCls
			self._tsrControl = TsrControlCls(self._core, self._cmd_group)
		return self._tsrControl

	def clone(self) -> 'HetfCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HetfCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
