from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DisassCls:
	"""Disass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("disass", core, parent)

	def set(self, enable: bool, timeout: int = None) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:ASSociation:DISass \n
		Snippet: driver.configure.connection.association.disass.set(enable = False, timeout = 1) \n
		Enables or disables automatic STA disassociation, when a STA is no longer present. If enabled, the R&S CMW detects that a
		STA is absent, it automatically removes its association after some user-specified period of time. \n
			:param enable: OFF | ON
			:param timeout: numeric Range: 1 s to 3600 s
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('timeout', timeout, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:ASSociation:DISass {param}'.rstrip())

	# noinspection PyTypeChecker
	class DisassStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF | ON
			- Timeout: int: numeric Range: 1 s to 3600 s"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Timeout')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Timeout: int = None

	def get(self) -> DisassStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:ASSociation:DISass \n
		Snippet: value: DisassStruct = driver.configure.connection.association.disass.get() \n
		Enables or disables automatic STA disassociation, when a STA is no longer present. If enabled, the R&S CMW detects that a
		STA is absent, it automatically removes its association after some user-specified period of time. \n
			:return: structure: for return value, see the help for DisassStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:ASSociation:DISass?', self.__class__.DisassStruct())
