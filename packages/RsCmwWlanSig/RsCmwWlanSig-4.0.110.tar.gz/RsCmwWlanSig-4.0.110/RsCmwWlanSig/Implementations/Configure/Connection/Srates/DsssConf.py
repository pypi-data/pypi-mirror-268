from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DsssConfCls:
	"""DsssConf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsssConf", core, parent)

	def set(self, d_1_mb: enums.RateSupport, d_2_mb: enums.RateSupport, c_55_m: enums.RateSupport, c_11_m: enums.RateSupport) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SRATes:DSSSconf \n
		Snippet: driver.configure.connection.srates.dsssConf.set(d_1_mb = enums.RateSupport.DISabled, d_2_mb = enums.RateSupport.DISabled, c_55_m = enums.RateSupport.DISabled, c_11_m = enums.RateSupport.DISabled) \n
		Definition of DSSS/CCK supported rates. These settings apply only if user-defined supported rates are enabled, see method
		RsCmwWlanSig.Configure.Connection.Srates.value. \n
			:param d_1_mb: DISabled | MANDatory | OPTional Support for DSSS, 1 Mbit/s
			:param d_2_mb: DISabled | MANDatory | OPTional Support for DSSS, 2 Mbit/s
			:param c_55_m: DISabled | MANDatory | OPTional Support for CCK, 5.5 Mbit/s
			:param c_11_m: DISabled | MANDatory | OPTional Support for CCK, 11 Mbit/s
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('d_1_mb', d_1_mb, DataType.Enum, enums.RateSupport), ArgSingle('d_2_mb', d_2_mb, DataType.Enum, enums.RateSupport), ArgSingle('c_55_m', c_55_m, DataType.Enum, enums.RateSupport), ArgSingle('c_11_m', c_11_m, DataType.Enum, enums.RateSupport))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SRATes:DSSSconf {param}'.rstrip())

	# noinspection PyTypeChecker
	class DsssConfStruct(StructBase):
		"""Response structure. Fields: \n
			- D_1_Mb: enums.RateSupport: DISabled | MANDatory | OPTional Support for DSSS, 1 Mbit/s
			- D_2_Mb: enums.RateSupport: DISabled | MANDatory | OPTional Support for DSSS, 2 Mbit/s
			- C_55_M: enums.RateSupport: DISabled | MANDatory | OPTional Support for CCK, 5.5 Mbit/s
			- C_11_M: enums.RateSupport: DISabled | MANDatory | OPTional Support for CCK, 11 Mbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_enum('D_1_Mb', enums.RateSupport),
			ArgStruct.scalar_enum('D_2_Mb', enums.RateSupport),
			ArgStruct.scalar_enum('C_55_M', enums.RateSupport),
			ArgStruct.scalar_enum('C_11_M', enums.RateSupport)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.D_1_Mb: enums.RateSupport = None
			self.D_2_Mb: enums.RateSupport = None
			self.C_55_M: enums.RateSupport = None
			self.C_11_M: enums.RateSupport = None

	def get(self) -> DsssConfStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SRATes:DSSSconf \n
		Snippet: value: DsssConfStruct = driver.configure.connection.srates.dsssConf.get() \n
		Definition of DSSS/CCK supported rates. These settings apply only if user-defined supported rates are enabled, see method
		RsCmwWlanSig.Configure.Connection.Srates.value. \n
			:return: structure: for return value, see the help for DsssConfStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SRATes:DSSSconf?', self.__class__.DsssConfStruct())
