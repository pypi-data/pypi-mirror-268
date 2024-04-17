from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HemacCls:
	"""Hemac commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hemac", core, parent)

	def get_bsr_support(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HEMac:BSRSupport \n
		Snippet: value: bool = driver.configure.connection.hemac.get_bsr_support() \n
		Indicates, whether the R&S CMW supports the buffer status report (BSR) . \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HEMac:BSRSupport?')
		return Conversions.str_to_bool(response)

	def set_bsr_support(self, supported: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HEMac:BSRSupport \n
		Snippet: driver.configure.connection.hemac.set_bsr_support(supported = False) \n
		Indicates, whether the R&S CMW supports the buffer status report (BSR) . \n
			:param supported: OFF | ON
		"""
		param = Conversions.bool_to_str(supported)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HEMac:BSRSupport {param}')
