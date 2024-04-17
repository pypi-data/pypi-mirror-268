from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ArxbPowerCls:
	"""ArxbPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("arxbPower", core, parent)

	def get(self, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:UESinfo[:ANTenna<n>]:ARXBpower \n
		Snippet: value: float = driver.sense.uesInfo.antenna.arxbPower.get(antenna = repcap.Antenna.Default) \n
		Queries the approximate RX burst power per individual antenna, calculated from the expected PEP and the configured
		standard. Antenna 2 is only available in a MIMO scenario. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: approx_power: float Unit: dBm"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'SENSe:WLAN:SIGNaling<Instance>:UESinfo:ANTenna{antenna_cmd_val}:ARXBpower?')
		return Conversions.str_to_float(response)
