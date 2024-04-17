from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IconfCls:
	"""Iconf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iconf", core, parent)

	def set(self, ip_first_part: int, ip_second_part: int, ip_third_part: int, ip_fourth_part: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:RSERver:ICONf \n
		Snippet: driver.configure.connection.security.rserver.iconf.set(ip_first_part = 1, ip_second_part = 1, ip_third_part = 1, ip_fourth_part = 1) \n
		Sets the IPv4 address of an external RADIUS server. \n
			:param ip_first_part: No help available
			:param ip_second_part: No help available
			:param ip_third_part: No help available
			:param ip_fourth_part: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ip_first_part', ip_first_part, DataType.Integer), ArgSingle('ip_second_part', ip_second_part, DataType.Integer), ArgSingle('ip_third_part', ip_third_part, DataType.Integer), ArgSingle('ip_fourth_part', ip_fourth_part, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:RSERver:ICONf {param}'.rstrip())

	# noinspection PyTypeChecker
	class IconfStruct(StructBase):
		"""Response structure. Fields: \n
			- Ip_First_Part: int: No parameter help available
			- Ip_Second_Part: int: No parameter help available
			- Ip_Third_Part: int: No parameter help available
			- Ip_Fourth_Part: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Ip_First_Part'),
			ArgStruct.scalar_int('Ip_Second_Part'),
			ArgStruct.scalar_int('Ip_Third_Part'),
			ArgStruct.scalar_int('Ip_Fourth_Part')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ip_First_Part: int = None
			self.Ip_Second_Part: int = None
			self.Ip_Third_Part: int = None
			self.Ip_Fourth_Part: int = None

	def get(self) -> IconfStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:RSERver:ICONf \n
		Snippet: value: IconfStruct = driver.configure.connection.security.rserver.iconf.get() \n
		Sets the IPv4 address of an external RADIUS server. \n
			:return: structure: for return value, see the help for IconfStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:RSERver:ICONf?', self.__class__.IconfStruct())
