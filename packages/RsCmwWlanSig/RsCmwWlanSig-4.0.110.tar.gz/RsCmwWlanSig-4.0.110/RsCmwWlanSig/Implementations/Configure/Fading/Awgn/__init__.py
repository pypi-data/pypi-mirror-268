from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AwgnCls:
	"""Awgn commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("awgn", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:AWGN:ENABle \n
		Snippet: value: bool = driver.configure.fading.awgn.get_enable() \n
		Enables or disables AWGN insertion via the fading module. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:FADing:AWGN:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:AWGN:ENABle \n
		Snippet: driver.configure.fading.awgn.set_enable(enable = False) \n
		Enables or disables AWGN insertion via the fading module. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:FADing:AWGN:ENABle {param}')

	def get_sn_ratio(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:AWGN:SNRatio \n
		Snippet: value: float = driver.configure.fading.awgn.get_sn_ratio() \n
		Specifies the signal to noise ratio for the AWGN inserted on the internal fading module. \n
			:return: ratio: numeric Range: 0 dB to 40 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:FADing:AWGN:SNRatio?')
		return Conversions.str_to_float(response)

	def set_sn_ratio(self, ratio: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:AWGN:SNRatio \n
		Snippet: driver.configure.fading.awgn.set_sn_ratio(ratio = 1.0) \n
		Specifies the signal to noise ratio for the AWGN inserted on the internal fading module. \n
			:param ratio: numeric Range: 0 dB to 40 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:FADing:AWGN:SNRatio {param}')

	def clone(self) -> 'AwgnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AwgnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
