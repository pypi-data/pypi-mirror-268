from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AddressCls:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)

	def get(self, station=repcap.Station.Default) -> str:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:STA<s>:UECapability:MAC:ADDRess \n
		Snippet: value: str = driver.sense.sta.ueCapability.mac.address.get(station = repcap.Station.Default) \n
		Gets the MAC address of an associated DUT. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: mac_address: string Hexadecimal MAC address as string"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'SENSe:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:UECapability:MAC:ADDRess?')
		return trim_str_response(response)
