from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpControlCls:
	"""TpControl commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpControl", core, parent)

	def get_pw_constraint(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:TPControl:PWConstraint \n
		Snippet: value: int = driver.configure.connection.tpControl.get_pw_constraint() \n
		Reduces the maximum power of the AP beyond the regulatory limits. \n
			:return: power: numeric Range: 0 dB to 255 dB
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:TPControl:PWConstraint?')
		return Conversions.str_to_int(response)

	def set_pw_constraint(self, power: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:TPControl:PWConstraint \n
		Snippet: driver.configure.connection.tpControl.set_pw_constraint(power = 1) \n
		Reduces the maximum power of the AP beyond the regulatory limits. \n
			:param power: numeric Range: 0 dB to 255 dB
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:TPControl:PWConstraint {param}')

	# noinspection PyTypeChecker
	def get_regulatory(self) -> enums.TpControl:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:TPControl:REGulatory \n
		Snippet: value: enums.TpControl = driver.configure.connection.tpControl.get_regulatory() \n
		Sets one of different AP types with different power constraints in 6 GHz band. \n
			:return: type_py: INDoor | STANdard | VERYlowpow | INENabled | INSTdpower IND: Indoor AP STAN: Standard power AP VERY: Very low power AP INEN: Indoor enabled AP INST: Indoor standard power AP
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:TPControl:REGulatory?')
		return Conversions.str_to_scalar_enum(response, enums.TpControl)

	def set_regulatory(self, type_py: enums.TpControl) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:TPControl:REGulatory \n
		Snippet: driver.configure.connection.tpControl.set_regulatory(type_py = enums.TpControl.INDoor) \n
		Sets one of different AP types with different power constraints in 6 GHz band. \n
			:param type_py: INDoor | STANdard | VERYlowpow | INENabled | INSTdpower IND: Indoor AP STAN: Standard power AP VERY: Very low power AP INEN: Indoor enabled AP INST: Indoor standard power AP
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TpControl)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:TPControl:REGulatory {param}')
