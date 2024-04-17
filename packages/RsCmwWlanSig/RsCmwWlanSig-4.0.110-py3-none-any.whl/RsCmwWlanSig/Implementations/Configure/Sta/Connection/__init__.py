from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectionCls:
	"""Connection commands group definition. 13 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connection", core, parent)

	@property
	def qos(self):
		"""qos commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_qos'):
			from .Qos import QosCls
			self._qos = QosCls(self._core, self._cmd_group)
		return self._qos

	@property
	def dfdef(self):
		"""dfdef commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfdef'):
			from .Dfdef import DfdefCls
			self._dfdef = DfdefCls(self._core, self._cmd_group)
		return self._dfdef

	@property
	def hetf(self):
		"""hetf commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_hetf'):
			from .Hetf import HetfCls
			self._hetf = HetfCls(self._core, self._cmd_group)
		return self._hetf

	@property
	def ampdu(self):
		"""ampdu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ampdu'):
			from .Ampdu import AmpduCls
			self._ampdu = AmpduCls(self._core, self._cmd_group)
		return self._ampdu

	def clone(self) -> 'ConnectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConnectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
