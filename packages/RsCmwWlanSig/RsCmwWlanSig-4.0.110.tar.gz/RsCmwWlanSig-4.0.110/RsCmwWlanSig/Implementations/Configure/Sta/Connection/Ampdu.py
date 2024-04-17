from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmpduCls:
	"""Ampdu commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ampdu", core, parent)

	def set(self, enable: enums.EnableState, multi_tid: enums.EnableState, max_length: int, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:AMPDu \n
		Snippet: driver.configure.sta.connection.ampdu.set(enable = enums.EnableState.DISable, multi_tid = enums.EnableState.DISable, max_length = 1, station = repcap.Station.Default) \n
		Configures aggregate MPDUs (A-MPDU) . \n
			:param enable: DISable | ENABle Enables/ disables the A-MPDUs
			:param multi_tid: DISable | ENABle Enables/ disables multi-TID A-MPDU
			:param max_length: integer The maximal length of entire A-MPDU Range: 50 to 131.071E+3, Unit: byte
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Enum, enums.EnableState), ArgSingle('multi_tid', multi_tid, DataType.Enum, enums.EnableState), ArgSingle('max_length', max_length, DataType.Integer))
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:AMPDu {param}'.rstrip())

	# noinspection PyTypeChecker
	class AmpduStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: enums.EnableState: DISable | ENABle Enables/ disables the A-MPDUs
			- Multi_Tid: enums.EnableState: DISable | ENABle Enables/ disables multi-TID A-MPDU
			- Max_Length: int: integer The maximal length of entire A-MPDU Range: 50 to 131.071E+3, Unit: byte"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Enable', enums.EnableState),
			ArgStruct.scalar_enum('Multi_Tid', enums.EnableState),
			ArgStruct.scalar_int('Max_Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: enums.EnableState = None
			self.Multi_Tid: enums.EnableState = None
			self.Max_Length: int = None

	def get(self, station=repcap.Station.Default) -> AmpduStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:AMPDu \n
		Snippet: value: AmpduStruct = driver.configure.sta.connection.ampdu.get(station = repcap.Station.Default) \n
		Configures aggregate MPDUs (A-MPDU) . \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for AmpduStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:AMPDu?', self.__class__.AmpduStruct())
