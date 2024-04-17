from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UesInfoCls:
	"""UesInfo commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uesInfo", core, parent)

	@property
	def settings(self):
		"""settings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import SettingsCls
			self._settings = SettingsCls(self._core, self._cmd_group)
		return self._settings

	def reset(self) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:UESinfo:RESet \n
		Snippet: driver.configure.uesInfo.reset() \n
		Clears entries in all statistic tables concerning user data traffic. \n
		"""
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:UESinfo:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:UESinfo:RESet \n
		Snippet: driver.configure.uesInfo.reset_with_opc() \n
		Clears entries in all statistic tables concerning user data traffic. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCmwWlanSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:WLAN:SIGNaling<Instance>:UESinfo:RESet', opc_timeout_ms)

	def clone(self) -> 'UesInfoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UesInfoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
