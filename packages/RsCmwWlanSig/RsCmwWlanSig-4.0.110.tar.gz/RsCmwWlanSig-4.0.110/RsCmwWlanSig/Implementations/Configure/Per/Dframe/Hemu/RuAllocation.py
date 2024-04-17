from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RuAllocationCls:
	"""RuAllocation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ruAllocation", core, parent)

	def set(self, ch_20_index: enums.Ch20Index, ru_index: enums.RuIndex, alloc_state: enums.RuAlloc) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DFRame:HEMU:RUALlocation \n
		Snippet: driver.configure.per.dframe.hemu.ruAllocation.set(ch_20_index = enums.Ch20Index.CHA1, ru_index = enums.RuIndex.RU1, alloc_state = enums.RuAlloc.DMY1) \n
		Configures allocations for specified channel and resource unit (RU) . Maps a user to the RU, sets the size of allocation. \n
			:param ch_20_index: CHA1 | CHA2 | CHA3 | CHA4
			:param ru_index: RU1 | RU2 | RU3 | RU4 | RU5 | RU6 | RU7 | RU8 | RU9 Resource unit selection
			:param alloc_state: OFF | USR1 | DMY1 | DMY2 | DMY3 User mapping for to the selected RU
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ch_20_index', ch_20_index, DataType.Enum, enums.Ch20Index), ArgSingle('ru_index', ru_index, DataType.Enum, enums.RuIndex), ArgSingle('alloc_state', alloc_state, DataType.Enum, enums.RuAlloc))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DFRame:HEMU:RUALlocation {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Alloc_State: enums.RuAlloc: OFF | USR1 | DMY1 | DMY2 | DMY3 User mapping for to the selected RU
			- Size: enums.AllocSize: T26 | T52 | T106 | T242 | T484 | T996 | T2X9 RU size: 26-, 52-, 106-, 242-, 484, 996-tone RU, 2x996-tone RU"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Alloc_State', enums.RuAlloc),
			ArgStruct.scalar_enum('Size', enums.AllocSize)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Alloc_State: enums.RuAlloc = None
			self.Size: enums.AllocSize = None

	def get(self, ch_20_index: enums.Ch20Index, ru_index: enums.RuIndex) -> GetStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DFRame:HEMU:RUALlocation \n
		Snippet: value: GetStruct = driver.configure.per.dframe.hemu.ruAllocation.get(ch_20_index = enums.Ch20Index.CHA1, ru_index = enums.RuIndex.RU1) \n
		Configures allocations for specified channel and resource unit (RU) . Maps a user to the RU, sets the size of allocation. \n
			:param ch_20_index: CHA1 | CHA2 | CHA3 | CHA4
			:param ru_index: RU1 | RU2 | RU3 | RU4 | RU5 | RU6 | RU7 | RU8 | RU9 Resource unit selection
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ch_20_index', ch_20_index, DataType.Enum, enums.Ch20Index), ArgSingle('ru_index', ru_index, DataType.Enum, enums.RuIndex))
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DFRame:HEMU:RUALlocation? {param}'.rstrip(), self.__class__.GetStruct())
