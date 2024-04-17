from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QosCls:
	"""Qos commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qos", core, parent)

	# noinspection PyTypeChecker
	def get_etoe(self) -> enums.Tid:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:QOS:ETOE \n
		Snippet: value: enums.Tid = driver.configure.connection.qos.get_etoe() \n
		Sets the TID value to be used for the end-to-end connection using DAU. \n
			:return: tid: TID0 | TID1 | TID2 | TID3 | TID4 | TID5 | TID6 | TID7
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:QOS:ETOE?')
		return Conversions.str_to_scalar_enum(response, enums.Tid)

	def set_etoe(self, tid: enums.Tid) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:QOS:ETOE \n
		Snippet: driver.configure.connection.qos.set_etoe(tid = enums.Tid.TID0) \n
		Sets the TID value to be used for the end-to-end connection using DAU. \n
			:param tid: TID0 | TID1 | TID2 | TID3 | TID4 | TID5 | TID6 | TID7
		"""
		param = Conversions.enum_scalar_to_str(tid, enums.Tid)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:QOS:ETOE {param}')

	# noinspection PyTypeChecker
	def get_prioritiz(self) -> enums.PrioMode:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:QOS:PRIoritiz \n
		Snippet: value: enums.PrioMode = driver.configure.connection.qos.get_prioritiz() \n
			INTRO_CMD_HELP: Prioritization mode selects the transmission sequence. \n
			- Round-robin schedules equal transmission time to each TID
			- TID priority selection prioritizes the transmission of highest TID values
			- Automatic selection \n
			:return: mode: ROURobin | TIDPriority | AUTO
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:QOS:PRIoritiz?')
		return Conversions.str_to_scalar_enum(response, enums.PrioMode)

	def set_prioritiz(self, mode: enums.PrioMode) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:QOS:PRIoritiz \n
		Snippet: driver.configure.connection.qos.set_prioritiz(mode = enums.PrioMode.AUTO) \n
			INTRO_CMD_HELP: Prioritization mode selects the transmission sequence. \n
			- Round-robin schedules equal transmission time to each TID
			- TID priority selection prioritizes the transmission of highest TID values
			- Automatic selection \n
			:param mode: ROURobin | TIDPriority | AUTO
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PrioMode)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:QOS:PRIoritiz {param}')
