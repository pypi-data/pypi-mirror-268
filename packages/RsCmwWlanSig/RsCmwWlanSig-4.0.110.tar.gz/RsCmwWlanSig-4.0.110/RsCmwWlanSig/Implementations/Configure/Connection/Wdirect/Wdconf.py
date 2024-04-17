from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WdconfCls:
	"""Wdconf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wdconf", core, parent)

	def set(self, manufacturer: str, model_name: str, model_number: str, serial_number: str, device_name: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:WDIRect:WDConf \n
		Snippet: driver.configure.connection.wdirect.wdconf.set(manufacturer = 'abc', model_name = 'abc', model_number = 'abc', serial_number = 'abc', device_name = 'abc') \n
		No command help available \n
			:param manufacturer: No help available
			:param model_name: No help available
			:param model_number: No help available
			:param serial_number: No help available
			:param device_name: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('manufacturer', manufacturer, DataType.String), ArgSingle('model_name', model_name, DataType.String), ArgSingle('model_number', model_number, DataType.String), ArgSingle('serial_number', serial_number, DataType.String), ArgSingle('device_name', device_name, DataType.String))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:WDIRect:WDConf {param}'.rstrip())

	# noinspection PyTypeChecker
	class WdconfStruct(StructBase):
		"""Response structure. Fields: \n
			- Manufacturer: str: No parameter help available
			- Model_Name: str: No parameter help available
			- Model_Number: str: No parameter help available
			- Serial_Number: str: No parameter help available
			- Device_Name: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Manufacturer'),
			ArgStruct.scalar_str('Model_Name'),
			ArgStruct.scalar_str('Model_Number'),
			ArgStruct.scalar_str('Serial_Number'),
			ArgStruct.scalar_str('Device_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Manufacturer: str = None
			self.Model_Name: str = None
			self.Model_Number: str = None
			self.Serial_Number: str = None
			self.Device_Name: str = None

	def get(self) -> WdconfStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:WDIRect:WDConf \n
		Snippet: value: WdconfStruct = driver.configure.connection.wdirect.wdconf.get() \n
		No command help available \n
			:return: structure: for return value, see the help for WdconfStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:WDIRect:WDConf?', self.__class__.WdconfStruct())
