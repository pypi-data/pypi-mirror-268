from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsReportCls:
	"""AbsReport commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absReport", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Total: int: decimal Maximum of all reports received in preceding interval Range: 0 KB to 4.145152E+6 KB, Unit: kB
			- Buffered_Data_Tid: int: decimal Maximum of all QoS control reports Range: 0 KB to 4.145152E+6 KB, Unit: kB
			- Tidx: enums.Tid: TID0 | TID1 | TID2 | TID3 | TID4 | TID5 | TID6 | TID7 Indication of TID, for which the buffer status BufferedData_TID is reported
			- Buffered_Data_Ac: int: decimal Maximum AC-specific queue size of all AC control reports Range: 0 KB to 4.145152E+6 KB, Unit: kB
			- Acx: enums.AccessCategory: ACBE | ACBK | ACVI | ACVO Indication of access category (ACI bitmap subfield) for which the buffer status BufferedData_AC is reported ACBE: AC_BE (best effort) ACBK: AC_BK (background) ACVI: AC_VI (video) ACVO: AC_VO (voice)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Total'),
			ArgStruct.scalar_int('Buffered_Data_Tid'),
			ArgStruct.scalar_enum('Tidx', enums.Tid),
			ArgStruct.scalar_int('Buffered_Data_Ac'),
			ArgStruct.scalar_enum('Acx', enums.AccessCategory)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Total: int = None
			self.Buffered_Data_Tid: int = None
			self.Tidx: enums.Tid = None
			self.Buffered_Data_Ac: int = None
			self.Acx: enums.AccessCategory = None

	def get(self, station=repcap.Station.Default) -> GetStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:STA<s>:UESinfo:ABSReport \n
		Snippet: value: GetStruct = driver.sense.sta.uesInfo.absReport.get(station = repcap.Station.Default) \n
		Indicates reported buffered data for a UE supporting a HE buffer status report (BSR) control field. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'SENSe:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:UESinfo:ABSReport?', self.__class__.GetStruct())
