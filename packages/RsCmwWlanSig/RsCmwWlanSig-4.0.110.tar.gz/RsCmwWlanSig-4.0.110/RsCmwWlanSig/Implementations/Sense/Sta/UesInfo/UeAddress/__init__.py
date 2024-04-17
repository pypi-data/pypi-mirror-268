from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeAddressCls:
	"""UeAddress commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: IpVersion, default value after init: IpVersion.V4"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueAddress", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_ipVersion_get', 'repcap_ipVersion_set', repcap.IpVersion.V4)

	def repcap_ipVersion_set(self, ipVersion: repcap.IpVersion) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IpVersion.Default
		Default value after init: IpVersion.V4"""
		self._cmd_group.set_repcap_enum_value(ipVersion)

	def repcap_ipVersion_get(self) -> repcap.IpVersion:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def ipv(self):
		"""ipv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipv'):
			from .Ipv import IpvCls
			self._ipv = IpvCls(self._core, self._cmd_group)
		return self._ipv

	def clone(self) -> 'UeAddressCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeAddressCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
