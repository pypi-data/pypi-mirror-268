from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DyFragmentCls:
	"""DyFragment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dyFragment", core, parent)

	def set(self, level: enums.Level, enable_tx: enums.EnableState) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:DYFRagment \n
		Snippet: driver.configure.connection.dyFragment.set(level = enums.Level.LEV0, enable_tx = enums.EnableState.DISable) \n
		No command help available \n
			:param level: No help available
			:param enable_tx: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level', level, DataType.Enum, enums.Level), ArgSingle('enable_tx', enable_tx, DataType.Enum, enums.EnableState))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:DYFRagment {param}'.rstrip())

	# noinspection PyTypeChecker
	class DyFragmentStruct(StructBase):
		"""Response structure. Fields: \n
			- Level: enums.Level: No parameter help available
			- Enable_Tx: enums.EnableState: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Level', enums.Level),
			ArgStruct.scalar_enum('Enable_Tx', enums.EnableState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Level: enums.Level = None
			self.Enable_Tx: enums.EnableState = None

	def get(self) -> DyFragmentStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:DYFRagment \n
		Snippet: value: DyFragmentStruct = driver.configure.connection.dyFragment.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DyFragmentStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:DYFRagment?', self.__class__.DyFragmentStruct())
