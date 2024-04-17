from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpePowerCls:
	"""EpePower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("epePower", core, parent)

	def set(self, expected_peak_envelop_power: float or bool, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:ANTenna<n>:EPEPower \n
		Snippet: driver.configure.rfSettings.antenna.epePower.set(expected_peak_envelop_power = 1.0, antenna = repcap.Antenna.Default) \n
		Specifies the expected peak envelope power of the specified antenna at the I/Q input. Antenna 2 is only available in MIMO
		scenarios with two input paths. The correct DUT range to be set is (-20 dBm + external attenuation) to (55 dBm + external
		attenuation) . \n
			:param expected_peak_envelop_power: (float or boolean) No help available
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = Conversions.decimal_or_bool_value_to_str(expected_peak_envelop_power)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:ANTenna{antenna_cmd_val}:EPEPower {param}')

	def get(self, antenna=repcap.Antenna.Default) -> float or bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:ANTenna<n>:EPEPower \n
		Snippet: value: float or bool = driver.configure.rfSettings.antenna.epePower.get(antenna = repcap.Antenna.Default) \n
		Specifies the expected peak envelope power of the specified antenna at the I/Q input. Antenna 2 is only available in MIMO
		scenarios with two input paths. The correct DUT range to be set is (-20 dBm + external attenuation) to (55 dBm + external
		attenuation) . \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: expected_peak_envelop_power: (float or boolean) No help available"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:ANTenna{antenna_cmd_val}:EPEPower?')
		return Conversions.str_to_float_or_bool(response)
