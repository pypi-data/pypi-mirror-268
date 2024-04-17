from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StationCls:
	"""Station commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("station", core, parent)

	# noinspection PyTypeChecker
	def get_sconnection(self) -> enums.ConnectionAllowed:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STATion:SCONnection \n
		Snippet: value: enums.ConnectionAllowed = driver.configure.connection.station.get_sconnection() \n
		Specifies to which access points the simulated station is allowed to connect (operation mode 'Station') . \n
			:return: mode: ANY | SSID ANY: Any AP is allowed. SSID: Only a specific AP is allowed, identified by the configured SSID, see method RsCmwWlanSig.Configure.Connection.ssid.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:STATion:SCONnection?')
		return Conversions.str_to_scalar_enum(response, enums.ConnectionAllowed)

	def set_sconnection(self, mode: enums.ConnectionAllowed) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STATion:SCONnection \n
		Snippet: driver.configure.connection.station.set_sconnection(mode = enums.ConnectionAllowed.ANY) \n
		Specifies to which access points the simulated station is allowed to connect (operation mode 'Station') . \n
			:param mode: ANY | SSID ANY: Any AP is allowed. SSID: Only a specific AP is allowed, identified by the configured SSID, see method RsCmwWlanSig.Configure.Connection.ssid.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ConnectionAllowed)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STATion:SCONnection {param}')

	# noinspection PyTypeChecker
	def get_cmode(self) -> enums.ConnectionMode:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STATion:CMODe \n
		Snippet: value: enums.ConnectionMode = driver.configure.connection.station.get_cmode() \n
		Selects the connection behavior of the simulated station (operation mode 'Station') . \n
			:return: mode: ACONnect | MANual ACONnect: automatic connection MANual: manual connection via method RsCmwWlanSig.Call.Action.Station.Connect.set or method RsCmwWlanSig.Call.Action.Station.Reconnect.set
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:STATion:CMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ConnectionMode)

	def set_cmode(self, mode: enums.ConnectionMode) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STATion:CMODe \n
		Snippet: driver.configure.connection.station.set_cmode(mode = enums.ConnectionMode.ACONnect) \n
		Selects the connection behavior of the simulated station (operation mode 'Station') . \n
			:param mode: ACONnect | MANual ACONnect: automatic connection MANual: manual connection via method RsCmwWlanSig.Call.Action.Station.Connect.set or method RsCmwWlanSig.Call.Action.Station.Reconnect.set
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ConnectionMode)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STATion:CMODe {param}')
