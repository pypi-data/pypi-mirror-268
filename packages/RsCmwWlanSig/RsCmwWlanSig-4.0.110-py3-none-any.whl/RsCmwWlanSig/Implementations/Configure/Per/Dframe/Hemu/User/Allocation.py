from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllocationCls:
	"""Allocation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("allocation", core, parent)

	def set(self, ch_20_index: enums.Ch20Index, ru_index: enums.RuIndex, user=repcap.User.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DFRame:HEMU:USER<index>:ALLocation \n
		Snippet: driver.configure.per.dframe.hemu.user.allocation.set(ch_20_index = enums.Ch20Index.CHA1, ru_index = enums.RuIndex.RU1, user = repcap.User.Default) \n
		Configures allocations for the user in HE MU PPDU. Maps the user to a resource unit (RU) . \n
			:param ch_20_index: CHA1 | CHA2 | CHA3 | CHA4
			:param ru_index: RU1 | RU2 | RU3 | RU4 | RU5 | RU6 | RU7 | RU8 | RU9
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ch_20_index', ch_20_index, DataType.Enum, enums.Ch20Index), ArgSingle('ru_index', ru_index, DataType.Enum, enums.RuIndex))
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DFRame:HEMU:USER{user_cmd_val}:ALLocation {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllocationStruct(StructBase):
		"""Response structure. Fields: \n
			- Ch_20_Index: enums.Ch20Index: CHA1 | CHA2 | CHA3 | CHA4
			- Ru_Index: enums.RuIndex: RU1 | RU2 | RU3 | RU4 | RU5 | RU6 | RU7 | RU8 | RU9"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ch_20_Index', enums.Ch20Index),
			ArgStruct.scalar_enum('Ru_Index', enums.RuIndex)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ch_20_Index: enums.Ch20Index = None
			self.Ru_Index: enums.RuIndex = None

	def get(self, user=repcap.User.Default) -> AllocationStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DFRame:HEMU:USER<index>:ALLocation \n
		Snippet: value: AllocationStruct = driver.configure.per.dframe.hemu.user.allocation.get(user = repcap.User.Default) \n
		Configures allocations for the user in HE MU PPDU. Maps the user to a resource unit (RU) . \n
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: structure: for return value, see the help for AllocationStruct structure arguments."""
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DFRame:HEMU:USER{user_cmd_val}:ALLocation?', self.__class__.AllocationStruct())
