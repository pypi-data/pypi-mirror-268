from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UportsCls:
	"""Uports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uports", core, parent)

	def set(self, source_port: int, destination_port: int, packetGenerator=repcap.PacketGenerator.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:UPORts \n
		Snippet: driver.configure.pgen.uports.set(source_port = 1, destination_port = 1, packetGenerator = repcap.PacketGenerator.Default) \n
		Sets the source and destination ports for the UDP protocol. \n
			:param source_port: integer Range: 0 to 65535
			:param destination_port: integer Range: 0 to 65535
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_port', source_port, DataType.Integer), ArgSingle('destination_port', destination_port, DataType.Integer))
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:UPORts {param}'.rstrip())

	# noinspection PyTypeChecker
	class UportsStruct(StructBase):
		"""Response structure. Fields: \n
			- Source_Port: int: integer Range: 0 to 65535
			- Destination_Port: int: integer Range: 0 to 65535"""
		__meta_args_list = [
			ArgStruct.scalar_int('Source_Port'),
			ArgStruct.scalar_int('Destination_Port')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Source_Port: int = None
			self.Destination_Port: int = None

	def get(self, packetGenerator=repcap.PacketGenerator.Default) -> UportsStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:UPORts \n
		Snippet: value: UportsStruct = driver.configure.pgen.uports.get(packetGenerator = repcap.PacketGenerator.Default) \n
		Sets the source and destination ports for the UDP protocol. \n
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
			:return: structure: for return value, see the help for UportsStruct structure arguments."""
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:UPORts?', self.__class__.UportsStruct())
