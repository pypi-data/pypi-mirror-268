from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HetbCls:
	"""Hetb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hetb", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Rate: List[enums.DataRate]: No parameter help available
			- Ru_Size: List[enums.RuSize]: No parameter help available
			- Nss: List[enums.SpacialStreamsNr]: No parameter help available
			- Frames_Curr: List[int]: No parameter help available
			- Frames_Tot: List[int]: No parameter help available
			- Bytes_Curr: List[float]: No parameter help available
			- Bytes_Tot: List[float]: No parameter help available
			- Mbps_Curr: List[float]: No parameter help available
			- Mbps_Tot: List[float]: No parameter help available
			- Power_Curr: List[float]: No parameter help available
			- Power_Tot: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Rate', DataType.EnumList, enums.DataRate, False, True, 1),
			ArgStruct('Ru_Size', DataType.EnumList, enums.RuSize, False, True, 1),
			ArgStruct('Nss', DataType.EnumList, enums.SpacialStreamsNr, False, True, 1),
			ArgStruct('Frames_Curr', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Frames_Tot', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Bytes_Curr', DataType.FloatList, None, False, True, 1),
			ArgStruct('Bytes_Tot', DataType.FloatList, None, False, True, 1),
			ArgStruct('Mbps_Curr', DataType.FloatList, None, False, True, 1),
			ArgStruct('Mbps_Tot', DataType.FloatList, None, False, True, 1),
			ArgStruct('Power_Curr', DataType.FloatList, None, False, True, 1),
			ArgStruct('Power_Tot', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rate: List[enums.DataRate] = None
			self.Ru_Size: List[enums.RuSize] = None
			self.Nss: List[enums.SpacialStreamsNr] = None
			self.Frames_Curr: List[int] = None
			self.Frames_Tot: List[int] = None
			self.Bytes_Curr: List[float] = None
			self.Bytes_Tot: List[float] = None
			self.Mbps_Curr: List[float] = None
			self.Mbps_Tot: List[float] = None
			self.Power_Curr: List[float] = None
			self.Power_Tot: List[float] = None

	def get(self, station=repcap.Station.Default) -> GetStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:STA<s>:UESinfo:RXPSdu:HETB \n
		Snippet: value: GetStruct = driver.sense.sta.uesInfo.rxPsdu.hetb.get(station = repcap.Station.Default) \n
		No command help available \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'SENSe:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:UESinfo:RXPSdu:HETB?', self.__class__.GetStruct())
