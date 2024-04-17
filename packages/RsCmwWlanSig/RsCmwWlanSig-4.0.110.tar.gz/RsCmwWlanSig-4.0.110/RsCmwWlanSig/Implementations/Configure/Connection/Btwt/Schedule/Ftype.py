from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FtypeCls:
	"""Ftype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ftype", core, parent)

	def set(self, flow_id: int, flow_type: enums.FlowType) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BTWT:SCHedule:FTYPe \n
		Snippet: driver.configure.connection.btwt.schedule.ftype.set(flow_id = 1, flow_type = enums.FlowType.ANNounced) \n
		Specifies the broadcast TWT flow type for the specified schedule period. \n
			:param flow_id: integer
			:param flow_type: ANNounced | UNANnounced
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('flow_id', flow_id, DataType.Integer), ArgSingle('flow_type', flow_type, DataType.Enum, enums.FlowType))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BTWT:SCHedule:FTYPe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, flow_id: int) -> enums.FlowType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BTWT:SCHedule:FTYPe \n
		Snippet: value: enums.FlowType = driver.configure.connection.btwt.schedule.ftype.get(flow_id = 1) \n
		Specifies the broadcast TWT flow type for the specified schedule period. \n
			:param flow_id: integer
			:return: flow_type: ANNounced | UNANnounced"""
		param = Conversions.decimal_value_to_str(flow_id)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BTWT:SCHedule:FTYPe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FlowType)
