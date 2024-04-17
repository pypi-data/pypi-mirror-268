from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StimeCls:
	"""Stime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stime", core, parent)

	def set(self, flow_id: int, start_time: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BTWT:SCHedule:STIMe \n
		Snippet: driver.configure.connection.btwt.schedule.stime.set(flow_id = 1, start_time = 1.0) \n
		Specifies the offset of the specified schedule period from beacon. \n
			:param flow_id: integer
			:param start_time: numeric Range: 0 ms to 100 ms
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('flow_id', flow_id, DataType.Integer), ArgSingle('start_time', start_time, DataType.Float))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BTWT:SCHedule:STIMe {param}'.rstrip())

	def get(self, flow_id: int) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BTWT:SCHedule:STIMe \n
		Snippet: value: float = driver.configure.connection.btwt.schedule.stime.get(flow_id = 1) \n
		Specifies the offset of the specified schedule period from beacon. \n
			:param flow_id: integer
			:return: start_time: numeric Range: 0 ms to 100 ms"""
		param = Conversions.decimal_value_to_str(flow_id)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BTWT:SCHedule:STIMe? {param}')
		return Conversions.str_to_float(response)
