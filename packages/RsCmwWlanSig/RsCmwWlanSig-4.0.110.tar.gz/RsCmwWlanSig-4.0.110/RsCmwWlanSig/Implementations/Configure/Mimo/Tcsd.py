from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcsdCls:
	"""Tcsd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcsd", core, parent)

	def set(self, csd_1: int, csd_2: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:MIMO:TCSD \n
		Snippet: driver.configure.mimo.tcsd.set(csd_1 = 1, csd_2 = 1) \n
		No command help available \n
			:param csd_1: No help available
			:param csd_2: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('csd_1', csd_1, DataType.Integer), ArgSingle('csd_2', csd_2, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:MIMO:TCSD {param}'.rstrip())

	# noinspection PyTypeChecker
	class TcsdStruct(StructBase):
		"""Response structure. Fields: \n
			- Csd_1: int: No parameter help available
			- Csd_2: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Csd_1'),
			ArgStruct.scalar_int('Csd_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Csd_1: int = None
			self.Csd_2: int = None

	def get(self) -> TcsdStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:MIMO:TCSD \n
		Snippet: value: TcsdStruct = driver.configure.mimo.tcsd.get() \n
		No command help available \n
			:return: structure: for return value, see the help for TcsdStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:MIMO:TCSD?', self.__class__.TcsdStruct())
