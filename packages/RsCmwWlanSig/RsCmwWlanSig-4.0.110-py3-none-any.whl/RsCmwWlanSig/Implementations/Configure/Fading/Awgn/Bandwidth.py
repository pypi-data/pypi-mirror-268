from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def get_ratio(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:AWGN:BWIDth:RATio \n
		Snippet: value: float = driver.configure.fading.awgn.bandwidth.get_ratio() \n
		Specifies the minimum ratio between the noise bandwidth and the channel bandwidth. \n
			:return: ratio: numeric Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:FADing:AWGN:BWIDth:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:AWGN:BWIDth:RATio \n
		Snippet: driver.configure.fading.awgn.bandwidth.set_ratio(ratio = 1.0) \n
		Specifies the minimum ratio between the noise bandwidth and the channel bandwidth. \n
			:param ratio: numeric Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:FADing:AWGN:BWIDth:RATio {param}')
