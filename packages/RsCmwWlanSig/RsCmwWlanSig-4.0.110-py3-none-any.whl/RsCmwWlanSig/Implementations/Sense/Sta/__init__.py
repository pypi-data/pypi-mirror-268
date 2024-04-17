from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StaCls:
	"""Sta commands group definition. 13 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: Station, default value after init: Station.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sta", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_station_get', 'repcap_station_set', repcap.Station.Nr1)

	def repcap_station_set(self, station: repcap.Station) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Station.Default
		Default value after init: Station.Nr1"""
		self._cmd_group.set_repcap_enum_value(station)

	def repcap_station_get(self) -> repcap.Station:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def uesInfo(self):
		"""uesInfo commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_uesInfo'):
			from .UesInfo import UesInfoCls
			self._uesInfo = UesInfoCls(self._core, self._cmd_group)
		return self._uesInfo

	@property
	def ueCapability(self):
		"""ueCapability commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueCapability'):
			from .UeCapability import UeCapabilityCls
			self._ueCapability = UeCapabilityCls(self._core, self._cmd_group)
		return self._ueCapability

	@property
	def hetbInfo(self):
		"""hetbInfo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hetbInfo'):
			from .HetbInfo import HetbInfoCls
			self._hetbInfo = HetbInfoCls(self._core, self._cmd_group)
		return self._hetbInfo

	def clone(self) -> 'StaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
