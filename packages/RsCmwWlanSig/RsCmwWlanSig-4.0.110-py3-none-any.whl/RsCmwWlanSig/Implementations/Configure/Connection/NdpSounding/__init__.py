from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NdpSoundingCls:
	"""NdpSounding commands group definition. 14 total commands, 1 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ndpSounding", core, parent)

	@property
	def ssTx(self):
		"""ssTx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssTx'):
			from .SsTx import SsTxCls
			self._ssTx = SsTxCls(self._core, self._cmd_group)
		return self._ssTx

	# noinspection PyTypeChecker
	def get_method(self) -> enums.NdpSoundingMethod:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:METHod \n
		Snippet: value: enums.NdpSoundingMethod = driver.configure.connection.ndpSounding.get_method() \n
		Sets the feedback method for NDP sounding procedure. \n
			:return: method: NONTrigger | TBASed 'NONTrigger': non-trigger-based 'TBASed': trigger-based
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:METHod?')
		return Conversions.str_to_scalar_enum(response, enums.NdpSoundingMethod)

	def set_method(self, method: enums.NdpSoundingMethod) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:METHod \n
		Snippet: driver.configure.connection.ndpSounding.set_method(method = enums.NdpSoundingMethod.NONTrigger) \n
		Sets the feedback method for NDP sounding procedure. \n
			:param method: NONTrigger | TBASed 'NONTrigger': non-trigger-based 'TBASed': trigger-based
		"""
		param = Conversions.enum_scalar_to_str(method, enums.NdpSoundingMethod)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:METHod {param}')

	# noinspection PyTypeChecker
	def get_target(self) -> enums.Station:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:TARGet \n
		Snippet: value: enums.Station = driver.configure.connection.ndpSounding.get_target() \n
		Selects the STA to which the NDP sounding applies. This parameter is visible, if 'Multi STA' is enabled. \n
			:return: station: STA1 | STA2 | STA3
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:TARGet?')
		return Conversions.str_to_scalar_enum(response, enums.Station)

	def set_target(self, station: enums.Station) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:TARGet \n
		Snippet: driver.configure.connection.ndpSounding.set_target(station = enums.Station.STA1) \n
		Selects the STA to which the NDP sounding applies. This parameter is visible, if 'Multi STA' is enabled. \n
			:param station: STA1 | STA2 | STA3
		"""
		param = Conversions.enum_scalar_to_str(station, enums.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:TARGet {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.NdpSoundingType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:TYPE \n
		Snippet: value: enums.NdpSoundingType = driver.configure.connection.ndpSounding.get_type_py() \n
		Selects the report type for NDP sounding procedure. All types of feedback are returned via the HE Compressed
		Beamforming/CQI Frame. \n
			:return: type_py: SU | MU | CQI 'SU': single-user feedback 'MU': multi-user feedback (only for trigger-based sounding procedure) 'CQI': channel quality index feedback
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.NdpSoundingType)

	def set_type_py(self, type_py: enums.NdpSoundingType) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:TYPE \n
		Snippet: driver.configure.connection.ndpSounding.set_type_py(type_py = enums.NdpSoundingType.CQI) \n
		Selects the report type for NDP sounding procedure. All types of feedback are returned via the HE Compressed
		Beamforming/CQI Frame. \n
			:param type_py: SU | MU | CQI 'SU': single-user feedback 'MU': multi-user feedback (only for trigger-based sounding procedure) 'CQI': channel quality index feedback
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.NdpSoundingType)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:TYPE {param}')

	# noinspection PyTypeChecker
	def get_bw(self) -> enums.ChannelBandwidthDut:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:BW \n
		Snippet: value: enums.ChannelBandwidthDut = driver.configure.connection.ndpSounding.get_bw() \n
		Selects the channel bandwidth for NDP sounding procedure. \n
			:return: band: BW20 | BW40 | BW80 | BW160
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:BW?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBandwidthDut)

	def set_bw(self, band: enums.ChannelBandwidthDut) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:BW \n
		Snippet: driver.configure.connection.ndpSounding.set_bw(band = enums.ChannelBandwidthDut.BW160) \n
		Selects the channel bandwidth for NDP sounding procedure. \n
			:param band: BW20 | BW40 | BW80 | BW160
		"""
		param = Conversions.enum_scalar_to_str(band, enums.ChannelBandwidthDut)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:BW {param}')

	# noinspection PyTypeChecker
	def get_sp_streams(self) -> enums.Streams:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:SPSTreams \n
		Snippet: value: enums.Streams = driver.configure.connection.ndpSounding.get_sp_streams() \n
		Selects the number of spatial streams for NDP sounding procedure. \n
			:return: num_streams: STR1 | STR2
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:SPSTreams?')
		return Conversions.str_to_scalar_enum(response, enums.Streams)

	def set_sp_streams(self, num_streams: enums.Streams) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:SPSTreams \n
		Snippet: driver.configure.connection.ndpSounding.set_sp_streams(num_streams = enums.Streams.STR1) \n
		Selects the number of spatial streams for NDP sounding procedure. \n
			:param num_streams: STR1 | STR2
		"""
		param = Conversions.enum_scalar_to_str(num_streams, enums.Streams)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:SPSTreams {param}')

	# noinspection PyTypeChecker
	def get_ltf_gi(self) -> enums.LtfGi:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:LTFGi \n
		Snippet: value: enums.LtfGi = driver.configure.connection.ndpSounding.get_ltf_gi() \n
		Selects the GI / LTF combination for NDP sounding procedure. \n
			:return: ltf_gi: L208 | L216 | L432 'L208': 2x HE-LTF + 0.8 µs GI 'L216': 2x HE-LTF + 1.6 µs GI 'L432': 4x HE-LTF + 3.2 µs GI (optional)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:LTFGi?')
		return Conversions.str_to_scalar_enum(response, enums.LtfGi)

	def set_ltf_gi(self, ltf_gi: enums.LtfGi) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:LTFGi \n
		Snippet: driver.configure.connection.ndpSounding.set_ltf_gi(ltf_gi = enums.LtfGi.L208) \n
		Selects the GI / LTF combination for NDP sounding procedure. \n
			:param ltf_gi: L208 | L216 | L432 'L208': 2x HE-LTF + 0.8 µs GI 'L216': 2x HE-LTF + 1.6 µs GI 'L432': 4x HE-LTF + 3.2 µs GI (optional)
		"""
		param = Conversions.enum_scalar_to_str(ltf_gi, enums.LtfGi)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:LTFGi {param}')

	def get_rustart(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:RUSTart \n
		Snippet: value: int = driver.configure.connection.ndpSounding.get_rustart() \n
		Specifies the 26-tone RU marking the beginning of the measured bandwidth (RU start index) for NDP sounding procedure. \n
			:return: ru_idx: integer Range: 0 to 0
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:RUSTart?')
		return Conversions.str_to_int(response)

	def set_rustart(self, ru_idx: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:RUSTart \n
		Snippet: driver.configure.connection.ndpSounding.set_rustart(ru_idx = 1) \n
		Specifies the 26-tone RU marking the beginning of the measured bandwidth (RU start index) for NDP sounding procedure. \n
			:param ru_idx: integer Range: 0 to 0
		"""
		param = Conversions.decimal_value_to_str(ru_idx)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:RUSTart {param}')

	def get_ruend(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:RUENd \n
		Snippet: value: int = driver.configure.connection.ndpSounding.get_ruend() \n
		Specifies the last 26-tone RU to be measured (RU end index) during NDP sounding procedure. \n
			:return: ru_idx: integer Range: 8 to 8
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:RUENd?')
		return Conversions.str_to_int(response)

	def set_ruend(self, ru_idx: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:RUENd \n
		Snippet: driver.configure.connection.ndpSounding.set_ruend(ru_idx = 1) \n
		Specifies the last 26-tone RU to be measured (RU end index) during NDP sounding procedure. \n
			:param ru_idx: integer Range: 8 to 8
		"""
		param = Conversions.decimal_value_to_str(ru_idx)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:RUENd {param}')

	# noinspection PyTypeChecker
	def get_cbook(self) -> enums.Size:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:CBOok \n
		Snippet: value: enums.Size = driver.configure.connection.ndpSounding.get_cbook() \n
		Sets the codebook size for HE TB sounding: 0 or 1. \n
			:return: size: SIZE0 | SIZE1
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:CBOok?')
		return Conversions.str_to_scalar_enum(response, enums.Size)

	def set_cbook(self, size: enums.Size) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:CBOok \n
		Snippet: driver.configure.connection.ndpSounding.set_cbook(size = enums.Size.SIZE0) \n
		Sets the codebook size for HE TB sounding: 0 or 1. \n
			:param size: SIZE0 | SIZE1
		"""
		param = Conversions.enum_scalar_to_str(size, enums.Size)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:CBOok {param}')

	# noinspection PyTypeChecker
	def get_num_columns(self) -> enums.NumColumns:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:NUMColumns \n
		Snippet: value: enums.NumColumns = driver.configure.connection.ndpSounding.get_num_columns() \n
		Sets the number of columns value Nc for HE TB sounding. \n
			:return: num_col: COL1 | COL2
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:NUMColumns?')
		return Conversions.str_to_scalar_enum(response, enums.NumColumns)

	def set_num_columns(self, num_col: enums.NumColumns) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:NUMColumns \n
		Snippet: driver.configure.connection.ndpSounding.set_num_columns(num_col = enums.NumColumns.COL1) \n
		Sets the number of columns value Nc for HE TB sounding. \n
			:param num_col: COL1 | COL2
		"""
		param = Conversions.enum_scalar_to_str(num_col, enums.NumColumns)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:NUMColumns {param}')

	# noinspection PyTypeChecker
	def get_sub_grouping(self) -> enums.Ngrouping:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:SUBGrouping \n
		Snippet: value: enums.Ngrouping = driver.configure.connection.ndpSounding.get_sub_grouping() \n
		No command help available \n
			:return: ng: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:SUBGrouping?')
		return Conversions.str_to_scalar_enum(response, enums.Ngrouping)

	def set_sub_grouping(self, ng: enums.Ngrouping) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:SUBGrouping \n
		Snippet: driver.configure.connection.ndpSounding.set_sub_grouping(ng = enums.Ngrouping.GRP16) \n
		No command help available \n
			:param ng: No help available
		"""
		param = Conversions.enum_scalar_to_str(ng, enums.Ngrouping)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:SUBGrouping {param}')

	def get_txp(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:TXP \n
		Snippet: value: int = driver.configure.connection.ndpSounding.get_txp() \n
		Selects the periodic transmission interval for NDP sounding procedure. \n
			:return: interval: integer Range: 1 to 10E+3, Unit: ms
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:TXP?')
		return Conversions.str_to_int(response)

	def set_txp(self, interval: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:TXP \n
		Snippet: driver.configure.connection.ndpSounding.set_txp(interval = 1) \n
		Selects the periodic transmission interval for NDP sounding procedure. \n
			:param interval: integer Range: 1 to 10E+3, Unit: ms
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:TXP {param}')

	def get_txen(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:TXEN \n
		Snippet: value: bool = driver.configure.connection.ndpSounding.get_txen() \n
		Switches on or off the periodic transmission for NDP sounding procedure. \n
			:return: state: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:TXEN?')
		return Conversions.str_to_bool(response)

	def set_txen(self, state: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:NDPSounding:TXEN \n
		Snippet: driver.configure.connection.ndpSounding.set_txen(state = False) \n
		Switches on or off the periodic transmission for NDP sounding procedure. \n
			:param state: OFF | ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:NDPSounding:TXEN {param}')

	def clone(self) -> 'NdpSoundingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NdpSoundingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
