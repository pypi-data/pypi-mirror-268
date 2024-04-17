from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UphInfoCls:
	"""UphInfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uphInfo", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Burst_Power: float: float Indication of HE TB burst power. Range: -999 dBm to 999 dBm
			- Uph: int: decimal Indication of UL power headroom. Range: 0 dB to 31 dB
			- Min_Tx_Power_Flag: bool: OFF | ON Indication whether the HE TB bursts are sent at the minimum transmit power of the station."""
		__meta_args_list = [
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_int('Uph'),
			ArgStruct.scalar_bool('Min_Tx_Power_Flag')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Burst_Power: float = None
			self.Uph: int = None
			self.Min_Tx_Power_Flag: bool = None

	def get(self, station=repcap.Station.Default) -> GetStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:STA<s>:HETBinfo:UPHinfo \n
		Snippet: value: GetStruct = driver.sense.sta.hetbInfo.uphInfo.get(station = repcap.Station.Default) \n
		Queries actual information related to uplink power headroom (UPH) control. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'SENSe:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:HETBinfo:UPHinfo?', self.__class__.GetStruct())
