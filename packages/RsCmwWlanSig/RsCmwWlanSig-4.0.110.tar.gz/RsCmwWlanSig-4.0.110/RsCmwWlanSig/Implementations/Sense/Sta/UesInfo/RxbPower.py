from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxbPowerCls:
	"""RxbPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rxbPower", core, parent)

	def get(self, station=repcap.Station.Default) -> float:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:STA<s>:UESinfo:RXBPower \n
		Snippet: value: float = driver.sense.sta.uesInfo.rxbPower.get(station = repcap.Station.Default) \n
		Queries the average power of the last burst received from the DUT. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: power: float Unit: dBm"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'SENSe:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:UESinfo:RXBPower?')
		return Conversions.str_to_float(response)
