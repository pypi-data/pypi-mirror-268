from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TwtCls:
	"""Twt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("twt", core, parent)

	def get_required(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:TWT:REQuired \n
		Snippet: value: bool = driver.configure.connection.twt.get_required() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:TWT:REQuired?')
		return Conversions.str_to_bool(response)

	def set_required(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:TWT:REQuired \n
		Snippet: driver.configure.connection.twt.set_required(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:TWT:REQuired {param}')
