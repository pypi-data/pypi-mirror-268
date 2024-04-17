from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AssociationCls:
	"""Association commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("association", core, parent)

	@property
	def sta(self):
		"""sta commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sta'):
			from .Sta import StaCls
			self._sta = StaCls(self._core, self._cmd_group)
		return self._sta

	@property
	def disass(self):
		"""disass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_disass'):
			from .Disass import DisassCls
			self._disass = DisassCls(self._core, self._cmd_group)
		return self._disass

	def get_preemption(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:ASSociation:PREemption \n
		Snippet: value: bool = driver.configure.connection.association.get_preemption() \n
		If enabled, then the existing association possible with any MAC addresses is replaced by a new incoming one. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:ASSociation:PREemption?')
		return Conversions.str_to_bool(response)

	def set_preemption(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:ASSociation:PREemption \n
		Snippet: driver.configure.connection.association.set_preemption(enable = False) \n
		If enabled, then the existing association possible with any MAC addresses is replaced by a new incoming one. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:ASSociation:PREemption {param}')

	# noinspection PyTypeChecker
	def get_sta_priority(self) -> enums.PrioModeB:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:ASSociation:STAPriority \n
		Snippet: value: enums.PrioModeB = driver.configure.connection.association.get_sta_priority() \n
		Specifies how the stack prioritizes one STA over another in multi-STA connections. \n
			:return: mode: AUTO | ROURobin Automatic or round robin
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:ASSociation:STAPriority?')
		return Conversions.str_to_scalar_enum(response, enums.PrioModeB)

	def set_sta_priority(self, mode: enums.PrioModeB) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:ASSociation:STAPriority \n
		Snippet: driver.configure.connection.association.set_sta_priority(mode = enums.PrioModeB.AUTO) \n
		Specifies how the stack prioritizes one STA over another in multi-STA connections. \n
			:param mode: AUTO | ROURobin Automatic or round robin
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PrioModeB)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:ASSociation:STAPriority {param}')

	def clone(self) -> 'AssociationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AssociationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
