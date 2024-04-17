from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MfDefCls:
	"""MfDef commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mfDef", core, parent)

	def set(self, state: enums.EnableState, format_py: enums.DataFormatExt, rate: enums.Coderate) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:MFDef \n
		Snippet: driver.configure.connection.mfDef.set(state = enums.EnableState.DISable, format_py = enums.DataFormatExt.HEES, rate = enums.Coderate.BR12) \n
		Enables and configures the user-defined frame rate control for management frames. \n
			:param state: DISable | ENABle Disables/enables the user-defined frame rate control
			:param format_py: NHT | HTM | VHT | HES | HEM Selects the frame format NHT: non-high throughput format (non-HT) HTM: HT mixed format (HT MF) VHT: very high throughput format HES: high efficiency single-user format (HE SU) HEM: high efficiency multi-user format (HE MU)
			:param rate: D1MBit | D2MBits | C55Mbits | C11Mbits | BR12 | BR34 | QR12 | QR34 | Q1M12 | Q1M34 | Q6M23 | Q6M34 | MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | MCS8 | MCS9 | MCS10 | MCS11 | MCS12 | MCS13 | MCS14 | MCS15 Sets the rate D1MBit: DSSS, 1 Mbit/s D2MBits: DSSS, 2 Mbit/s C55Mbits: CCK, 5.5 Mbit/s C11Mbits: CCK, 11 Mbit/s BR12: BPSK, 1/2, 6 Mbit/s BR34: BPSK, 3/4, 9 Mbit/s QR12: QPSK, 1/2, 12 Mbit/s QR34: QPSK, 3/4, 18 Mbit/s Q1M12: 16-QAM, 1/2, 24 Mbit/s Q1M34: 16-QAM, 3/4, 36 Mbit/s Q6M23: 64-QAM, 2/3, 48 Mbit/s Q6M34: 64-QAM, 3/4, 54 Mbit/s MCS, MCS1,...,MCS15: MCS 0 to MCS 15
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Enum, enums.EnableState), ArgSingle('format_py', format_py, DataType.Enum, enums.DataFormatExt), ArgSingle('rate', rate, DataType.Enum, enums.Coderate))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:MFDef {param}'.rstrip())

	# noinspection PyTypeChecker
	class MfDefStruct(StructBase):
		"""Response structure. Fields: \n
			- State: enums.EnableState: DISable | ENABle Disables/enables the user-defined frame rate control
			- Format_Py: enums.DataFormatExt: NHT | HTM | VHT | HES | HEM Selects the frame format NHT: non-high throughput format (non-HT) HTM: HT mixed format (HT MF) VHT: very high throughput format HES: high efficiency single-user format (HE SU) HEM: high efficiency multi-user format (HE MU)
			- Rate: enums.Coderate: D1MBit | D2MBits | C55Mbits | C11Mbits | BR12 | BR34 | QR12 | QR34 | Q1M12 | Q1M34 | Q6M23 | Q6M34 | MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | MCS8 | MCS9 | MCS10 | MCS11 | MCS12 | MCS13 | MCS14 | MCS15 Sets the rate D1MBit: DSSS, 1 Mbit/s D2MBits: DSSS, 2 Mbit/s C55Mbits: CCK, 5.5 Mbit/s C11Mbits: CCK, 11 Mbit/s BR12: BPSK, 1/2, 6 Mbit/s BR34: BPSK, 3/4, 9 Mbit/s QR12: QPSK, 1/2, 12 Mbit/s QR34: QPSK, 3/4, 18 Mbit/s Q1M12: 16-QAM, 1/2, 24 Mbit/s Q1M34: 16-QAM, 3/4, 36 Mbit/s Q6M23: 64-QAM, 2/3, 48 Mbit/s Q6M34: 64-QAM, 3/4, 54 Mbit/s MCS, MCS1,...,MCS15: MCS 0 to MCS 15"""
		__meta_args_list = [
			ArgStruct.scalar_enum('State', enums.EnableState),
			ArgStruct.scalar_enum('Format_Py', enums.DataFormatExt),
			ArgStruct.scalar_enum('Rate', enums.Coderate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: enums.EnableState = None
			self.Format_Py: enums.DataFormatExt = None
			self.Rate: enums.Coderate = None

	def get(self) -> MfDefStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:MFDef \n
		Snippet: value: MfDefStruct = driver.configure.connection.mfDef.get() \n
		Enables and configures the user-defined frame rate control for management frames. \n
			:return: structure: for return value, see the help for MfDefStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:MFDef?', self.__class__.MfDefStruct())
