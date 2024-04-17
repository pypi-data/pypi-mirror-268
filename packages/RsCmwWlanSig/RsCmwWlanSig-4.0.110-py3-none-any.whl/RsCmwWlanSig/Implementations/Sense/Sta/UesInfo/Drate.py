from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DrateCls:
	"""Drate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("drate", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Format_Py: enums.FrameFormat: NHT | HT | VHT | HESU | HEMU | HETB Frame format NHT: non-high throughput format (non-HT) HT: high throughput format VHT: very high throughput format HESU: high efficiency format, single user MIMO HEMU: high efficiency format, multi user MIMO HETB: high efficiency format, trigger based uplink single user MIMO
			- Rate: enums.DataRate: MB1 | MB2 | MB5 | MB6 | MB9 | MB11 | MB12 | MB18 | MB24 | MB36 | MB48 | MB54 | MCS0 | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | MCS8 | MCS9 | MCS10 | MCS11 | MCS12 | MCS13 | MCS14 | MCS15 MBx: data rate for NHT in Mbit/s {1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36, 48, 54} MCSx: modulation and coding scheme x for HT, VHT and HE
			- Cbw: enums.ChannelBandwidth: BW20 | BW40 | BW80 | BW88 | BW16 Channel bandwidth in MHz: 20, 40, 80, 80+80, 160
			- Nss: enums.SpacialStreamsNr: NSS1 | NSS2 | NSS3 | NSS4 | NSS5 | NSS6 | NSS7 | NSS8 Number of spatial streams"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Format_Py', enums.FrameFormat),
			ArgStruct.scalar_enum('Rate', enums.DataRate),
			ArgStruct.scalar_enum('Cbw', enums.ChannelBandwidth),
			ArgStruct.scalar_enum('Nss', enums.SpacialStreamsNr)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Format_Py: enums.FrameFormat = None
			self.Rate: enums.DataRate = None
			self.Cbw: enums.ChannelBandwidth = None
			self.Nss: enums.SpacialStreamsNr = None

	def get(self, station=repcap.Station.Default) -> GetStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:STA<s>:UESinfo:DRATe \n
		Snippet: value: GetStruct = driver.sense.sta.uesInfo.drate.get(station = repcap.Station.Default) \n
		Queries information related to the data rate of the DUT signal. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'SENSe:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:UESinfo:DRATe?', self.__class__.GetStruct())
