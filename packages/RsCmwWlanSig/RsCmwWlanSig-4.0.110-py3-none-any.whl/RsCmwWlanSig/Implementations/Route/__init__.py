from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RouteCls:
	"""Route commands group definition. 6 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("route", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenario'):
			from .Scenario import ScenarioCls
			self._scenario = ScenarioCls(self._core, self._cmd_group)
		return self._scenario

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: STANdard cell | MIMO2 | SCFading | MIMFading STANdard Standard SISO scenario MIMO2 MIMO 2x2 (DL and UL) SCFading Standard SISO scenario with fading MIMFading MIMO 2x2 scenario with fading
			- Master: str: string For future use - returned value not relevant
			- Rx_Connector: enums.RxConnector: RF connector for the input path 1
			- Rx_Converter: enums.RxConverter: RX module for the input path 1
			- Tx_Connector: enums.TxConnector: RF connector for output path 1
			- Tx_Converter: enums.TxConverter: TX module for output path 1
			- Tx_Connector_2: enums.TxConnector: RF connector for output path 2
			- Tx_Converter_2: enums.TxConverter: TX module for output path 2
			- Rx_Connector_2: enums.RxConnector: RF connector for the input path 2
			- Rx_Converter_2: enums.RxConverter: RX module for the input path 2"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_str('Master'),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_2', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_2', enums.TxConverter),
			ArgStruct.scalar_enum('Rx_Connector_2', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter_2', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Master: str = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_Connector_2: enums.TxConnector = None
			self.Tx_Converter_2: enums.TxConverter = None
			self.Rx_Connector_2: enums.RxConnector = None
			self.Rx_Converter_2: enums.RxConverter = None

	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:WLAN:SIGNaling<instance> \n
		Snippet: value: ValueStruct = driver.route.get_value() \n
		Queries the active test scenario, the used TRX modules and the used RF connectors. For the STANdard and SCFading
		scenarios, the first six parameters are returned. For the MIMO scenario, all eight parameters are returned. For possible
		connector and converter values, see 'Values for signal path selection'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WLAN:SIGNaling<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'RouteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RouteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
