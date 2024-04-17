from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsTxCls:
	"""SsTx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssTx", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:SSTX \n
		Snippet: driver.configure.connection.hetf.ssTx.set() \n
		Transmits the trigger frame once. \n
		"""
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:SSTX')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:SSTX \n
		Snippet: driver.configure.connection.hetf.ssTx.set_with_opc() \n
		Transmits the trigger frame once. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWlanSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:SSTX', opc_timeout_ms)
