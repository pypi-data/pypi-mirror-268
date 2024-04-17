from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddressCls:
	"""IpAddress commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipAddress", core, parent)

	@property
	def cmw(self):
		"""cmw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmw'):
			from .Cmw import CmwCls
			self._cmw = CmwCls(self._core, self._cmd_group)
		return self._cmw

	@property
	def sta(self):
		"""sta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sta'):
			from .Sta import StaCls
			self._sta = StaCls(self._core, self._cmd_group)
		return self._sta

	@property
	def gateway(self):
		"""gateway commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gateway'):
			from .Gateway import GatewayCls
			self._gateway = GatewayCls(self._core, self._cmd_group)
		return self._gateway

	@property
	def dns(self):
		"""dns commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dns'):
			from .Dns import DnsCls
			self._dns = DnsCls(self._core, self._cmd_group)
		return self._dns

	@property
	def stack(self):
		"""stack commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stack'):
			from .Stack import StackCls
			self._stack = StackCls(self._core, self._cmd_group)
		return self._stack

	@property
	def destination(self):
		"""destination commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_destination'):
			from .Destination import DestinationCls
			self._destination = DestinationCls(self._core, self._cmd_group)
		return self._destination

	def clone(self) -> 'IpAddressCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpAddressCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
