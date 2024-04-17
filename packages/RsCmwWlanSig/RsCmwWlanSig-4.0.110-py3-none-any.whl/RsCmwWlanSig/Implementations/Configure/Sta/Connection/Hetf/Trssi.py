from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrssiCls:
	"""Trssi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trssi", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Int_Value: int: decimal Target_RSSI index 0 to 90: map to -110 dBm to -20 dBm 91-126: reserved 127: station is commanded to transmit at maximum power for the assigned MCS Range: 0 to 127
			- Dbm_Value: int: decimal Target_RSSI value Range: -110 dBm to -20 dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Int_Value'),
			ArgStruct.scalar_int('Dbm_Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Int_Value: int = None
			self.Dbm_Value: int = None

	def get(self, station=repcap.Station.Default) -> GetStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:TRSSi \n
		Snippet: value: GetStruct = driver.configure.sta.connection.hetf.trssi.get(station = repcap.Station.Default) \n
		Specifies the expected Rx power of HE TB PPDU transmission as a response to trigger frame. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:TRSSi?', self.__class__.GetStruct())
