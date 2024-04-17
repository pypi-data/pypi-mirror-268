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
	def fetch(self) -> enums.PsState:
		"""SCPI: FETCh:WLAN:SIGNaling<instance>:SECond:STATe \n
		Snippet: value: enums.PsState = driver.second.state.fetch() \n
		Gets the connection status, refer to 'Connection status'. Commands for station one, two and three are available. \n
			:return: ps_state: IDLE | PROBed | AUTHenticated | ASSociated | DEAuthenticated | DISassociated | CTIMeout"""
		response = self._core.io.query_str(f'FETCh:WLAN:SIGNaling<Instance>:SECond:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.PsState)
