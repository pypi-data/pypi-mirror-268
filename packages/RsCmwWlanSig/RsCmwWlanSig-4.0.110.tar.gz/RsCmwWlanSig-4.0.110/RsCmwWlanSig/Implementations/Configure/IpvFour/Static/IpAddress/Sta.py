from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StaCls:
	"""Sta commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sta", core, parent)

	def set(self, first_number: int, sec_number: int, third_number: int, fourth_number: int, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:IPVFour:STATic:IPADdress:STA<s> \n
		Snippet: driver.configure.ipvFour.static.ipAddress.sta.set(first_number = 1, sec_number = 1, third_number = 1, fourth_number = 1, station = repcap.Station.Default) \n
		Defines the static IP V4 address of the DUT. The setting is only relevant for access point and instruments without a DAU. \n
			:param first_number: No help available
			:param sec_number: No help available
			:param third_number: No help available
			:param fourth_number: No help available
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Static')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('first_number', first_number, DataType.Integer), ArgSingle('sec_number', sec_number, DataType.Integer), ArgSingle('third_number', third_number, DataType.Integer), ArgSingle('fourth_number', fourth_number, DataType.Integer))
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:IPVFour:STATic:IPADdress:STA{station_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class StaStruct(StructBase):
		"""Response structure. Fields: \n
			- First_Number: int: No parameter help available
			- Sec_Number: int: No parameter help available
			- Third_Number: int: No parameter help available
			- Fourth_Number: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('First_Number'),
			ArgStruct.scalar_int('Sec_Number'),
			ArgStruct.scalar_int('Third_Number'),
			ArgStruct.scalar_int('Fourth_Number')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.First_Number: int = None
			self.Sec_Number: int = None
			self.Third_Number: int = None
			self.Fourth_Number: int = None

	def get(self, station=repcap.Station.Default) -> StaStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:IPVFour:STATic:IPADdress:STA<s> \n
		Snippet: value: StaStruct = driver.configure.ipvFour.static.ipAddress.sta.get(station = repcap.Station.Default) \n
		Defines the static IP V4 address of the DUT. The setting is only relevant for access point and instruments without a DAU. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Static')
			:return: structure: for return value, see the help for StaStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:IPVFour:STATic:IPADdress:STA{station_cmd_val}?', self.__class__.StaStruct())
