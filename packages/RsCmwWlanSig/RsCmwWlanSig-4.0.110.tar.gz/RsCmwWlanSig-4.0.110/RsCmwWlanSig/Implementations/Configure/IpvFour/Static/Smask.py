from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmaskCls:
	"""Smask commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smask", core, parent)

	def set(self, first_octet: int, second_octet: int, third_octet: int, fourth_octet: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:IPVFour:STATic:SMASk \n
		Snippet: driver.configure.ipvFour.static.smask.set(first_octet = 1, second_octet = 1, third_octet = 1, fourth_octet = 1) \n
		Specifies the subnet mask of the built-in IPv4 stack. The setting is relevant for instruments without DAU. \n
			:param first_octet: No help available
			:param second_octet: No help available
			:param third_octet: No help available
			:param fourth_octet: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('first_octet', first_octet, DataType.Integer), ArgSingle('second_octet', second_octet, DataType.Integer), ArgSingle('third_octet', third_octet, DataType.Integer), ArgSingle('fourth_octet', fourth_octet, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:IPVFour:STATic:SMASk {param}'.rstrip())

	# noinspection PyTypeChecker
	class SmaskStruct(StructBase):
		"""Response structure. Fields: \n
			- First_Octet: int: No parameter help available
			- Second_Octet: int: No parameter help available
			- Third_Octet: int: No parameter help available
			- Fourth_Octet: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('First_Octet'),
			ArgStruct.scalar_int('Second_Octet'),
			ArgStruct.scalar_int('Third_Octet'),
			ArgStruct.scalar_int('Fourth_Octet')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.First_Octet: int = None
			self.Second_Octet: int = None
			self.Third_Octet: int = None
			self.Fourth_Octet: int = None

	def get(self) -> SmaskStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:IPVFour:STATic:SMASk \n
		Snippet: value: SmaskStruct = driver.configure.ipvFour.static.smask.get() \n
		Specifies the subnet mask of the built-in IPv4 stack. The setting is relevant for instruments without DAU. \n
			:return: structure: for return value, see the help for SmaskStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:IPVFour:STATic:SMASk?', self.__class__.SmaskStruct())
