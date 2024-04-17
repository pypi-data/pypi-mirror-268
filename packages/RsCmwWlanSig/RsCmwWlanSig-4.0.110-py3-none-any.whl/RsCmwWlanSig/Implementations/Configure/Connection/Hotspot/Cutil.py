from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CutilCls:
	"""Cutil commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cutil", core, parent)

	def set(self, station_count: int, channel_utilization: int, available_admission_capacity: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HOTSpot:CUTil \n
		Snippet: driver.configure.connection.hotspot.cutil.set(station_count = 1, channel_utilization = 1, available_admission_capacity = 1) \n
		Configures the contents of the BSS load element. \n
			:param station_count: numeric Number of stations that are currently associated with the BSS Range: 0 to 65535
			:param channel_utilization: numeric Percentage of time, that the access point sensed the primary channel was busy Range: 0 % to 100 %, Unit: %
			:param available_admission_capacity: numeric Remaining time available via explicit admission control, in units of 32 μs/s Range: 0 to 31250
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('station_count', station_count, DataType.Integer), ArgSingle('channel_utilization', channel_utilization, DataType.Integer), ArgSingle('available_admission_capacity', available_admission_capacity, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HOTSpot:CUTil {param}'.rstrip())

	# noinspection PyTypeChecker
	class CutilStruct(StructBase):
		"""Response structure. Fields: \n
			- Station_Count: int: numeric Number of stations that are currently associated with the BSS Range: 0 to 65535
			- Channel_Utilization: int: numeric Percentage of time, that the access point sensed the primary channel was busy Range: 0 % to 100 %, Unit: %
			- Available_Admission_Capacity: int: numeric Remaining time available via explicit admission control, in units of 32 μs/s Range: 0 to 31250"""
		__meta_args_list = [
			ArgStruct.scalar_int('Station_Count'),
			ArgStruct.scalar_int('Channel_Utilization'),
			ArgStruct.scalar_int('Available_Admission_Capacity')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Station_Count: int = None
			self.Channel_Utilization: int = None
			self.Available_Admission_Capacity: int = None

	def get(self) -> CutilStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HOTSpot:CUTil \n
		Snippet: value: CutilStruct = driver.configure.connection.hotspot.cutil.get() \n
		Configures the contents of the BSS load element. \n
			:return: structure: for return value, see the help for CutilStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HOTSpot:CUTil?', self.__class__.CutilStruct())
