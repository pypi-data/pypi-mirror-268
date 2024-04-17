from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpVersionCls:
	"""IpVersion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipVersion", core, parent)

	def set(self, version: enums.IpVersion, packetGenerator=repcap.PacketGenerator.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:IPVersion \n
		Snippet: driver.configure.pgen.ipVersion.set(version = enums.IpVersion.IV4, packetGenerator = repcap.PacketGenerator.Default) \n
		Sets the IP version to be used for generating packets. \n
			:param version: IV4 | IV6
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
		"""
		param = Conversions.enum_scalar_to_str(version, enums.IpVersion)
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:IPVersion {param}')

	# noinspection PyTypeChecker
	def get(self, packetGenerator=repcap.PacketGenerator.Default) -> enums.IpVersion:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:IPVersion \n
		Snippet: value: enums.IpVersion = driver.configure.pgen.ipVersion.get(packetGenerator = repcap.PacketGenerator.Default) \n
		Sets the IP version to be used for generating packets. \n
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
			:return: version: IV4 | IV6"""
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:IPVersion?')
		return Conversions.str_to_scalar_enum(response, enums.IpVersion)
