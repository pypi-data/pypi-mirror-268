from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReconnectCls:
	"""Reconnect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reconnect", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALL:WLAN:SIGNaling<Instance>:ACTion:STATion:REConnect \n
		Snippet: driver.call.action.station.reconnect.set() \n
		Re-establishes the existing association to the AP under test. The command has the same effect as a disconnect, followed
		immediately by a connect. The command is only relevant in the operation mode 'Station' with connection mode 'Manual'. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALL:WLAN:SIGNaling<Instance>:ACTion:STATion:REConnect', opc_timeout_ms)
