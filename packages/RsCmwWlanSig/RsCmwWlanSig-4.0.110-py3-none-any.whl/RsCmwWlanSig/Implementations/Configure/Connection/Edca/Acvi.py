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

	def set(self, aif_sn: int, ecw_min: int, ecw_max: int, tx_op_lim: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:EDCA:ACVI \n
		Snippet: driver.configure.connection.edca.acvi.set(aif_sn = 1, ecw_min = 1, ecw_max = 1, tx_op_lim = 1) \n
		Configures the record fields of EDCA parameter set. \n
			:param aif_sn: integer Arbitration inter-frame space number Range: 2 to 15
			:param ecw_min: integer Minimal contention window Range: 0 to 15
			:param ecw_max: integer Maximal contention window Range: 0 to 15
			:param tx_op_lim: integer Transmission opportunity limit Range: 0 to 255
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aif_sn', aif_sn, DataType.Integer), ArgSingle('ecw_min', ecw_min, DataType.Integer), ArgSingle('ecw_max', ecw_max, DataType.Integer), ArgSingle('tx_op_lim', tx_op_lim, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:EDCA:ACVI {param}'.rstrip())

	# noinspection PyTypeChecker
	class AcviStruct(StructBase):
		"""Response structure. Fields: \n
			- Aif_Sn: int: integer Arbitration inter-frame space number Range: 2 to 15
			- Ecw_Min: int: integer Minimal contention window Range: 0 to 15
			- Ecw_Max: int: integer Maximal contention window Range: 0 to 15
			- Tx_Op_Lim: int: integer Transmission opportunity limit Range: 0 to 255"""
		__meta_args_list = [
			ArgStruct.scalar_int('Aif_Sn'),
			ArgStruct.scalar_int('Ecw_Min'),
			ArgStruct.scalar_int('Ecw_Max'),
			ArgStruct.scalar_int('Tx_Op_Lim')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aif_Sn: int = None
			self.Ecw_Min: int = None
			self.Ecw_Max: int = None
			self.Tx_Op_Lim: int = None

	def get(self) -> AcviStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:EDCA:ACVI \n
		Snippet: value: AcviStruct = driver.configure.connection.edca.acvi.get() \n
		Configures the record fields of EDCA parameter set. \n
			:return: structure: for return value, see the help for AcviStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:EDCA:ACVI?', self.__class__.AcviStruct())
