from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class KalgoCls:
	"""Kalgo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("kalgo", core, parent)

	def set(self, ki: str, opc: str, rand: str, algorithm: enums.AuthAlgorithm) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:EAKA:KALGo \n
		Snippet: driver.configure.connection.security.eaka.kalgo.set(ki = 'abc', opc = 'abc', rand = 'abc', algorithm = enums.AuthAlgorithm.MILenage) \n
		Configures EAP-AKA on the internal RADIUS server. \n
			:param ki: string Secret key as string with 32 hexadecimal digits
			:param opc: string Operator variant key as string with 32 hexadecimal digits
			:param rand: string Random number as string with 32 hexadecimal digits
			:param algorithm: MILenage | XOR Authentication algorithm to be used
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ki', ki, DataType.String), ArgSingle('opc', opc, DataType.String), ArgSingle('rand', rand, DataType.String), ArgSingle('algorithm', algorithm, DataType.Enum, enums.AuthAlgorithm))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:EAKA:KALGo {param}'.rstrip())

	# noinspection PyTypeChecker
	class KalgoStruct(StructBase):
		"""Response structure. Fields: \n
			- Ki: str: string Secret key as string with 32 hexadecimal digits
			- Opc: str: string Operator variant key as string with 32 hexadecimal digits
			- Rand: str: string Random number as string with 32 hexadecimal digits
			- Algorithm: enums.AuthAlgorithm: MILenage | XOR Authentication algorithm to be used"""
		__meta_args_list = [
			ArgStruct.scalar_str('Ki'),
			ArgStruct.scalar_str('Opc'),
			ArgStruct.scalar_str('Rand'),
			ArgStruct.scalar_enum('Algorithm', enums.AuthAlgorithm)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ki: str = None
			self.Opc: str = None
			self.Rand: str = None
			self.Algorithm: enums.AuthAlgorithm = None

	def get(self) -> KalgoStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:EAKA:KALGo \n
		Snippet: value: KalgoStruct = driver.configure.connection.security.eaka.kalgo.get() \n
		Configures EAP-AKA on the internal RADIUS server. \n
			:return: structure: for return value, see the help for KalgoStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:EAKA:KALGo?', self.__class__.KalgoStruct())
