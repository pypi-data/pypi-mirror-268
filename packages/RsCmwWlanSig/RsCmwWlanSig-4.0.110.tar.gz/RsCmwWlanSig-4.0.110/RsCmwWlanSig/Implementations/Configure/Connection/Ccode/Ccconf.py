from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcconfCls:
	"""Ccconf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccconf", core, parent)

	def set(self, code_digit: str, first_channel: int, nb_of_channels: int, max_tx_power: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:CCODe:CCConf \n
		Snippet: driver.configure.connection.ccode.ccconf.set(code_digit = 'abc', first_channel = 1, nb_of_channels = 1, max_tx_power = 1) \n
		Sets the regulatory domain information to be transmitted in beacon frames. To enable the transmission, see method
		RsCmwWlanSig.Configure.Connection.Ccode.ccState. \n
			:param code_digit: string Country code as string
			:param first_channel: integer First in the range of allowed channels Range: 0 to 255
			:param nb_of_channels: integer Number of allowed channels Range: 0 to 255
			:param max_tx_power: integer Maximum transmit power Range: -40 dBm to 40 dBm, Unit: dBm
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('code_digit', code_digit, DataType.String), ArgSingle('first_channel', first_channel, DataType.Integer), ArgSingle('nb_of_channels', nb_of_channels, DataType.Integer), ArgSingle('max_tx_power', max_tx_power, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:CCODe:CCConf {param}'.rstrip())

	# noinspection PyTypeChecker
	class CcconfStruct(StructBase):
		"""Response structure. Fields: \n
			- Code_Digit: str: string Country code as string
			- First_Channel: int: integer First in the range of allowed channels Range: 0 to 255
			- Nb_Of_Channels: int: integer Number of allowed channels Range: 0 to 255
			- Max_Tx_Power: int: integer Maximum transmit power Range: -40 dBm to 40 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_str('Code_Digit'),
			ArgStruct.scalar_int('First_Channel'),
			ArgStruct.scalar_int('Nb_Of_Channels'),
			ArgStruct.scalar_int('Max_Tx_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Code_Digit: str = None
			self.First_Channel: int = None
			self.Nb_Of_Channels: int = None
			self.Max_Tx_Power: int = None

	def get(self) -> CcconfStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:CCODe:CCConf \n
		Snippet: value: CcconfStruct = driver.configure.connection.ccode.ccconf.get() \n
		Sets the regulatory domain information to be transmitted in beacon frames. To enable the transmission, see method
		RsCmwWlanSig.Configure.Connection.Ccode.ccState. \n
			:return: structure: for return value, see the help for CcconfStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:CCODe:CCConf?', self.__class__.CcconfStruct())
