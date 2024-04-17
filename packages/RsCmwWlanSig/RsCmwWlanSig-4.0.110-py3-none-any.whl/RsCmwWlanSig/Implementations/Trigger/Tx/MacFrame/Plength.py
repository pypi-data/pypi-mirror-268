from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlengthCls:
	"""Plength commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PulseLengthMode:
		"""SCPI: TRIGger:WLAN:SIGNaling<instance>:TX:MACFrame:PLENgth:MODE \n
		Snippet: value: enums.PulseLengthMode = driver.trigger.tx.macFrame.plength.get_mode() \n
		Configures the length of generated TX MAC frame trigger pulses. \n
			:return: pulse_length_mode: DEFault | BLENgth | UDEFined DEFault The pulse length is 1 µs. BLENgth The pulse length equals the burst length. UDEFined The pulse length is specified via method RsCmwWlanSig.Trigger.Tx.MacFrame.Plength.value.
		"""
		response = self._core.io.query_str('TRIGger:WLAN:SIGNaling<Instance>:TX:MACFrame:PLENgth:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PulseLengthMode)

	def set_mode(self, pulse_length_mode: enums.PulseLengthMode) -> None:
		"""SCPI: TRIGger:WLAN:SIGNaling<instance>:TX:MACFrame:PLENgth:MODE \n
		Snippet: driver.trigger.tx.macFrame.plength.set_mode(pulse_length_mode = enums.PulseLengthMode.BLENgth) \n
		Configures the length of generated TX MAC frame trigger pulses. \n
			:param pulse_length_mode: DEFault | BLENgth | UDEFined DEFault The pulse length is 1 µs. BLENgth The pulse length equals the burst length. UDEFined The pulse length is specified via method RsCmwWlanSig.Trigger.Tx.MacFrame.Plength.value.
		"""
		param = Conversions.enum_scalar_to_str(pulse_length_mode, enums.PulseLengthMode)
		self._core.io.write(f'TRIGger:WLAN:SIGNaling<Instance>:TX:MACFrame:PLENgth:MODE {param}')

	def get_value(self) -> float or bool:
		"""SCPI: TRIGger:WLAN:SIGNaling<instance>:TX:MACFrame:PLENgth:VALue \n
		Snippet: value: float or bool = driver.trigger.tx.macFrame.plength.get_value() \n
		Sets the pulse length for the mode UDEFined of the TX frame trigger, see method RsCmwWlanSig.Trigger.Tx.MacFrame.Plength.
		mode. \n
			:return: pulse_length_val: (float or boolean) numeric | ON | OFF Range: 1E-6 s to 0.01 s
		"""
		response = self._core.io.query_str('TRIGger:WLAN:SIGNaling<Instance>:TX:MACFrame:PLENgth:VALue?')
		return Conversions.str_to_float_or_bool(response)

	def set_value(self, pulse_length_val: float or bool) -> None:
		"""SCPI: TRIGger:WLAN:SIGNaling<instance>:TX:MACFrame:PLENgth:VALue \n
		Snippet: driver.trigger.tx.macFrame.plength.set_value(pulse_length_val = 1.0) \n
		Sets the pulse length for the mode UDEFined of the TX frame trigger, see method RsCmwWlanSig.Trigger.Tx.MacFrame.Plength.
		mode. \n
			:param pulse_length_val: (float or boolean) numeric | ON | OFF Range: 1E-6 s to 0.01 s
		"""
		param = Conversions.decimal_or_bool_value_to_str(pulse_length_val)
		self._core.io.write(f'TRIGger:WLAN:SIGNaling<Instance>:TX:MACFrame:PLENgth:VALue {param}')
