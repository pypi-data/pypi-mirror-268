from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GatewayCls:
	"""Gateway commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gateway", core, parent)

	def set(self, first: int, sec: int, third: int, fourth: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:IPVFour:STATic:IPADdress:GATeway \n
		Snippet: driver.configure.ipvFour.static.ipAddress.gateway.set(first = 1, sec = 1, third = 1, fourth = 1) \n
		Provides the IPv4 address of the default gateway. The setting is relevant for instruments without DAU. \n
			:param first: No help available
			:param sec: No help available
			:param third: No help available
			:param fourth: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('first', first, DataType.Integer), ArgSingle('sec', sec, DataType.Integer), ArgSingle('third', third, DataType.Integer), ArgSingle('fourth', fourth, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:IPVFour:STATic:IPADdress:GATeway {param}'.rstrip())

	# noinspection PyTypeChecker
	class GatewayStruct(StructBase):
		"""Response structure. Fields: \n
			- First: int: No parameter help available
			- Sec: int: No parameter help available
			- Third: int: No parameter help available
			- Fourth: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('First'),
			ArgStruct.scalar_int('Sec'),
			ArgStruct.scalar_int('Third'),
			ArgStruct.scalar_int('Fourth')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.First: int = None
			self.Sec: int = None
			self.Third: int = None
			self.Fourth: int = None

	def get(self) -> GatewayStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:IPVFour:STATic:IPADdress:GATeway \n
		Snippet: value: GatewayStruct = driver.configure.ipvFour.static.ipAddress.gateway.get() \n
		Provides the IPv4 address of the default gateway. The setting is relevant for instruments without DAU. \n
			:return: structure: for return value, see the help for GatewayStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:IPVFour:STATic:IPADdress:GATeway?', self.__class__.GatewayStruct())
