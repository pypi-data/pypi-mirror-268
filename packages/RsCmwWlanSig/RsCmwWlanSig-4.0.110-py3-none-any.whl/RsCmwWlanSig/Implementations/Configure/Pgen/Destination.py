from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DestinationCls:
	"""Destination commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("destination", core, parent)

	def set(self, station: enums.Station, packetGenerator=repcap.PacketGenerator.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:DESTination \n
		Snippet: driver.configure.pgen.destination.set(station = enums.Station.STA1, packetGenerator = repcap.PacketGenerator.Default) \n
		Specifies the STA to which the packets are addressed to. This parameter is visible, if 'Multi STA' is enabled. \n
			:param station: STA1 | STA2 | STA3
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
		"""
		param = Conversions.enum_scalar_to_str(station, enums.Station)
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:DESTination {param}')

	# noinspection PyTypeChecker
	def get(self, packetGenerator=repcap.PacketGenerator.Default) -> enums.Station:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PGEN<index>:DESTination \n
		Snippet: value: enums.Station = driver.configure.pgen.destination.get(packetGenerator = repcap.PacketGenerator.Default) \n
		Specifies the STA to which the packets are addressed to. This parameter is visible, if 'Multi STA' is enabled. \n
			:param packetGenerator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pgen')
			:return: station: STA1 | STA2 | STA3"""
		packetGenerator_cmd_val = self._cmd_group.get_repcap_cmd_value(packetGenerator, repcap.PacketGenerator)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:PGEN{packetGenerator_cmd_val}:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.Station)
