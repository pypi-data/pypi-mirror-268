from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PgenCls:
	"""Pgen commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: PacketGenerator, default value after init: PacketGenerator.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pgen", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_packetGenerator_get', 'repcap_packetGenerator_set', repcap.PacketGenerator.Nr1)

	def repcap_packetGenerator_set(self, packetGenerator: repcap.PacketGenerator) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PacketGenerator.Default
		Default value after init: PacketGenerator.Nr1"""
		self._cmd_group.set_repcap_enum_value(packetGenerator)

	def repcap_packetGenerator_get(self) -> repcap.PacketGenerator:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def pgStats(self):
		"""pgStats commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pgStats'):
			from .PgStats import PgStatsCls
			self._pgStats = PgStatsCls(self._core, self._cmd_group)
		return self._pgStats

	def clone(self) -> 'PgenCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PgenCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
