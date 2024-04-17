from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IlossCls:
	"""Iloss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iloss", core, parent)

	def get_loss(self) -> float:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:FADing:FSIMulator:ILOSs:LOSS \n
		Snippet: value: float = driver.configure.fading.fsimulator.iloss.get_loss() \n
		Sets the insertion loss for the fading simulator. \n
			:return: insertion_loss: float Range: -3.02 dB to 30 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:LOSS?')
		return Conversions.str_to_float(response)
