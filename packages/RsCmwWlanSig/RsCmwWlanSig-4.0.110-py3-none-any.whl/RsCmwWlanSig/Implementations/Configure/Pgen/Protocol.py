from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProtocolCls:
	"""Protocol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("protocol", core, parent)

	def set(self, type_py: enums.ProtocolType, packetGenerator=repcap.PacketGenerator.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:PROTocol \n
		Snippet: driver.configure.pgen.protocol.set(type_py = enums.ProtocolType.ICMP, packetGenerator = repcap.PacketGenerator.Default) \n
		Sets the protocol of the packet generator. \n
			:param type_py: ICMP | UDP
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ProtocolType)
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:PROTocol {param}')

	# noinspection PyTypeChecker
	def get(self, packetGenerator=repcap.PacketGenerator.Default) -> enums.ProtocolType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:PROTocol \n
		Snippet: value: enums.ProtocolType = driver.configure.pgen.protocol.get(packetGenerator = repcap.PacketGenerator.Default) \n
		Sets the protocol of the packet generator. \n
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
			:return: type_py: ICMP | UDP"""
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.ProtocolType)
