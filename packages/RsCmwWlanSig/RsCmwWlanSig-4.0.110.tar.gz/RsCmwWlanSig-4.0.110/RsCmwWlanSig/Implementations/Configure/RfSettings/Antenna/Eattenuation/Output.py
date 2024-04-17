from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OutputCls:
	"""Output commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	def set(self, ext_attenuation: float, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:ANTenna<n>:EATTenuation:OUTPut \n
		Snippet: driver.configure.rfSettings.antenna.eattenuation.output.set(ext_attenuation = 1.0, antenna = repcap.Antenna.Default) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the individual antennas. Antenna 2
		is only available in a MIMO scenario. \n
			:param ext_attenuation: numeric Range: -50 dB to 90 dB, Unit: dB
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = Conversions.decimal_value_to_str(ext_attenuation)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:ANTenna{antenna_cmd_val}:EATTenuation:OUTPut {param}')

	def get(self, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:ANTenna<n>:EATTenuation:OUTPut \n
		Snippet: value: float = driver.configure.rfSettings.antenna.eattenuation.output.get(antenna = repcap.Antenna.Default) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the individual antennas. Antenna 2
		is only available in a MIMO scenario. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: ext_attenuation: numeric Range: -50 dB to 90 dB, Unit: dB"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:ANTenna{antenna_cmd_val}:EATTenuation:OUTPut?')
		return Conversions.str_to_float(response)
