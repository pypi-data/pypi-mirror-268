from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UphInfoCls:
	"""UphInfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uphInfo", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Burst_Power: List[float]: float Measured burst power in uplink Range: -999 dBm to 999 dBm, Unit: dBm
			- Uph: List[int]: decimal UL power headroom Range: 0 dB to 31 dB, Unit: dB
			- Min_Tx_Power_Flag: List[bool]: OFF | ON Indication whether the HE TB bursts are sent at the minimum transmit power of the station
			- Lst: List[float]: float Rx timestamp from physical layer"""
		__meta_args_list = [
			ArgStruct('Burst_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Uph', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Min_Tx_Power_Flag', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Lst', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Burst_Power: List[float] = None
			self.Uph: List[int] = None
			self.Min_Tx_Power_Flag: List[bool] = None
			self.Lst: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:WLAN:SIGNaling<instance>:HETBased:UPHinfo \n
		Snippet: value: FetchStruct = driver.hetBased.uphInfo.fetch() \n
		Queries the results of the signaling HE TB list mode measurements on UL power headroom (UPH) . The result groups are
		listed in a sequence as {<BurstPower>, <UPH>, <MinTXPowerFlag>, <LST>}frame_1, ..., {<BurstPower>, <UPH>,
		<MinTXPowerFlag>, <LST>}frame_n. The number of results n is set via method RsCmwWlanSig.Configure.HetBased.frames \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:SIGNaling<Instance>:HETBased:UPHinfo?', self.__class__.FetchStruct())
