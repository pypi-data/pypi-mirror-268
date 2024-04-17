from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EloggingCls:
	"""Elogging commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("elogging", core, parent)

	def set(self) -> None:
		"""SCPI: CLEan:WLAN:SIGNaling<instance>:ELOGging \n
		Snippet: driver.clean.elogging.set() \n
		Clears the event log. \n
		"""
		self._core.io.write(f'CLEan:WLAN:SIGNaling<Instance>:ELOGging')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CLEan:WLAN:SIGNaling<instance>:ELOGging \n
		Snippet: driver.clean.elogging.set_with_opc() \n
		Clears the event log. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWlanSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CLEan:WLAN:SIGNaling<Instance>:ELOGging', opc_timeout_ms)
