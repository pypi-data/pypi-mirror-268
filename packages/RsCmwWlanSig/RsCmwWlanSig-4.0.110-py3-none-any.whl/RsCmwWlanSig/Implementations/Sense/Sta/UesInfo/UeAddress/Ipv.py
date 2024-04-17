from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvCls:
	"""Ipv commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipv", core, parent)

	def get(self, station=repcap.Station.Default, ipVersion=repcap.IpVersion.Default) -> str:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:STA<s>:UESinfo:UEADdress:IPV<n> \n
		Snippet: value: str = driver.sense.sta.uesInfo.ueAddress.ipv.get(station = repcap.Station.Default, ipVersion = repcap.IpVersion.Default) \n
		Queries the detected IPv4 / IPv6 addresses of the connected DUT. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:param ipVersion: optional repeated capability selector. Default value: V4 (settable in the interface 'UeAddress')
			:return: ip_address: string IPv4 / IPv6 addresses as string"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		response = self._core.io.query_str(f'SENSe:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:UESinfo:UEADdress:IPV{ipVersion_cmd_val}?')
		return trim_str_response(response)
