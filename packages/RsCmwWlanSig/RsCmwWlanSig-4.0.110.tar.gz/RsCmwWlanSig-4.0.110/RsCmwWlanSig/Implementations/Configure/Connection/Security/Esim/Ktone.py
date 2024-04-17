from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class KtoneCls:
	"""Ktone commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ktone", core, parent)

	def set(self, rand: str, sres: str, kc: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:ESIM:KTONe \n
		Snippet: driver.configure.connection.security.esim.ktone.set(rand = 'abc', sres = 'abc', kc = 'abc') \n
		Defines the first triplet for EAP-SIM authentication (internal RADIUS server) . \n
			:param rand: string Random challenge as string with 32 hexadecimal digits
			:param sres: string Signed response as string with 8 hexadecimal digits
			:param kc: string Ciphering key as string with 16 hexadecimal digits
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rand', rand, DataType.String), ArgSingle('sres', sres, DataType.String), ArgSingle('kc', kc, DataType.String))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:ESIM:KTONe {param}'.rstrip())

	# noinspection PyTypeChecker
	class KtoneStruct(StructBase):
		"""Response structure. Fields: \n
			- Rand: str: string Random challenge as string with 32 hexadecimal digits
			- Sres: str: string Signed response as string with 8 hexadecimal digits
			- Kc: str: string Ciphering key as string with 16 hexadecimal digits"""
		__meta_args_list = [
			ArgStruct.scalar_str('Rand'),
			ArgStruct.scalar_str('Sres'),
			ArgStruct.scalar_str('Kc')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rand: str = None
			self.Sres: str = None
			self.Kc: str = None

	def get(self) -> KtoneStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:ESIM:KTONe \n
		Snippet: value: KtoneStruct = driver.configure.connection.security.esim.ktone.get() \n
		Defines the first triplet for EAP-SIM authentication (internal RADIUS server) . \n
			:return: structure: for return value, see the help for KtoneStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:ESIM:KTONe?', self.__class__.KtoneStruct())
