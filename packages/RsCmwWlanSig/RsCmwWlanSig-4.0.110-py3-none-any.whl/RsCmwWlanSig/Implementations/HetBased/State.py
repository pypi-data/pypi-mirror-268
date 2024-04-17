from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.HeTbMainMeasState:
		"""SCPI: FETCh:WLAN:SIGNaling<instance>:HETBased:STATe \n
		Snippet: value: enums.HeTbMainMeasState = driver.hetBased.state.fetch() \n
		Queries the main measurement state. Use FETCh:...:STATe:ALL? to query the measurement state including the substates. Use
		INITiate..., STOP..., ABORt... to change the measurement state. \n
			:return: state: OFF | RUN | RDY OFF: measurement switched off, no resources allocated, no results available (when entered after ABORt...) RDY: measurement has been terminated, valid results can be available RUN: measurement running (after INITiate..., READ...) , synchronization pending or adjusted, resources active or queued"""
		response = self._core.io.query_str(f'FETCh:WLAN:SIGNaling<Instance>:HETBased:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.HeTbMainMeasState)
