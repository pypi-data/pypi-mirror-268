from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdauCls:
	"""Edau commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edau", core, parent)

	def get_nid(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:EDAU:NID \n
		Snippet: value: int = driver.configure.edau.get_nid() \n
		Specifies the subnet node ID of the instrument where the external DAU is installed. \n
			:return: node_id: integer Range: 1 to 254
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:EDAU:NID?')
		return Conversions.str_to_int(response)

	def set_nid(self, node_id: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:EDAU:NID \n
		Snippet: driver.configure.edau.set_nid(node_id = 1) \n
		Specifies the subnet node ID of the instrument where the external DAU is installed. \n
			:param node_id: integer Range: 1 to 254
		"""
		param = Conversions.decimal_value_to_str(node_id)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:EDAU:NID {param}')

	# noinspection PyTypeChecker
	def get_nsegment(self) -> enums.SegmentNumber:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:EDAU:NSEGment \n
		Snippet: value: enums.SegmentNumber = driver.configure.edau.get_nsegment() \n
		Specifies the network segment of the instrument where the external DAU is installed. \n
			:return: segment_number: A | B | C
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:EDAU:NSEGment?')
		return Conversions.str_to_scalar_enum(response, enums.SegmentNumber)

	def set_nsegment(self, segment_number: enums.SegmentNumber) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:EDAU:NSEGment \n
		Snippet: driver.configure.edau.set_nsegment(segment_number = enums.SegmentNumber.A) \n
		Specifies the network segment of the instrument where the external DAU is installed. \n
			:param segment_number: A | B | C
		"""
		param = Conversions.enum_scalar_to_str(segment_number, enums.SegmentNumber)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:EDAU:NSEGment {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:EDAU:ENABle \n
		Snippet: value: bool = driver.configure.edau.get_enable() \n
		Enables usage of an external DAU. \n
			:return: external_dau: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:EDAU:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, external_dau: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:EDAU:ENABle \n
		Snippet: driver.configure.edau.set_enable(external_dau = False) \n
		Enables usage of an external DAU. \n
			:param external_dau: OFF | ON
		"""
		param = Conversions.bool_to_str(external_dau)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:EDAU:ENABle {param}')
