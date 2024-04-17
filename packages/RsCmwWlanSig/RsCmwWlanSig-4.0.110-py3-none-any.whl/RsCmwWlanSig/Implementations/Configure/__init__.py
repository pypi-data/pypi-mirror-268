from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 193 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def fading(self):
		"""fading commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Fading import FadingCls
			self._fading = FadingCls(self._core, self._cmd_group)
		return self._fading

	@property
	def edau(self):
		"""edau commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_edau'):
			from .Edau import EdauCls
			self._edau = EdauCls(self._core, self._cmd_group)
		return self._edau

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def uesInfo(self):
		"""uesInfo commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_uesInfo'):
			from .UesInfo import UesInfoCls
			self._uesInfo = UesInfoCls(self._core, self._cmd_group)
		return self._uesInfo

	@property
	def etoe(self):
		"""etoe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_etoe'):
			from .Etoe import EtoeCls
			self._etoe = EtoeCls(self._core, self._cmd_group)
		return self._etoe

	@property
	def rfSettings(self):
		"""rfSettings commands group. 2 Sub-classes, 12 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def connection(self):
		"""connection commands group. 21 Sub-classes, 13 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import ConnectionCls
			self._connection = ConnectionCls(self._core, self._cmd_group)
		return self._connection

	@property
	def sta(self):
		"""sta commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sta'):
			from .Sta import StaCls
			self._sta = StaCls(self._core, self._cmd_group)
		return self._sta

	@property
	def pgen(self):
		"""pgen commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pgen'):
			from .Pgen import PgenCls
			self._pgen = PgenCls(self._core, self._cmd_group)
		return self._pgen

	@property
	def ipvSix(self):
		"""ipvSix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipvSix'):
			from .IpvSix import IpvSixCls
			self._ipvSix = IpvSixCls(self._core, self._cmd_group)
		return self._ipvSix

	@property
	def ipvFour(self):
		"""ipvFour commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipvFour'):
			from .IpvFour import IpvFourCls
			self._ipvFour = IpvFourCls(self._core, self._cmd_group)
		return self._ipvFour

	@property
	def hetBased(self):
		"""hetBased commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hetBased'):
			from .HetBased import HetBasedCls
			self._hetBased = HetBasedCls(self._core, self._cmd_group)
		return self._hetBased

	@property
	def per(self):
		"""per commands group. 2 Sub-classes, 8 commands."""
		if not hasattr(self, '_per'):
			from .Per import PerCls
			self._per = PerCls(self._core, self._cmd_group)
		return self._per

	@property
	def mmonitor(self):
		"""mmonitor commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmonitor'):
			from .Mmonitor import MmonitorCls
			self._mmonitor = MmonitorCls(self._core, self._cmd_group)
		return self._mmonitor

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
