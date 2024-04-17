from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FsimulatorCls:
	"""Fsimulator commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fsimulator", core, parent)

	@property
	def iloss(self):
		"""iloss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iloss'):
			from .Iloss import IlossCls
			self._iloss = IlossCls(self._core, self._cmd_group)
		return self._iloss

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.Profile:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:FSIMulator:STANdard \n
		Snippet: value: enums.Profile = driver.configure.fading.fsimulator.get_standard() \n
		Selects a propagation condition profile for fading, see 'Predefined fading settings'. \n
			:return: profile: MODA | MODB | MODC | MODD | MODE | MODF Mode A to F
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:FADing:FSIMulator:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.Profile)

	def set_standard(self, profile: enums.Profile) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:FSIMulator:STANdard \n
		Snippet: driver.configure.fading.fsimulator.set_standard(profile = enums.Profile.MODA) \n
		Selects a propagation condition profile for fading, see 'Predefined fading settings'. \n
			:param profile: MODA | MODB | MODC | MODD | MODE | MODF Mode A to F
		"""
		param = Conversions.enum_scalar_to_str(profile, enums.Profile)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:FADing:FSIMulator:STANdard {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:FSIMulator:ENABle \n
		Snippet: value: bool = driver.configure.fading.fsimulator.get_enable() \n
		Enables/disables the fading simulator. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:FADing:FSIMulator:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:FSIMulator:ENABle \n
		Snippet: driver.configure.fading.fsimulator.set_enable(enable = False) \n
		Enables/disables the fading simulator. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:FADing:FSIMulator:ENABle {param}')

	def clone(self) -> 'FsimulatorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FsimulatorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
