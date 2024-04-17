from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OobDiscoveryCls:
	"""OobDiscovery commands group definition. 8 total commands, 0 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oobDiscovery", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:ENABle \n
		Snippet: value: bool = driver.configure.connection.oobDiscovery.get_enable() \n
		Disables or enables the out-of-band discovery for a co-located AP. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:ENABle \n
		Snippet: driver.configure.connection.oobDiscovery.set_enable(enable = False) \n
		Disables or enables the out-of-band discovery for a co-located AP. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:ENABle {param}')

	def get_ssid(self) -> str:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:SSID \n
		Snippet: value: str = driver.configure.connection.oobDiscovery.get_ssid() \n
		Configures the SSID of the co-located AP operating as the other WLAN instance. \n
			:return: ssid: string Additional parameters: OFF | ON (disables | enables the discovery) .
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:SSID?')
		return trim_str_response(response)

	def set_ssid(self, ssid: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:SSID \n
		Snippet: driver.configure.connection.oobDiscovery.set_ssid(ssid = 'abc') \n
		Configures the SSID of the co-located AP operating as the other WLAN instance. \n
			:param ssid: string Additional parameters: OFF | ON (disables | enables the discovery) .
		"""
		param = Conversions.value_to_quoted_str(ssid)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:SSID {param}')

	def get_bssid(self) -> str:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:BSSid \n
		Snippet: value: str = driver.configure.connection.oobDiscovery.get_bssid() \n
		Configures the BSSID for the co-located AP. \n
			:return: mac: hex Range: 0 to 281.474976710655E+12
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:BSSid?')
		return trim_str_response(response)

	def set_bssid(self, mac: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:BSSid \n
		Snippet: driver.configure.connection.oobDiscovery.set_bssid(mac = rawAbc) \n
		Configures the BSSID for the co-located AP. \n
			:param mac: hex Range: 0 to 281.474976710655E+12
		"""
		param = Conversions.value_to_str(mac)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:BSSid {param}')

	def get_channel(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:CHANnel \n
		Snippet: value: int = driver.configure.connection.oobDiscovery.get_channel() \n
		Configures the channel number for the co-located AP. \n
			:return: channel: integer Range: 1 to 253
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:CHANnel \n
		Snippet: driver.configure.connection.oobDiscovery.set_channel(channel = 1) \n
		Configures the channel number for the co-located AP. \n
			:param channel: integer Range: 1 to 253
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:CHANnel {param}')

	def get_op_class(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:OPCLass \n
		Snippet: value: int = driver.configure.connection.oobDiscovery.get_op_class() \n
		Configures the operation class for the co-located AP. \n
			:return: class_py: integer Range: 1 to 255
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:OPCLass?')
		return Conversions.str_to_int(response)

	def set_op_class(self, class_py: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:OPCLass \n
		Snippet: driver.configure.connection.oobDiscovery.set_op_class(class_py = 1) \n
		Configures the operation class for the co-located AP. \n
			:param class_py: integer Range: 1 to 255
		"""
		param = Conversions.decimal_value_to_str(class_py)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:OPCLass {param}')

	def get_psd(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:PSD \n
		Snippet: value: float = driver.configure.connection.oobDiscovery.get_psd() \n
		Configures the power level for power spectral density for 20 MHz channels. \n
			:return: value: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:PSD?')
		return Conversions.str_to_float(response)

	def set_psd(self, value: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:PSD \n
		Snippet: driver.configure.connection.oobDiscovery.set_psd(value = 1.0) \n
		Configures the power level for power spectral density for 20 MHz channels. \n
			:param value: float Range: -64 to 63.5, Unit: dBm / 20 MHz
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:PSD {param}')

	def get_probe_resp(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:PROBeresp \n
		Snippet: value: bool = driver.configure.connection.oobDiscovery.get_probe_resp() \n
		Enables or disables the unsolicited probe responses for the co-located AP operating in 6 GHz band. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:PROBeresp?')
		return Conversions.str_to_bool(response)

	def set_probe_resp(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:PROBeresp \n
		Snippet: driver.configure.connection.oobDiscovery.set_probe_resp(enable = False) \n
		Enables or disables the unsolicited probe responses for the co-located AP operating in 6 GHz band. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:PROBeresp {param}')

	# noinspection PyTypeChecker
	def get_broadcast(self) -> enums.FilsProbe:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:BROadcast \n
		Snippet: value: enums.FilsProbe = driver.configure.connection.oobDiscovery.get_broadcast() \n
		Configures the unsolicited probe responses for the co-located AP operating in sub-6 GHz band. \n
			:return: fils_probe: OFF | FILS | PROBe OFF: disables the discovery of probe responses FILS: enables fast initial link setup authentication PROBe: enables the discovery of unsolicited probe responses
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:BROadcast?')
		return Conversions.str_to_scalar_enum(response, enums.FilsProbe)

	def set_broadcast(self, fils_probe: enums.FilsProbe) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OOBDiscovery:BROadcast \n
		Snippet: driver.configure.connection.oobDiscovery.set_broadcast(fils_probe = enums.FilsProbe.FILS) \n
		Configures the unsolicited probe responses for the co-located AP operating in sub-6 GHz band. \n
			:param fils_probe: OFF | FILS | PROBe OFF: disables the discovery of probe responses FILS: enables fast initial link setup authentication PROBe: enables the discovery of unsolicited probe responses
		"""
		param = Conversions.enum_scalar_to_str(fils_probe, enums.FilsProbe)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OOBDiscovery:BROadcast {param}')
