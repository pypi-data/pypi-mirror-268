from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectCls:
	"""Connect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connect", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALL:WLAN:SIGNaling<Instance>:ACTion:STATion:CONNect \n
		Snippet: driver.call.action.station.connect.set() \n
		Initiates an association to the AP under test. The command is only relevant in the operation mode 'Station' with
		connection mode 'Manual'. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALL:WLAN:SIGNaling<Instance>:ACTion:STATion:CONNect', opc_timeout_ms)
