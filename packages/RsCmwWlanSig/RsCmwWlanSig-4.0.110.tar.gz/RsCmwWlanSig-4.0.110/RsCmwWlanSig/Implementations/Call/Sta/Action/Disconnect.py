from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DisconnectCls:
	"""Disconnect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("disconnect", core, parent)

	def set(self, station=repcap.Station.Default, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALL:WLAN:SIGNaling<Instance>:STA<s>:ACTion:DISConnect \n
		Snippet: driver.call.sta.action.disconnect.set(station = repcap.Station.Default) \n
		Disassociates and deauthenticates the DUT by sending a deauthentication frame. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write_with_opc(f'CALL:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:ACTion:DISConnect', opc_timeout_ms)
