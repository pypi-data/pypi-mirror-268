from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HetfCls:
	"""Hetf commands group definition. 11 total commands, 1 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hetf", core, parent)

	@property
	def ssTx(self):
		"""ssTx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssTx'):
			from .SsTx import SsTxCls
			self._ssTx = SsTxCls(self._core, self._cmd_group)
		return self._ssTx

	def get_txp(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:TXP \n
		Snippet: value: int = driver.configure.connection.hetf.get_txp() \n
		Sets the interval for periodical trigger frame. \n
			:return: interval: integer Range: 1 to 10E+3, Unit: ms
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:TXP?')
		return Conversions.str_to_int(response)

	def set_txp(self, interval: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:TXP \n
		Snippet: driver.configure.connection.hetf.set_txp(interval = 1) \n
		Sets the interval for periodical trigger frame. \n
			:param interval: integer Range: 1 to 10E+3, Unit: ms
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:TXP {param}')

	def get_txen(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:TXEN \n
		Snippet: value: bool = driver.configure.connection.hetf.get_txen() \n
		Enables/ disables the periodical trigger frame. \n
			:return: state: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:TXEN?')
		return Conversions.str_to_bool(response)

	def set_txen(self, state: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:TXEN \n
		Snippet: driver.configure.connection.hetf.set_txen(state = False) \n
		Enables/ disables the periodical trigger frame. \n
			:param state: OFF | ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:TXEN {param}')

	def get_ldpc(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:LDPC \n
		Snippet: value: bool = driver.configure.connection.hetf.get_ldpc() \n
		Specifies the support of LDPC extra symbol segment. \n
			:return: extra_symbol: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:LDPC?')
		return Conversions.str_to_bool(response)

	def set_ldpc(self, extra_symbol: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:LDPC \n
		Snippet: driver.configure.connection.hetf.set_ldpc(extra_symbol = False) \n
		Specifies the support of LDPC extra symbol segment. \n
			:param extra_symbol: OFF | ON
		"""
		param = Conversions.bool_to_str(extra_symbol)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:LDPC {param}')

	# noinspection PyTypeChecker
	class ApTxPowerStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Int_Value: int: decimal Range: 0 to 60
			- Dbm_Value: int: decimal Range: -20 dBm to 40 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Int_Value'),
			ArgStruct.scalar_int('Dbm_Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Int_Value: int = None
			self.Dbm_Value: int = None

	def get_ap_tx_power(self) -> ApTxPowerStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:APTXpower \n
		Snippet: value: ApTxPowerStruct = driver.configure.connection.hetf.get_ap_tx_power() \n
		Specifies the value of 'AP TX Power' the R&S CMW signals via a trigger frame. \n
			:return: structure: for return value, see the help for ApTxPowerStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:APTXpower?', self.__class__.ApTxPowerStruct())

	# noinspection PyTypeChecker
	def get_mltf(self) -> enums.MuMimoLongTrainField:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:MLTF \n
		Snippet: value: enums.MuMimoLongTrainField = driver.configure.connection.hetf.get_mltf() \n
		Sets MU-MIMO long training fields (LTF) . \n
			:return: mu_mimo_ltf: SING | MASK SING: single stream pilots MASK: mask LTF sequence of each spatial stream by a distinct orthogonal code
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:MLTF?')
		return Conversions.str_to_scalar_enum(response, enums.MuMimoLongTrainField)

	def set_mltf(self, mu_mimo_ltf: enums.MuMimoLongTrainField) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:MLTF \n
		Snippet: driver.configure.connection.hetf.set_mltf(mu_mimo_ltf = enums.MuMimoLongTrainField.MASK) \n
		Sets MU-MIMO long training fields (LTF) . \n
			:param mu_mimo_ltf: SING | MASK SING: single stream pilots MASK: mask LTF sequence of each spatial stream by a distinct orthogonal code
		"""
		param = Conversions.enum_scalar_to_str(mu_mimo_ltf, enums.MuMimoLongTrainField)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:MLTF {param}')

	# noinspection PyTypeChecker
	def get_gilt(self) -> enums.Giltf:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:GILT \n
		Snippet: value: enums.Giltf = driver.configure.connection.hetf.get_gilt() \n
		Specifies the guard interval and LTF type of the HE TB PPDU. For method RsCmwWlanSig.Configure.Connection.Hetf.mltf MASK,
		the value '1x HE-LTF + 1.6 µs GI' is not supported. \n
			:return: giltf: L116 | L216 | L432 LTF type and corresponding GI: L116: 1x HE-LTF + 1.6 µs GI L216: 2x HE-LTF + 1.6 µs GI L432: 4x HE-LTF + 3.2 µs GI
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:GILT?')
		return Conversions.str_to_scalar_enum(response, enums.Giltf)

	def set_gilt(self, giltf: enums.Giltf) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:GILT \n
		Snippet: driver.configure.connection.hetf.set_gilt(giltf = enums.Giltf.L116) \n
		Specifies the guard interval and LTF type of the HE TB PPDU. For method RsCmwWlanSig.Configure.Connection.Hetf.mltf MASK,
		the value '1x HE-LTF + 1.6 µs GI' is not supported. \n
			:param giltf: L116 | L216 | L432 LTF type and corresponding GI: L116: 1x HE-LTF + 1.6 µs GI L216: 2x HE-LTF + 1.6 µs GI L432: 4x HE-LTF + 3.2 µs GI
		"""
		param = Conversions.enum_scalar_to_str(giltf, enums.Giltf)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:GILT {param}')

	# noinspection PyTypeChecker
	def get_chbw(self) -> enums.ChannelBandwidthDut:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:CHBW \n
		Snippet: value: enums.ChannelBandwidthDut = driver.configure.connection.hetf.get_chbw() \n
		Specifies the channel bandwidth of the HE TB PPDU. \n
			:return: bandwidth: BW20 | BW40 | BW80 | BW160
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:CHBW?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBandwidthDut)

	def set_chbw(self, bandwidth: enums.ChannelBandwidthDut) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:CHBW \n
		Snippet: driver.configure.connection.hetf.set_chbw(bandwidth = enums.ChannelBandwidthDut.BW160) \n
		Specifies the channel bandwidth of the HE TB PPDU. \n
			:param bandwidth: BW20 | BW40 | BW80 | BW160
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.ChannelBandwidthDut)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:CHBW {param}')

	def get_csr(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:CSR \n
		Snippet: value: bool = driver.configure.connection.hetf.get_csr() \n
		Specifies, whether the check of medium status is required before responding. \n
			:return: required: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:CSR?')
		return Conversions.str_to_bool(response)

	def set_csr(self, required: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:CSR \n
		Snippet: driver.configure.connection.hetf.set_csr(required = False) \n
		Specifies, whether the check of medium status is required before responding. \n
			:param required: OFF | ON
		"""
		param = Conversions.bool_to_str(required)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:CSR {param}')

	def get_nof_symbols(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:NOFSymbols \n
		Snippet: value: int = driver.configure.connection.hetf.get_nof_symbols() \n
		Specifies the length of the HE TB PPDU. \n
			:return: num_of_symbols: integer Range: 1 to 330, Unit: symbol
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:NOFSymbols?')
		return Conversions.str_to_int(response)

	def set_nof_symbols(self, num_of_symbols: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:NOFSymbols \n
		Snippet: driver.configure.connection.hetf.set_nof_symbols(num_of_symbols = 1) \n
		Specifies the length of the HE TB PPDU. \n
			:param num_of_symbols: integer Range: 1 to 330, Unit: symbol
		"""
		param = Conversions.decimal_value_to_str(num_of_symbols)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:NOFSymbols {param}')

	# noinspection PyTypeChecker
	def get_ttyp(self) -> enums.TriggerType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:TTYP \n
		Snippet: value: enums.TriggerType = driver.configure.connection.hetf.get_ttyp() \n
		Specifies the trigger type as specified in the Common Info field. \n
			:return: type_py: BTR | BRP | MRTS | BSRP | BQRP BTR: Basic Trigger BRP: Beamforming Report Poll MRTS: MU-RTS BSRP: Buffer Status Report Poll BQRP: Bandwidth Query Report Poll
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:TTYP?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerType)

	def set_ttyp(self, type_py: enums.TriggerType) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HETF:TTYP \n
		Snippet: driver.configure.connection.hetf.set_ttyp(type_py = enums.TriggerType.BQRP) \n
		Specifies the trigger type as specified in the Common Info field. \n
			:param type_py: BTR | BRP | MRTS | BSRP | BQRP BTR: Basic Trigger BRP: Beamforming Report Poll MRTS: MU-RTS BSRP: Buffer Status Report Poll BQRP: Bandwidth Query Report Poll
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TriggerType)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HETF:TTYP {param}')

	def clone(self) -> 'HetfCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HetfCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
