from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PerCls:
	"""Per commands group definition. 17 total commands, 2 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("per", core, parent)

	@property
	def dframe(self):
		"""dframe commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dframe'):
			from .Dframe import DframeCls
			self._dframe = DframeCls(self._core, self._cmd_group)
		return self._dframe

	@property
	def payload(self):
		"""payload commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import PayloadCls
			self._payload = PayloadCls(self._core, self._cmd_group)
		return self._payload

	# noinspection PyTypeChecker
	class FdefStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Format_Py: enums.DataFormatExt: NHT | HTM | VHT | HES | HEM Selects the frame format NHT: non-high throughput format (non-HT) HTM: HT mixed format (HT MF) VHT: very high throughput format HES: high efficiency single-user format (HE SU) HEM: high efficiency multi-user format (HE MU)
			- Bandwidth: enums.ChannelBandwidthDut: BW20 | BW40 | BW80 | BW160 Channel bandwidth The value must not exceed the operating channel bandwidth, see [CMDLINKRESOLVED Configure.RfSettings#OcWidth CMDLINKRESOLVED].
			- Coderate: enums.Coderate: BR12 | QR12 | QR34 | Q1M12 | Q1M34 | Q6M23 | Q6M34 | BR34 | MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | D1MBit | D2MBits | C55Mbits | C11Mbits | MCS8 | MCS9 | MCS10 | MCS11 | MCS12 | MCS13 | MCS14 | MCS15 See rate list in [CMDLINKRESOLVED Configure.Connection.MfDef#set CMDLINKRESOLVED]
			- Guard_Interval: enums.GuardInterval: Optional setting parameter. LONG | SHORt | GI08 | GI16 | GI32 SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Ltf_Type: enums.LtfType: Optional setting parameter. X1 | X2 | X4 1x HE-LTF, 2x HE-LTF, 4x HE-LTF for 802.11ax
			- Pe_Duration: enums.PeDuration: Optional setting parameter. PE0 | PE4 | PE8 | PE12 | PE16 | AUTO PEx: additional receive processing time of x μs signaled in packet extension (PE) field (only for 802.11ax) AUTO: automatic setting based on the reported DUTs capabilities
			- Ctype: enums.CodingType: Optional setting parameter. LDPC | BCC Coding type (for 802.11ax - VHT, HE_SU, HE_MU frames only) : low density parity check or binary convolution code
			- Streams: enums.Streams: Optional setting parameter. STR1 | STR2 Number of streams
			- Stbc: bool: Optional setting parameter. OFF | ON Enables / disables space time block coding (STBC) . If disabled, spatial multiplexing is used."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Format_Py', enums.DataFormatExt),
			ArgStruct.scalar_enum('Bandwidth', enums.ChannelBandwidthDut),
			ArgStruct.scalar_enum('Coderate', enums.Coderate),
			ArgStruct.scalar_enum_optional('Guard_Interval', enums.GuardInterval),
			ArgStruct.scalar_enum_optional('Ltf_Type', enums.LtfType),
			ArgStruct.scalar_enum_optional('Pe_Duration', enums.PeDuration),
			ArgStruct.scalar_enum_optional('Ctype', enums.CodingType),
			ArgStruct.scalar_enum_optional('Streams', enums.Streams),
			ArgStruct.scalar_bool_optional('Stbc')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Format_Py: enums.DataFormatExt = None
			self.Bandwidth: enums.ChannelBandwidthDut = None
			self.Coderate: enums.Coderate = None
			self.Guard_Interval: enums.GuardInterval = None
			self.Ltf_Type: enums.LtfType = None
			self.Pe_Duration: enums.PeDuration = None
			self.Ctype: enums.CodingType = None
			self.Streams: enums.Streams = None
			self.Stbc: bool = None

	def get_fdef(self) -> FdefStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:FDEF \n
		Snippet: value: FdefStruct = driver.configure.per.get_fdef() \n
		Configures the downlink data frames for PER measurements. \n
			:return: structure: for return value, see the help for FdefStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:SIGNaling<Instance>:PER:FDEF?', self.__class__.FdefStruct())

	def set_fdef(self, value: FdefStruct) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:FDEF \n
		Snippet with structure: \n
		structure = driver.configure.per.FdefStruct() \n
		structure.Format_Py: enums.DataFormatExt = enums.DataFormatExt.HEES \n
		structure.Bandwidth: enums.ChannelBandwidthDut = enums.ChannelBandwidthDut.BW160 \n
		structure.Coderate: enums.Coderate = enums.Coderate.BR12 \n
		structure.Guard_Interval: enums.GuardInterval = enums.GuardInterval.GI08 \n
		structure.Ltf_Type: enums.LtfType = enums.LtfType.X1 \n
		structure.Pe_Duration: enums.PeDuration = enums.PeDuration.AUTO \n
		structure.Ctype: enums.CodingType = enums.CodingType.BCC \n
		structure.Streams: enums.Streams = enums.Streams.STR1 \n
		structure.Stbc: bool = False \n
		driver.configure.per.set_fdef(value = structure) \n
		Configures the downlink data frames for PER measurements. \n
			:param value: see the help for FdefStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:SIGNaling<Instance>:PER:FDEF', value)

	# noinspection PyTypeChecker
	def get_dpattern(self) -> enums.Pattern:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DPATtern \n
		Snippet: value: enums.Pattern = driver.configure.per.get_dpattern() \n
		Selects the data that the R&S CMW transfers to the DUT. \n
			:return: pattern: PN1 | PN2 | PN3 | PN4 | PN5 | PN6 | PN7 | PN8 | PN9 | PN10 | PN11 | PN12 | PN13 | PN14 | PN15 | PN16 | PN17 | PN18 | PN19 | PN20 | PN21 | PN22 | PN23 | PN24 | PN25 | PN26 | PN27 | PN28 | PN29 | PN30 | PN31 | PN32 | PRANdom | AZERo | AONE | PT01 | PT10 PN1,...,PN32: pseudo-noise bit sequences of different lengths PRANdom: random bit sequence AZERo: all zero pattern '000...' AONE: all one pattern '111...' PT01: alternating sequence starting with zero '010101...' PT10: alternating sequence starting with one '101010...'
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:PER:DPATtern?')
		return Conversions.str_to_scalar_enum(response, enums.Pattern)

	def set_dpattern(self, pattern: enums.Pattern) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DPATtern \n
		Snippet: driver.configure.per.set_dpattern(pattern = enums.Pattern.AONE) \n
		Selects the data that the R&S CMW transfers to the DUT. \n
			:param pattern: PN1 | PN2 | PN3 | PN4 | PN5 | PN6 | PN7 | PN8 | PN9 | PN10 | PN11 | PN12 | PN13 | PN14 | PN15 | PN16 | PN17 | PN18 | PN19 | PN20 | PN21 | PN22 | PN23 | PN24 | PN25 | PN26 | PN27 | PN28 | PN29 | PN30 | PN31 | PN32 | PRANdom | AZERo | AONE | PT01 | PT10 PN1,...,PN32: pseudo-noise bit sequences of different lengths PRANdom: random bit sequence AZERo: all zero pattern '000...' AONE: all one pattern '111...' PT01: alternating sequence starting with zero '010101...' PT10: alternating sequence starting with one '101010...'
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.Pattern)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DPATtern {param}')

	def get_dinterval(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DINTerval \n
		Snippet: value: int = driver.configure.per.get_dinterval() \n
		Specifies the time interval (in units of 1024 µs) between data packet transmissions for the PER measurement. \n
			:return: interval: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:PER:DINTerval?')
		return Conversions.str_to_int(response)

	def set_dinterval(self, interval: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DINTerval \n
		Snippet: driver.configure.per.set_dinterval(interval = 1) \n
		Specifies the time interval (in units of 1024 µs) between data packet transmissions for the PER measurement. \n
			:param interval: integer Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DINTerval {param}')

	# noinspection PyTypeChecker
	def get_tidentifier(self) -> enums.Tid:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:TIDentifier \n
		Snippet: value: enums.Tid = driver.configure.per.get_tidentifier() \n
		Sets the TID value to be used for PER measurements. \n
			:return: tid: TID0 | TID1 | TID2 | TID3 | TID4 | TID5 | TID6 | TID7
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:PER:TIDentifier?')
		return Conversions.str_to_scalar_enum(response, enums.Tid)

	def set_tidentifier(self, tid: enums.Tid) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:TIDentifier \n
		Snippet: driver.configure.per.set_tidentifier(tid = enums.Tid.TID0) \n
		Sets the TID value to be used for PER measurements. \n
			:param tid: TID0 | TID1 | TID2 | TID3 | TID4 | TID5 | TID6 | TID7
		"""
		param = Conversions.enum_scalar_to_str(tid, enums.Tid)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:TIDentifier {param}')

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.Station:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DESTination \n
		Snippet: value: enums.Station = driver.configure.per.get_destination() \n
		Specify the station for which the traffic is measured. This parameter is visible, if 'Multi STA' is enabled. \n
			:return: sta: STA1 | STA2 | STA3
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:PER:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.Station)

	def set_destination(self, sta: enums.Station) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DESTination \n
		Snippet: driver.configure.per.set_destination(sta = enums.Station.STA1) \n
		Specify the station for which the traffic is measured. This parameter is visible, if 'Multi STA' is enabled. \n
			:param sta: STA1 | STA2 | STA3
		"""
		param = Conversions.enum_scalar_to_str(sta, enums.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DESTination {param}')

	def get_packets(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:PACKets \n
		Snippet: value: int = driver.configure.per.get_packets() \n
		Sets the number of user data MAC packets to be transmitted to the DUT. \n
			:return: number_of_packets: numeric Range: 1 to 1E+6
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:PER:PACKets?')
		return Conversions.str_to_int(response)

	def set_packets(self, number_of_packets: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:PACKets \n
		Snippet: driver.configure.per.set_packets(number_of_packets = 1) \n
		Sets the number of user data MAC packets to be transmitted to the DUT. \n
			:param number_of_packets: numeric Range: 1 to 1E+6
		"""
		param = Conversions.decimal_value_to_str(number_of_packets)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:PACKets {param}')

	# noinspection PyTypeChecker
	def get_atype(self) -> enums.AckType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:ATYPe \n
		Snippet: value: enums.AckType = driver.configure.per.get_atype() \n
		Selects an evaluation scheme for the PER measurement. Currently, only the standard frame acknowledgment is available. \n
			:return: ack_type: ACK
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:PER:ATYPe?')
		return Conversions.str_to_scalar_enum(response, enums.AckType)

	def set_atype(self, ack_type: enums.AckType) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:ATYPe \n
		Snippet: driver.configure.per.set_atype(ack_type = enums.AckType.ACK) \n
		Selects an evaluation scheme for the PER measurement. Currently, only the standard frame acknowledgment is available. \n
			:param ack_type: ACK
		"""
		param = Conversions.enum_scalar_to_str(ack_type, enums.AckType)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:ATYPe {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.per.get_repetition() \n
		No command help available \n
			:return: repetition: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:PER:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:REPetition \n
		Snippet: driver.configure.per.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		No command help available \n
			:param repetition: No help available
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:REPetition {param}')

	def clone(self) -> 'PerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
