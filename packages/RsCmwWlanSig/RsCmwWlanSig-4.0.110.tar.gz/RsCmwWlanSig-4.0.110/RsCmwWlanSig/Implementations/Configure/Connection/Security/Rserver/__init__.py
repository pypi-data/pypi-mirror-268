from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RserverCls:
	"""Rserver commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rserver", core, parent)

	@property
	def iconf(self):
		"""iconf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iconf'):
			from .Iconf import IconfCls
			self._iconf = IconfCls(self._core, self._cmd_group)
		return self._iconf

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SourceInt:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:RSERver:MODE \n
		Snippet: value: enums.SourceInt = driver.configure.connection.security.rserver.get_mode() \n
		Selects the RADIUS server mode for WPA/WPA2 enterprise. \n
			:return: mode: INTernal | EXTernal
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:RSERver:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)

	def set_mode(self, mode: enums.SourceInt) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:RSERver:MODE \n
		Snippet: driver.configure.connection.security.rserver.set_mode(mode = enums.SourceInt.EXTernal) \n
		Selects the RADIUS server mode for WPA/WPA2 enterprise. \n
			:param mode: INTernal | EXTernal
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SourceInt)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:RSERver:MODE {param}')

	def get_skey(self) -> str:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:RSERver:SKEY \n
		Snippet: value: str = driver.configure.connection.security.rserver.get_skey() \n
		Sets the shared key of an external RADIUS server. \n
			:return: string: string Shared key as string
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:RSERver:SKEY?')
		return trim_str_response(response)

	def set_skey(self, string: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:RSERver:SKEY \n
		Snippet: driver.configure.connection.security.rserver.set_skey(string = 'abc') \n
		Sets the shared key of an external RADIUS server. \n
			:param string: string Shared key as string
		"""
		param = Conversions.value_to_quoted_str(string)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:RSERver:SKEY {param}')

	def get_pnumber(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:RSERver:PNUMber \n
		Snippet: value: int = driver.configure.connection.security.rserver.get_pnumber() \n
		Sets the UDP port number of an external RADIUS server. \n
			:return: number: integer Range: 1 to 65535
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:RSERver:PNUMber?')
		return Conversions.str_to_int(response)

	def set_pnumber(self, number: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:RSERver:PNUMber \n
		Snippet: driver.configure.connection.security.rserver.set_pnumber(number = 1) \n
		Sets the UDP port number of an external RADIUS server. \n
			:param number: integer Range: 1 to 65535
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:RSERver:PNUMber {param}')

	def clone(self) -> 'RserverCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RserverCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
