from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PayloadCls:
	"""Payload commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("payload", core, parent)

	def get_size(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:PAYLoad:SIZE \n
		Snippet: value: int = driver.configure.per.payload.get_size() \n
		Specifies the payload size (in bytes) for the PER measurement. \n
			:return: size: integer Range: see table below , Unit: byte
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:PER:PAYLoad:SIZE?')
		return Conversions.str_to_int(response)

	def set_size(self, size: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:PAYLoad:SIZE \n
		Snippet: driver.configure.per.payload.set_size(size = 1) \n
		Specifies the payload size (in bytes) for the PER measurement. \n
			:param size: integer Range: see table below , Unit: byte
		"""
		param = Conversions.decimal_value_to_str(size)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:PAYLoad:SIZE {param}')
