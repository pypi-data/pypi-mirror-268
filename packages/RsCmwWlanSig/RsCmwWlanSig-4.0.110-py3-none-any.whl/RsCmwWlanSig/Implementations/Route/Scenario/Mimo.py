from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Pcc_Bb_Board: enums.PccBasebandBoard: Signaling unit
			- Rx_Connector: enums.RxConnector: RF connector for the input path 1
			- Rx_Converter: enums.RxConverter: RX module for the input path 1
			- Tx_Connector: enums.TxConnector: RF connector for output path 1
			- Tx_Converter: enums.TxConverter: TX module for output path 1
			- Tx_2_Connector: enums.TxConnector: RF connector for output path 2
			- Tx_2_Converter: enums.TxConverter: TX module for output path 2. Select different modules for the two paths.
			- Rx_2_Connector: enums.RxConnector: Optional setting parameter. RF connector for the input path 2
			- Rx_2_Converter: enums.RxConverter: Optional setting parameter. RX module for the input path 2. Select different modules for the two paths."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.PccBasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum_optional('Rx_2_Connector', enums.RxConnector),
			ArgStruct.scalar_enum_optional('Rx_2_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.PccBasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Rx_2_Connector: enums.RxConnector = None
			self.Rx_2_Converter: enums.RxConverter = None

	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:WLAN:SIGNaling<instance>:SCENario:MIMO:FLEXible \n
		Snippet: value: FlexibleStruct = driver.route.scenario.mimo.get_flexible() \n
		Defines the RX and TX routing for the MIMO scenarios. For possible connector and converter values, see 'Values for signal
		path selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WLAN:SIGNaling<Instance>:SCENario:MIMO:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:WLAN:SIGNaling<instance>:SCENario:MIMO:FLEXible \n
		Snippet with structure: \n
		structure = driver.route.scenario.mimo.FlexibleStruct() \n
		structure.Pcc_Bb_Board: enums.PccBasebandBoard = enums.PccBasebandBoard.BBR1 \n
		structure.Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Tx_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Rx_2_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_2_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		driver.route.scenario.mimo.set_flexible(value = structure) \n
		Defines the RX and TX routing for the MIMO scenarios. For possible connector and converter values, see 'Values for signal
		path selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:WLAN:SIGNaling<Instance>:SCENario:MIMO:FLEXible', value)
