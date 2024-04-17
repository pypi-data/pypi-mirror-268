from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AtypeCls:
	"""Atype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atype", core, parent)

	def set(self, method: enums.AuthMethod, mode: enums.AutoManualMode, pin: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:WDIRect:ATYPe \n
		Snippet: driver.configure.connection.wdirect.atype.set(method = enums.AuthMethod.DISPlay, mode = enums.AutoManualMode.AUTO, pin = 'abc') \n
		No command help available \n
			:param method: No help available
			:param mode: No help available
			:param pin: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('method', method, DataType.Enum, enums.AuthMethod), ArgSingle('mode', mode, DataType.Enum, enums.AutoManualMode), ArgSingle('pin', pin, DataType.String))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:WDIRect:ATYPe {param}'.rstrip())

	# noinspection PyTypeChecker
	class AtypeStruct(StructBase):
		"""Response structure. Fields: \n
			- Method: enums.AuthMethod: No parameter help available
			- Mode: enums.AutoManualMode: No parameter help available
			- Pin: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Method', enums.AuthMethod),
			ArgStruct.scalar_enum('Mode', enums.AutoManualMode),
			ArgStruct.scalar_str('Pin')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Method: enums.AuthMethod = None
			self.Mode: enums.AutoManualMode = None
			self.Pin: str = None

	def get(self) -> AtypeStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:WDIRect:ATYPe \n
		Snippet: value: AtypeStruct = driver.configure.connection.wdirect.atype.get() \n
		No command help available \n
			:return: structure: for return value, see the help for AtypeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:WDIRect:ATYPe?', self.__class__.AtypeStruct())
