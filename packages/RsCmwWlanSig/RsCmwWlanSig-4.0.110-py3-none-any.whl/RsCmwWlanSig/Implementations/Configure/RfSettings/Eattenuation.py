from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EattenuationCls:
	"""Eattenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eattenuation", core, parent)

	def get_input_py(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:EATTenuation:INPut \n
		Snippet: value: float = driver.configure.rfSettings.eattenuation.get_input_py() \n
		No command help available \n
			:return: ext_attenuation: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:EATTenuation:INPut?')
		return Conversions.str_to_float(response)

	def set_input_py(self, ext_attenuation: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:EATTenuation:INPut \n
		Snippet: driver.configure.rfSettings.eattenuation.set_input_py(ext_attenuation = 1.0) \n
		No command help available \n
			:param ext_attenuation: No help available
		"""
		param = Conversions.decimal_value_to_str(ext_attenuation)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:EATTenuation:INPut {param}')
