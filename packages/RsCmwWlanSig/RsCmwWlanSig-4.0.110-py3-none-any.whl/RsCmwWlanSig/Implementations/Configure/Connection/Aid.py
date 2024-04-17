from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AidCls:
	"""Aid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aid", core, parent)

	def set(self, start: int, stop: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:AID \n
		Snippet: driver.configure.connection.aid.set(start = 1, stop = 1) \n
		Specifies the range of IDs to be assigned by the access point to the connected DUTs. \n
			:param start: numeric Range: 1 to 2007
			:param stop: numeric Range: 1 to 2007
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Integer), ArgSingle('stop', stop, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:AID {param}'.rstrip())

	# noinspection PyTypeChecker
	class AidStruct(StructBase):
		"""Response structure. Fields: \n
			- Start: int: numeric Range: 1 to 2007
			- Stop: int: numeric Range: 1 to 2007"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start'),
			ArgStruct.scalar_int('Stop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start: int = None
			self.Stop: int = None

	def get(self) -> AidStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:AID \n
		Snippet: value: AidStruct = driver.configure.connection.aid.get() \n
		Specifies the range of IDs to be assigned by the access point to the connected DUTs. \n
			:return: structure: for return value, see the help for AidStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:AID?', self.__class__.AidStruct())
