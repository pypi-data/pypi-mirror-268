from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlAllocationCls:
	"""BlAllocation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blAllocation", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ru_1: enums.RuAlloc: OFF | USR1 | DMY1 | DMY2 | DMY3 User mapping for to the corresponding RU (no user, user 1 or dummy user)
			- Size_1: enums.AllocSize: No parameter help available
			- Ru_2: enums.RuAlloc: No parameter help available
			- Size_2: enums.AllocSize: No parameter help available
			- Ru_3: enums.RuAlloc: No parameter help available
			- Size_3: enums.AllocSize: No parameter help available
			- Ru_4: enums.RuAlloc: No parameter help available
			- Size_4: enums.AllocSize: No parameter help available
			- Ru_5: enums.RuAlloc: No parameter help available
			- Size_5: enums.AllocSize: No parameter help available
			- Ru_6: enums.RuAlloc: No parameter help available
			- Size_6: enums.AllocSize: No parameter help available
			- Ru_7: enums.RuAlloc: No parameter help available
			- Size_7: enums.AllocSize: No parameter help available
			- Ru_8: enums.RuAlloc: No parameter help available
			- Size_8: enums.AllocSize: No parameter help available
			- Ru_9: enums.RuAlloc: No parameter help available
			- Size_9: enums.AllocSize: T26 | T52 | T106 | T242 | T484 | T996 | T2X9"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ru_1', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_1', enums.AllocSize),
			ArgStruct.scalar_enum('Ru_2', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_2', enums.AllocSize),
			ArgStruct.scalar_enum('Ru_3', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_3', enums.AllocSize),
			ArgStruct.scalar_enum('Ru_4', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_4', enums.AllocSize),
			ArgStruct.scalar_enum('Ru_5', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_5', enums.AllocSize),
			ArgStruct.scalar_enum('Ru_6', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_6', enums.AllocSize),
			ArgStruct.scalar_enum('Ru_7', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_7', enums.AllocSize),
			ArgStruct.scalar_enum('Ru_8', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_8', enums.AllocSize),
			ArgStruct.scalar_enum('Ru_9', enums.RuAlloc),
			ArgStruct.scalar_enum('Size_9', enums.AllocSize)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ru_1: enums.RuAlloc = None
			self.Size_1: enums.AllocSize = None
			self.Ru_2: enums.RuAlloc = None
			self.Size_2: enums.AllocSize = None
			self.Ru_3: enums.RuAlloc = None
			self.Size_3: enums.AllocSize = None
			self.Ru_4: enums.RuAlloc = None
			self.Size_4: enums.AllocSize = None
			self.Ru_5: enums.RuAlloc = None
			self.Size_5: enums.AllocSize = None
			self.Ru_6: enums.RuAlloc = None
			self.Size_6: enums.AllocSize = None
			self.Ru_7: enums.RuAlloc = None
			self.Size_7: enums.AllocSize = None
			self.Ru_8: enums.RuAlloc = None
			self.Size_8: enums.AllocSize = None
			self.Ru_9: enums.RuAlloc = None
			self.Size_9: enums.AllocSize = None

	def get(self, ch_20_index: enums.Ch20Index, station=repcap.Station.Default) -> GetStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:BLALlocation \n
		Snippet: value: GetStruct = driver.configure.connection.sta.dframe.hemu.blAllocation.get(ch_20_index = enums.Ch20Index.CHA1, station = repcap.Station.Default) \n
		Queries the allocation state and size of an entire 20MHz block for the specified channel. \n
			:param ch_20_index: CHA1 | CHA2 | CHA3 | CHA4
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(ch_20_index, enums.Ch20Index)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:BLALlocation? {param}', self.__class__.GetStruct())
