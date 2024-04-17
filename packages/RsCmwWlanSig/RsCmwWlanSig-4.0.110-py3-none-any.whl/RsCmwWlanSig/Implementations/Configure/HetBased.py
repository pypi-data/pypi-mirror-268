from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HetBasedCls:
	"""HetBased commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hetBased", core, parent)

	def get_frames(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:HETBased:FRAMes \n
		Snippet: value: int = driver.configure.hetBased.get_frames() \n
		Sets the number of frames for HE TB list mode measurements. This setting determines the statistic count of the
		measurement. \n
			:return: no_of_frames: integer Range: 1 to 2000
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:HETBased:FRAMes?')
		return Conversions.str_to_int(response)

	def set_frames(self, no_of_frames: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:HETBased:FRAMes \n
		Snippet: driver.configure.hetBased.set_frames(no_of_frames = 1) \n
		Sets the number of frames for HE TB list mode measurements. This setting determines the statistic count of the
		measurement. \n
			:param no_of_frames: integer Range: 1 to 2000
		"""
		param = Conversions.decimal_value_to_str(no_of_frames)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:HETBased:FRAMes {param}')
