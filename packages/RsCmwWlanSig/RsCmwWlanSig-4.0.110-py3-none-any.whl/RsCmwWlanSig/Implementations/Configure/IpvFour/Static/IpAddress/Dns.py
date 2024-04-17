from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DnsCls:
	"""Dns commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dns", core, parent)

	def set(self, first: int, sec: int, third: int, fourth: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:IPVFour:STATic:IPADdress:DNS \n
		Snippet: driver.configure.ipvFour.static.ipAddress.dns.set(first = 1, sec = 1, third = 1, fourth = 1) \n
		Provides the IPv4 address of a DNS server to the built-in IPv4 stack. The setting is relevant for instruments without DAU. \n
			:param first: No help available
			:param sec: No help available
			:param third: No help available
			:param fourth: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('first', first, DataType.Integer), ArgSingle('sec', sec, DataType.Integer), ArgSingle('third', third, DataType.Integer), ArgSingle('fourth', fourth, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:IPVFour:STATic:IPADdress:DNS {param}'.rstrip())

	# noinspection PyTypeChecker
	class DnsStruct(StructBase):
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

	def get(self) -> DnsStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:IPVFour:STATic:IPADdress:DNS \n
		Snippet: value: DnsStruct = driver.configure.ipvFour.static.ipAddress.dns.get() \n
		Provides the IPv4 address of a DNS server to the built-in IPv4 stack. The setting is relevant for instruments without DAU. \n
			:return: structure: for return value, see the help for DnsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:IPVFour:STATic:IPADdress:DNS?', self.__class__.DnsStruct())
