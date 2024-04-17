from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Main_State: bool: OFF | ON
			- Sync_State: enums.SyncState: PENDing | ADJusted PENDing: The generator has been turned on (off) but the signal is not yet (still) available. ADJusted: The physical output signal corresponds to the main generator state.
			- Dut_1: enums.PsState: IDLE | AUTHenticated | ASSociated | DEAuthenticated | DISassociated | CTIMeout
			- Dut_2: enums.PsState: IDLE | AUTHenticated | ASSociated | DEAuthenticated | DISassociated | CTIMeout
			- Dut_3: enums.PsState: IDLE | AUTHenticated | ASSociated | DEAuthenticated | DISassociated | CTIMeout"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Main_State'),
			ArgStruct.scalar_enum('Sync_State', enums.SyncState),
			ArgStruct.scalar_enum('Dut_1', enums.PsState),
			ArgStruct.scalar_enum('Dut_2', enums.PsState),
			ArgStruct.scalar_enum('Dut_3', enums.PsState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Main_State: bool = None
			self.Sync_State: enums.SyncState = None
			self.Dut_1: enums.PsState = None
			self.Dut_2: enums.PsState = None
			self.Dut_3: enums.PsState = None

	def get_all(self) -> AllStruct:
		"""SCPI: SOURce:WLAN:SIGNaling<instance>:STATe:ALL \n
		Snippet: value: AllStruct = driver.source.state.get_all() \n
		Returns detailed information about the WLAN signaling generator state and the connection state of station one to three.
		See also 'Connection status'. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:WLAN:SIGNaling<Instance>:STATe:ALL?', self.__class__.AllStruct())

	def get_value(self) -> bool:
		"""SCPI: SOURce:WLAN:SIGNaling<instance>:STATe \n
		Snippet: value: bool = driver.source.state.get_value() \n
		Turns the generator (the cell) on or off. \n
			:return: main_state: ON | OFF | 1 | 0 Switch generator ON or OFF
		"""
		response = self._core.io.query_str_with_opc('SOURce:WLAN:SIGNaling<Instance>:STATe?')
		return Conversions.str_to_bool(response)

	def set_value(self, main_state: bool) -> None:
		"""SCPI: SOURce:WLAN:SIGNaling<instance>:STATe \n
		Snippet: driver.source.state.set_value(main_state = False) \n
		Turns the generator (the cell) on or off. \n
			:param main_state: ON | OFF | 1 | 0 Switch generator ON or OFF
		"""
		param = Conversions.bool_to_str(main_state)
		self._core.io.write_with_opc(f'SOURce:WLAN:SIGNaling<Instance>:STATe {param}')
