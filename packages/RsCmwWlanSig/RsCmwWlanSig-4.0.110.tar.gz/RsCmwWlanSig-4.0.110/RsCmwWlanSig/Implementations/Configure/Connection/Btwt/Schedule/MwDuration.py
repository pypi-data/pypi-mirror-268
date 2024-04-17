from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MwDurationCls:
	"""MwDuration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mwDuration", core, parent)

	def set(self, flow_id: int, min_wake_duration: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BTWT:SCHedule:MWDuration \n
		Snippet: driver.configure.connection.btwt.schedule.mwDuration.set(flow_id = 1, min_wake_duration = 1.0) \n
		Specifies the minimum wake duration for the specified scheduled period. \n
			:param flow_id: integer
			:param min_wake_duration: numeric Range: 0 ms to 100 ms
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('flow_id', flow_id, DataType.Integer), ArgSingle('min_wake_duration', min_wake_duration, DataType.Float))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BTWT:SCHedule:MWDuration {param}'.rstrip())

	def get(self, flow_id: int) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BTWT:SCHedule:MWDuration \n
		Snippet: value: float = driver.configure.connection.btwt.schedule.mwDuration.get(flow_id = 1) \n
		Specifies the minimum wake duration for the specified scheduled period. \n
			:param flow_id: integer
			:return: min_wake_duration: numeric Range: 0 ms to 100 ms"""
		param = Conversions.decimal_value_to_str(flow_id)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BTWT:SCHedule:MWDuration? {param}')
		return Conversions.str_to_float(response)
