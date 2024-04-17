from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 17 total commands, 2 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import AntennaCls
			self._antenna = AntennaCls(self._core, self._cmd_group)
		return self._antenna

	@property
	def eattenuation(self):
		"""eattenuation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Eattenuation import EattenuationCls
			self._eattenuation = EattenuationCls(self._core, self._cmd_group)
		return self._eattenuation

	# noinspection PyTypeChecker
	def get_oc_width(self) -> enums.ChannelBandwidthDut:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:OCWidth \n
		Snippet: value: enums.ChannelBandwidthDut = driver.configure.rfSettings.get_oc_width() \n
		Sets the operating channel bandwidth. \n
			:return: value: BW20 | BW40 | BW80 | BW160 BW20: 20 MHz BW40: 40 MHz BW80: 80 MHz BW160: 160 MHz
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:OCWidth?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBandwidthDut)

	def set_oc_width(self, value: enums.ChannelBandwidthDut) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:OCWidth \n
		Snippet: driver.configure.rfSettings.set_oc_width(value = enums.ChannelBandwidthDut.BW160) \n
		Sets the operating channel bandwidth. \n
			:param value: BW20 | BW40 | BW80 | BW160 BW20: 20 MHz BW40: 40 MHz BW80: 80 MHz BW160: 160 MHz
		"""
		param = Conversions.enum_scalar_to_str(value, enums.ChannelBandwidthDut)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:OCWidth {param}')

	def get_foffset(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:FOFFset \n
		Snippet: value: int = driver.configure.rfSettings.get_foffset() \n
		Specifies a positive or negative frequency offset to be added to the configured center frequency. \n
			:return: offset: integer Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, offset: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:FOFFset \n
		Snippet: driver.configure.rfSettings.set_foffset(offset = 1) \n
		Specifies a positive or negative frequency offset to be added to the configured center frequency. \n
			:param offset: integer Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:FOFFset {param}')

	def get_channel(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:CHANnel \n
		Snippet: value: int = driver.configure.rfSettings.get_channel() \n
		Sets the RF channel number. \n
			:return: channel: integer Range: 1 to 196
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:CHANnel \n
		Snippet: driver.configure.rfSettings.set_channel(channel = 1) \n
		Sets the RF channel number. \n
			:param channel: integer Range: 1 to 196
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:CHANnel {param}')

	# noinspection PyTypeChecker
	def get_band(self) -> enums.FrequencyBand:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:BAND \n
		Snippet: value: enums.FrequencyBand = driver.configure.rfSettings.get_band() \n
		Selects the operating band sub 6 GHz or 6 GHz band. \n
			:return: freq_band: BS6Ghz | B6GHz
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.FrequencyBand)

	def set_band(self, freq_band: enums.FrequencyBand) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:BAND \n
		Snippet: driver.configure.rfSettings.set_band(freq_band = enums.FrequencyBand.B6GHz) \n
		Selects the operating band sub 6 GHz or 6 GHz band. \n
			:param freq_band: BS6Ghz | B6GHz
		"""
		param = Conversions.enum_scalar_to_str(freq_band, enums.FrequencyBand)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:BAND {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.rfSettings.get_frequency() \n
		Sets the center frequency of the generated WLAN signal and of the RF analyzer. \n
			:return: frequency: numeric Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.rfSettings.set_frequency(frequency = 1.0) \n
		Sets the center frequency of the generated WLAN signal and of the RF analyzer. \n
			:param frequency: numeric Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:FREQuency {param}')

	def get_np_index(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:NPINdex \n
		Snippet: value: int = driver.configure.rfSettings.get_np_index() \n
		Selects the position of the primary 20-MHz channel, for a signal with more than 20 MHz channel bandwidth. \n
			:return: np_20: integer Index of the 20-MHz channel configured as primary channel Range: 0 to no of channels - 1
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:NPINdex?')
		return Conversions.str_to_int(response)

	def set_np_index(self, np_20: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:NPINdex \n
		Snippet: driver.configure.rfSettings.set_np_index(np_20 = 1) \n
		Selects the position of the primary 20-MHz channel, for a signal with more than 20 MHz channel bandwidth. \n
			:param np_20: integer Index of the 20-MHz channel configured as primary channel Range: 0 to no of channels - 1
		"""
		param = Conversions.decimal_value_to_str(np_20)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:NPINdex {param}')

	def get_np_frequency(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:NPFRequency \n
		Snippet: value: float = driver.configure.rfSettings.get_np_frequency() \n
		Sets the center frequency of the primary 20-MHz channel, for a signal with more than 20 MHz bandwidth. \n
			:return: np_20_freq: numeric Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:NPFRequency?')
		return Conversions.str_to_float(response)

	def set_np_frequency(self, np_20_freq: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:NPFRequency \n
		Snippet: driver.configure.rfSettings.set_np_frequency(np_20_freq = 1.0) \n
		Sets the center frequency of the primary 20-MHz channel, for a signal with more than 20 MHz bandwidth. \n
			:param np_20_freq: numeric Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(np_20_freq)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:NPFRequency {param}')

	def get_np_channel(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:NPCHannel \n
		Snippet: value: int = driver.configure.rfSettings.get_np_channel() \n
		Sets the channel number of the primary 20-MHz channel, for a signal with more than 20 MHz bandwidth. \n
			:return: np_20_channel: integer Range: 1 to 196
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:NPCHannel?')
		return Conversions.str_to_int(response)

	def set_np_channel(self, np_20_channel: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:NPCHannel \n
		Snippet: driver.configure.rfSettings.set_np_channel(np_20_channel = 1) \n
		Sets the channel number of the primary 20-MHz channel, for a signal with more than 20 MHz bandwidth. \n
			:param np_20_channel: integer Range: 1 to 196
		"""
		param = Conversions.decimal_value_to_str(np_20_channel)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:NPCHannel {param}')

	def get_ml_offset(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:MLOFfset \n
		Snippet: value: int = driver.configure.rfSettings.get_ml_offset() \n
		No command help available \n
			:return: value: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:MLOFfset?')
		return Conversions.str_to_int(response)

	def set_ml_offset(self, value: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:MLOFfset \n
		Snippet: driver.configure.rfSettings.set_ml_offset(value = 1) \n
		No command help available \n
			:param value: No help available
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:MLOFfset {param}')

	def get_epe_power(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:EPEPower \n
		Snippet: value: float or bool = driver.configure.rfSettings.get_epe_power() \n
		No command help available \n
			:return: expected_peak_envelop_power: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:EPEPower?')
		return Conversions.str_to_float_or_bool(response)

	def set_epe_power(self, expected_peak_envelop_power: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:EPEPower \n
		Snippet: driver.configure.rfSettings.set_epe_power(expected_peak_envelop_power = 1.0) \n
		No command help available \n
			:param expected_peak_envelop_power: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(expected_peak_envelop_power)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:EPEPower {param}')

	def get_ts_ratio(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:TSRatio \n
		Snippet: value: float = driver.configure.rfSettings.get_ts_ratio() \n
		Sets the power ratio of TX2 to TX1 for the MIMO scenario. \n
			:return: ratio: numeric TX2/TX1 Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:TSRatio?')
		return Conversions.str_to_float(response)

	def set_ts_ratio(self, ratio: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:TSRatio \n
		Snippet: driver.configure.rfSettings.set_ts_ratio(ratio = 1.0) \n
		Sets the power ratio of TX2 to TX1 for the MIMO scenario. \n
			:param ratio: numeric TX2/TX1 Unit: dB
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:TSRatio {param}')

	def get_bo_power(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:BOPower \n
		Snippet: value: float = driver.configure.rfSettings.get_bo_power() \n
		Sets the burst power of the transmitted signal. The allowed value range depends on the used connector and the external
		attenuation in the output path. Minimum = levelconnector, min - ext. att.out Maximum = levelconnector, max - ext. att.out
		With levelconnector, min = -145.98 dBm (-137.98 dBm) , levelconnector, max = -15.98 dBm (-2.98 dBm) for RF COM (RF OUT) ;
		please also notice the ranges quoted in the data sheet. \n
			:return: burst_output_pow: numeric Range: see above , Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:RFSettings:BOPower?')
		return Conversions.str_to_float(response)

	def set_bo_power(self, burst_output_pow: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:BOPower \n
		Snippet: driver.configure.rfSettings.set_bo_power(burst_output_pow = 1.0) \n
		Sets the burst power of the transmitted signal. The allowed value range depends on the used connector and the external
		attenuation in the output path. Minimum = levelconnector, min - ext. att.out Maximum = levelconnector, max - ext. att.out
		With levelconnector, min = -145.98 dBm (-137.98 dBm) , levelconnector, max = -15.98 dBm (-2.98 dBm) for RF COM (RF OUT) ;
		please also notice the ranges quoted in the data sheet. \n
			:param burst_output_pow: numeric Range: see above , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(burst_output_pow)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:BOPower {param}')

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
