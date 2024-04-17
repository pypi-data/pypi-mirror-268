from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcviCls:
	"""Acvi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acvi", core, parent)

	def set(self, aif_sn: int, ecw_min: int, ecw_max: int, timer: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:MUEDca:ACVI \n
		Snippet: driver.configure.connection.muedca.acvi.set(aif_sn = 1, ecw_min = 1, ecw_max = 1, timer = 1) \n
		Configures the record fields of MU EDCA parameter set. \n
			:param aif_sn: integer Arbitration inter-frame space number. Zero disables channel access. Range: 0, 2 to 15
			:param ecw_min: integer Minimal contention window Range: 0 to 15
			:param ecw_max: integer Maximal contention window Range: 0 to 15
			:param timer: integer MU EDCA timer Range: 1 to 255 , Unit: 8x TUs (8x 1024 µs)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aif_sn', aif_sn, DataType.Integer), ArgSingle('ecw_min', ecw_min, DataType.Integer), ArgSingle('ecw_max', ecw_max, DataType.Integer), ArgSingle('timer', timer, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:MUEDca:ACVI {param}'.rstrip())

	# noinspection PyTypeChecker
	class AcviStruct(StructBase):
		"""Response structure. Fields: \n
			- Aif_Sn: int: integer Arbitration inter-frame space number. Zero disables channel access. Range: 0, 2 to 15
			- Ecw_Min: int: integer Minimal contention window Range: 0 to 15
			- Ecw_Max: int: integer Maximal contention window Range: 0 to 15
			- Timer: int: integer MU EDCA timer Range: 1 to 255 , Unit: 8x TUs (8x 1024 µs)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Aif_Sn'),
			ArgStruct.scalar_int('Ecw_Min'),
			ArgStruct.scalar_int('Ecw_Max'),
			ArgStruct.scalar_int('Timer')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aif_Sn: int = None
			self.Ecw_Min: int = None
			self.Ecw_Max: int = None
			self.Timer: int = None

	def get(self) -> AcviStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:MUEDca:ACVI \n
		Snippet: value: AcviStruct = driver.configure.connection.muedca.acvi.get() \n
		Configures the record fields of MU EDCA parameter set. \n
			:return: structure: for return value, see the help for AcviStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:MUEDca:ACVI?', self.__class__.AcviStruct())
