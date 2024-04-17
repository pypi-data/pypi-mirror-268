from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScenarioCls:
	"""Scenario commands group definition. 5 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenario", core, parent)

	@property
	def mimo(self):
		"""mimo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def scell(self):
		"""scell commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scell'):
			from .Scell import ScellCls
			self._scell = ScellCls(self._core, self._cmd_group)
		return self._scell

	@property
	def scFading(self):
		"""scFading commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scFading'):
			from .ScFading import ScFadingCls
			self._scFading = ScFadingCls(self._core, self._cmd_group)
		return self._scFading

	@property
	def mimFading(self):
		"""mimFading commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mimFading'):
			from .MimFading import MimFadingCls
			self._mimFading = MimFadingCls(self._core, self._cmd_group)
		return self._mimFading

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Scenario:
		"""SCPI: ROUTe:WLAN:SIGNaling<instance>:SCENario \n
		Snippet: value: enums.Scenario = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: scenario: STANdard | MIMO2 | SCFading | MIMFading STANdard Standard SISO scenario MIMO2 MIMO 2x2 (DL and UL) SCFading Standard SISO scenario with fading MIMFading MIMO 2x2 scenario with fading
		"""
		response = self._core.io.query_str('ROUTe:WLAN:SIGNaling<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.Scenario)

	def clone(self) -> 'ScenarioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScenarioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
