from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OfmLengthCls:
	"""OfmLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ofmLength", core, parent)

	def set(self, mode: enums.LenMode, length: int = None) -> None:
		"""SCPI: TRIGger:WLAN:SIGNaling<instance>:RX:MACFrame:OFMLength \n
		Snippet: driver.trigger.rx.macFrame.ofmLength.set(mode = enums.LenMode.DEFault, length = 1) \n
		Defines the minimum length for the all OFDM RX frame trigger modes (all modes except All Bursts and DSSS/CCK Bursts) ,
		see method RsCmwWlanSig.Trigger.Rx.MacFrame.btype. \n
			:param mode: DEFault | UDEFined DEFault: automatically calculated value UDEFined: configured Length
			:param length: numeric Range: 1 to 1500
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('mode', mode, DataType.Enum, enums.LenMode), ArgSingle('length', length, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'TRIGger:WLAN:SIGNaling<Instance>:RX:MACFrame:OFMLength {param}'.rstrip())

	# noinspection PyTypeChecker
	class OfmLengthStruct(StructBase):
		"""Response structure. Fields: \n
			- Mode: enums.LenMode: DEFault | UDEFined DEFault: automatically calculated value UDEFined: configured Length
			- Length: int: numeric Range: 1 to 1500"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mode', enums.LenMode),
			ArgStruct.scalar_int('Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mode: enums.LenMode = None
			self.Length: int = None

	def get(self) -> OfmLengthStruct:
		"""SCPI: TRIGger:WLAN:SIGNaling<instance>:RX:MACFrame:OFMLength \n
		Snippet: value: OfmLengthStruct = driver.trigger.rx.macFrame.ofmLength.get() \n
		Defines the minimum length for the all OFDM RX frame trigger modes (all modes except All Bursts and DSSS/CCK Bursts) ,
		see method RsCmwWlanSig.Trigger.Rx.MacFrame.btype. \n
			:return: structure: for return value, see the help for OfmLengthStruct structure arguments."""
		return self._core.io.query_struct(f'TRIGger:WLAN:SIGNaling<Instance>:RX:MACFrame:OFMLength?', self.__class__.OfmLengthStruct())
