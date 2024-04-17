from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UesInfoCls:
	"""UesInfo commands group definition. 10 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uesInfo", core, parent)

	@property
	def rxbPower(self):
		"""rxbPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxbPower'):
			from .RxbPower import RxbPowerCls
			self._rxbPower = RxbPowerCls(self._core, self._cmd_group)
		return self._rxbPower

	@property
	def drate(self):
		"""drate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_drate'):
			from .Drate import DrateCls
			self._drate = DrateCls(self._core, self._cmd_group)
		return self._drate

	@property
	def absReport(self):
		"""absReport commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absReport'):
			from .AbsReport import AbsReportCls
			self._absReport = AbsReportCls(self._core, self._cmd_group)
		return self._absReport

	@property
	def rxPsdu(self):
		"""rxPsdu commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_rxPsdu'):
			from .RxPsdu import RxPsduCls
			self._rxPsdu = RxPsduCls(self._core, self._cmd_group)
		return self._rxPsdu

	@property
	def ueAddress(self):
		"""ueAddress commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueAddress'):
			from .UeAddress import UeAddressCls
			self._ueAddress = UeAddressCls(self._core, self._cmd_group)
		return self._ueAddress

	def clone(self) -> 'UesInfoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UesInfoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
