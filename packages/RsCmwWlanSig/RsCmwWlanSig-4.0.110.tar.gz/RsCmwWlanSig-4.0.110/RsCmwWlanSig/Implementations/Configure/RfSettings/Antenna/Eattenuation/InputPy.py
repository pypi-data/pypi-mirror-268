from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPyCls:
	"""InputPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	def set(self, ext_attenuation: float, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:ANTenna<n>:EATTenuation:INPut \n
		Snippet: driver.configure.rfSettings.antenna.eattenuation.inputPy.set(ext_attenuation = 1.0, antenna = repcap.Antenna.Default) \n
		Specifies the external attenuation for the specified antenna in the analyzer path. Antenna 2 is only available in a MIMO
		scenario with two input paths. \n
			:param ext_attenuation: numeric Range: -50 dB to 55 dB, Unit: dB
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = Conversions.decimal_value_to_str(ext_attenuation)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:ANTenna{antenna_cmd_val}:EATTenuation:INPut {param}')

	def get(self, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:ANTenna<n>:EATTenuation:INPut \n
		Snippet: value: float = driver.configure.rfSettings.antenna.eattenuation.inputPy.get(antenna = repcap.Antenna.Default) \n
		Specifies the external attenuation for the specified antenna in the analyzer path. Antenna 2 is only available in a MIMO
		scenario with two input paths. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: ext_attenuation: numeric Range: -50 dB to 55 dB, Unit: dB"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:ANTenna{antenna_cmd_val}:EATTenuation:INPut?')
		return Conversions.str_to_float(response)
