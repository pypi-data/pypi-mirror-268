from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DfdefCls:
	"""Dfdef commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dfdef", core, parent)

	# noinspection PyTypeChecker
	class DfdefStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- State: enums.EnableState: DISable | ENABle Disables/enables the user-defined frame rate control
			- Format_Py: enums.DataFormatExt: NHT | HTM | VHT | HES | HEM Selects the frame format NHT: non-high throughput format (non-HT) HTM: HT mixed format (HT MF) VHT: very high throughput format HES: high efficiency single-user format (HE SU) HEM: high efficiency multi-user format (HE MU)
			- Chan_Bw: enums.ChannelBandwidthDut: BW20 | BW40 | BW80 | BW160 Channel bandwidth The value must not exceed the operating channel bandwidth, see [CMDLINKRESOLVED Configure.RfSettings#OcWidth CMDLINKRESOLVED].
			- Rate: enums.Coderate: D1MBit | D2MBits | C55Mbits | C11Mbits | BR12 | BR34 | QR12 | QR34 | Q1M12 | Q1M34 | Q6M23 | Q6M34 | MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | MCS8 | MCS9 | MCS10 | MCS11 | MCS12 | MCS13 | MCS14 | MCS15 See rate list in [CMDLINKRESOLVED Configure.Connection.MfDef#set CMDLINKRESOLVED]
			- Guard_Interval: enums.GuardInterval: Optional setting parameter. LONG | SHORt | GI08 | GI16 | GI32 SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Ltf_Type: enums.LtfType: Optional setting parameter. X1 | X2 | X4 1x HE-LTF, 2x HE-LTF, 4x HE-LTF for 802.11ax
			- Pe_Duration: enums.PeDuration: Optional setting parameter. PE0 | PE4 | PE8 | PE12 | PE16 | AUTO PEx: additional receive processing time of x μs signaled in packet extension (PE) field (only for 802.11ax) AUTO: automatic setting based on the reported DUTs capabilities
			- Ctype: enums.CodingType: Optional setting parameter. LDPC | BCC Coding type (for 802.11ax - VHT, HE_SU, HE_MU frames only) : low density parity check or binary convolution code
			- Streams: enums.Streams: Optional setting parameter. STR1 | STR2 Number of streams
			- Stbc: bool: Optional setting parameter. OFF | ON Enables / disables space time block coding (STBC) . If disabled, spatial multiplexing is used."""
		__meta_args_list = [
			ArgStruct.scalar_enum('State', enums.EnableState),
			ArgStruct.scalar_enum('Format_Py', enums.DataFormatExt),
			ArgStruct.scalar_enum('Chan_Bw', enums.ChannelBandwidthDut),
			ArgStruct.scalar_enum('Rate', enums.Coderate),
			ArgStruct.scalar_enum_optional('Guard_Interval', enums.GuardInterval),
			ArgStruct.scalar_enum_optional('Ltf_Type', enums.LtfType),
			ArgStruct.scalar_enum_optional('Pe_Duration', enums.PeDuration),
			ArgStruct.scalar_enum_optional('Ctype', enums.CodingType),
			ArgStruct.scalar_enum_optional('Streams', enums.Streams),
			ArgStruct.scalar_bool_optional('Stbc')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: enums.EnableState = None
			self.Format_Py: enums.DataFormatExt = None
			self.Chan_Bw: enums.ChannelBandwidthDut = None
			self.Rate: enums.Coderate = None
			self.Guard_Interval: enums.GuardInterval = None
			self.Ltf_Type: enums.LtfType = None
			self.Pe_Duration: enums.PeDuration = None
			self.Ctype: enums.CodingType = None
			self.Streams: enums.Streams = None
			self.Stbc: bool = None

	def set(self, structure: DfdefStruct, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:DFDef \n
		Snippet with structure: \n
		structure = driver.configure.sta.connection.dfdef.DfdefStruct() \n
		structure.State: enums.EnableState = enums.EnableState.DISable \n
		structure.Format_Py: enums.DataFormatExt = enums.DataFormatExt.HEES \n
		structure.Chan_Bw: enums.ChannelBandwidthDut = enums.ChannelBandwidthDut.BW160 \n
		structure.Rate: enums.Coderate = enums.Coderate.BR12 \n
		structure.Guard_Interval: enums.GuardInterval = enums.GuardInterval.GI08 \n
		structure.Ltf_Type: enums.LtfType = enums.LtfType.X1 \n
		structure.Pe_Duration: enums.PeDuration = enums.PeDuration.AUTO \n
		structure.Ctype: enums.CodingType = enums.CodingType.BCC \n
		structure.Streams: enums.Streams = enums.Streams.STR1 \n
		structure.Stbc: bool = False \n
		driver.configure.sta.connection.dfdef.set(structure, station = repcap.Station.Default) \n
		Enables and configures the user-defined frame rate control for data frames. \n
			:param structure: for set value, see the help for DfdefStruct structure arguments.
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write_struct(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:DFDef', structure)

	def get(self, station=repcap.Station.Default) -> DfdefStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:DFDef \n
		Snippet: value: DfdefStruct = driver.configure.sta.connection.dfdef.get(station = repcap.Station.Default) \n
		Enables and configures the user-defined frame rate control for data frames. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for DfdefStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:DFDef?', self.__class__.DfdefStruct())
