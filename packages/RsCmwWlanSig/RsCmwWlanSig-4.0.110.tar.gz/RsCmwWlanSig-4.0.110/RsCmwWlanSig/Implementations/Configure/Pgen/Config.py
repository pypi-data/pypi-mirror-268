from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigCls:
	"""Config commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	def set(self, state: bool, interval: int, payload_size: int, payload_type: enums.PayloadType, tid: enums.Tid = None, packetGenerator=repcap.PacketGenerator.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:CONFig \n
		Snippet: driver.configure.pgen.config.set(state = False, interval = 1, payload_size = 1, payload_type = enums.PayloadType.AONes, tid = enums.Tid.TID0, packetGenerator = repcap.PacketGenerator.Default) \n
		Configures the packet generator. \n
			:param state: OFF | ON Disables/enables the packet generator
			:param interval: integer Time interval between packet transmissions in units of 1024 μs Range: 0 to 10E+3
			:param payload_size: integer Payload size of generated packets in bytes Range: 0 to 1472
			:param payload_type: DEFault | AZERoes | AONes | BP01 | BP10 | PRANdom Bit sequence to be transmitted as payload DEFault: an implementation-specific default pattern AZERoes: all zeroes AONes: all ones BP01: bit pattern 010101... BP10: bit pattern 101010... PRANdom: a pseudo-random bit sequence
			:param tid: TID0 | TID1 | TID2 | TID3 | TID4 | TID5 | TID6 | TID7 TID signaled by the packet generator
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('interval', interval, DataType.Integer), ArgSingle('payload_size', payload_size, DataType.Integer), ArgSingle('payload_type', payload_type, DataType.Enum, enums.PayloadType), ArgSingle('tid', tid, DataType.Enum, enums.Tid, is_optional=True))
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:CONFig {param}'.rstrip())

	# noinspection PyTypeChecker
	class ConfigStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: OFF | ON Disables/enables the packet generator
			- Interval: int: integer Time interval between packet transmissions in units of 1024 μs Range: 0 to 10E+3
			- Payload_Size: int: integer Payload size of generated packets in bytes Range: 0 to 1472
			- Payload_Type: enums.PayloadType: DEFault | AZERoes | AONes | BP01 | BP10 | PRANdom Bit sequence to be transmitted as payload DEFault: an implementation-specific default pattern AZERoes: all zeroes AONes: all ones BP01: bit pattern 010101... BP10: bit pattern 101010... PRANdom: a pseudo-random bit sequence
			- Tid: enums.Tid: TID0 | TID1 | TID2 | TID3 | TID4 | TID5 | TID6 | TID7 TID signaled by the packet generator"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_int('Interval'),
			ArgStruct.scalar_int('Payload_Size'),
			ArgStruct.scalar_enum('Payload_Type', enums.PayloadType),
			ArgStruct.scalar_enum('Tid', enums.Tid)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Interval: int = None
			self.Payload_Size: int = None
			self.Payload_Type: enums.PayloadType = None
			self.Tid: enums.Tid = None

	def get(self, packetGenerator=repcap.PacketGenerator.Default) -> ConfigStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:CONFig \n
		Snippet: value: ConfigStruct = driver.configure.pgen.config.get(packetGenerator = repcap.PacketGenerator.Default) \n
		Configures the packet generator. \n
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
			:return: structure: for return value, see the help for ConfigStruct structure arguments."""
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:CONFig?', self.__class__.ConfigStruct())
