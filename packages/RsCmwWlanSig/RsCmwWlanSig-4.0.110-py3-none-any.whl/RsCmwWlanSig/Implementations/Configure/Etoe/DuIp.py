from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DuIpCls:
	"""DuIp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duIp", core, parent)

	def set(self, state: bool, first_number: int, sec_number: int, third_number: int, fourth_number: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:ETOE:DUIP \n
		Snippet: driver.configure.etoe.duIp.set(state = False, first_number = 1, sec_number = 1, third_number = 1, fourth_number = 1) \n
		Allows you to specify the IPv4 address that the DAU assigns to the DUT via DHCP. \n
			:param state: OFF | ON Disables/enables the IP address configuration
			:param first_number: No help available
			:param sec_number: No help available
			:param third_number: No help available
			:param fourth_number: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('first_number', first_number, DataType.Integer), ArgSingle('sec_number', sec_number, DataType.Integer), ArgSingle('third_number', third_number, DataType.Integer), ArgSingle('fourth_number', fourth_number, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:ETOE:DUIP {param}'.rstrip())

	# noinspection PyTypeChecker
	class DuIpStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: OFF | ON Disables/enables the IP address configuration
			- First_Number: int: No parameter help available
			- Sec_Number: int: No parameter help available
			- Third_Number: int: No parameter help available
			- Fourth_Number: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_int('First_Number'),
			ArgStruct.scalar_int('Sec_Number'),
			ArgStruct.scalar_int('Third_Number'),
			ArgStruct.scalar_int('Fourth_Number')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.First_Number: int = None
			self.Sec_Number: int = None
			self.Third_Number: int = None
			self.Fourth_Number: int = None

	def get(self) -> DuIpStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:ETOE:DUIP \n
		Snippet: value: DuIpStruct = driver.configure.etoe.duIp.get() \n
		Allows you to specify the IPv4 address that the DAU assigns to the DUT via DHCP. \n
			:return: structure: for return value, see the help for DuIpStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:ETOE:DUIP?', self.__class__.DuIpStruct())
