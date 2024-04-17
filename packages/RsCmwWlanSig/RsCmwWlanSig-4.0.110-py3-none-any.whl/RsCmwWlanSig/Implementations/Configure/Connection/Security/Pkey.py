from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PkeyCls:
	"""Pkey commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pkey", core, parent)

	def set(self, key_mode: enums.KeyMode, private_key: str = None) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:PKEY \n
		Snippet: driver.configure.connection.security.pkey.set(key_mode = enums.KeyMode.FIXed, private_key = 'abc') \n
		Sets the private security key for WPA3 personal as a string, 64 to 96 characters. \n
			:param key_mode: RANDom | FIXed RAND: private key assigned automatically FIX: private key assigned manually via private_key
			:param private_key: string
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('key_mode', key_mode, DataType.Enum, enums.KeyMode), ArgSingle('private_key', private_key, DataType.String, None, is_optional=True))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:PKEY {param}'.rstrip())

	# noinspection PyTypeChecker
	class PkeyStruct(StructBase):
		"""Response structure. Fields: \n
			- Key_Mode: enums.KeyMode: RANDom | FIXed RAND: private key assigned automatically FIX: private key assigned manually via private_key
			- Private_Key: str: string"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Key_Mode', enums.KeyMode),
			ArgStruct.scalar_str('Private_Key')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Key_Mode: enums.KeyMode = None
			self.Private_Key: str = None

	def get(self) -> PkeyStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:PKEY \n
		Snippet: value: PkeyStruct = driver.configure.connection.security.pkey.get() \n
		Sets the private security key for WPA3 personal as a string, 64 to 96 characters. \n
			:return: structure: for return value, see the help for PkeyStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:PKEY?', self.__class__.PkeyStruct())
