from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PgStatsCls:
	"""PgStats commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pgStats", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Icmp_Req_Frames: int: No parameter help available
			- Icmp_Req_Bytes: int: No parameter help available
			- Icmp_Resp_Frames: int: No parameter help available
			- Icmp_Resp_Bytes: int: No parameter help available
			- Icmp_Resp_Percent: float: No parameter help available
			- Udp_Sent_Frames: int: No parameter help available
			- Udp_Sent_Bytes: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Icmp_Req_Frames'),
			ArgStruct.scalar_int('Icmp_Req_Bytes'),
			ArgStruct.scalar_int('Icmp_Resp_Frames'),
			ArgStruct.scalar_int('Icmp_Resp_Bytes'),
			ArgStruct.scalar_float('Icmp_Resp_Percent'),
			ArgStruct.scalar_int('Udp_Sent_Frames'),
			ArgStruct.scalar_int('Udp_Sent_Bytes')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Icmp_Req_Frames: int = None
			self.Icmp_Req_Bytes: int = None
			self.Icmp_Resp_Frames: int = None
			self.Icmp_Resp_Bytes: int = None
			self.Icmp_Resp_Percent: float = None
			self.Udp_Sent_Frames: int = None
			self.Udp_Sent_Bytes: int = None

	def get(self, packetGenerator=repcap.PacketGenerator.Default) -> GetStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:PGEN<index>:PGSTats \n
		Snippet: value: GetStruct = driver.sense.pgen.pgStats.get(packetGenerator = repcap.PacketGenerator.Default) \n
		No command help available \n
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		return self._core.io.query_struct(f'SENSe:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:PGSTats?', self.__class__.GetStruct())
