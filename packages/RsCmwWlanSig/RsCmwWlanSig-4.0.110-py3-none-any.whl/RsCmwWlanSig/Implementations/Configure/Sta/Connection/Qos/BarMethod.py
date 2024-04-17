from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BarMethodCls:
	"""BarMethod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("barMethod", core, parent)

	def set(self, method: enums.BarMethod, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:QOS:BARMethod \n
		Snippet: driver.configure.sta.connection.qos.barMethod.set(method = enums.BarMethod.EXPBar, station = repcap.Station.Default) \n
		Specifies the method used to request a BlockAck frame from the DUT \n
			:param method: IMPBar | EXPBar | MUBar Implicit, explicit or multi-user block acknowledgment request
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = Conversions.enum_scalar_to_str(method, enums.BarMethod)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:QOS:BARMethod {param}')

	# noinspection PyTypeChecker
	def get(self, station=repcap.Station.Default) -> enums.BarMethod:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:QOS:BARMethod \n
		Snippet: value: enums.BarMethod = driver.configure.sta.connection.qos.barMethod.get(station = repcap.Station.Default) \n
		Specifies the method used to request a BlockAck frame from the DUT \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: method: IMPBar | EXPBar | MUBar Implicit, explicit or multi-user block acknowledgment request"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:QOS:BARMethod?')
		return Conversions.str_to_scalar_enum(response, enums.BarMethod)
