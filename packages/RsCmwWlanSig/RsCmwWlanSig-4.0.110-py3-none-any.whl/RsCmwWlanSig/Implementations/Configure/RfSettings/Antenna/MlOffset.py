from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MlOffsetCls:
	"""MlOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mlOffset", core, parent)

	def set(self, value: int, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:ANTenna<n>:MLOFfset \n
		Snippet: driver.configure.rfSettings.antenna.mlOffset.set(value = 1, antenna = repcap.Antenna.Default) \n
		Varies the input level of the mixer for the specified antenna in the analyzer path. Antenna 2 is only available in MIMO
		scenarios with two input paths. \n
			:param value: integer Range: -10 dB to 12dB , Unit: dB
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = Conversions.decimal_value_to_str(value)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:ANTenna{antenna_cmd_val}:MLOFfset {param}')

	def get(self, antenna=repcap.Antenna.Default) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:RFSettings:ANTenna<n>:MLOFfset \n
		Snippet: value: int = driver.configure.rfSettings.antenna.mlOffset.get(antenna = repcap.Antenna.Default) \n
		Varies the input level of the mixer for the specified antenna in the analyzer path. Antenna 2 is only available in MIMO
		scenarios with two input paths. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: value: integer Range: -10 dB to 12dB , Unit: dB"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:RFSettings:ANTenna{antenna_cmd_val}:MLOFfset?')
		return Conversions.str_to_int(response)
