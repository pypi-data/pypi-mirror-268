from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from ..Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ..Internal.Types import DataType
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PackRateCls:
	"""PackRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("packRate", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.Coderate:
		"""SCPI: FETCh:WLAN:SIGNaling<instance>:PACKrate \n
		Snippet: value: enums.Coderate = driver.packRate.fetch() \n
		Returns the modulation and coding rate/scheme of the last received ACK frame. \n
		Use RsCmwWlanSig.reliability.last_value to read the updated reliability indicator. \n
			:return: rate: BR12 | QR12 | QR34 | Q1M12 | Q1M34 | Q6M23 | Q6M34 | BR34 | MCS | MCS1 | MCS2 | MCS3 | MCS4 | MCS5 | MCS6 | MCS7 | D1MBit | D2MBits | C55Mbits | C11Mbits | MCS8 | MCS9 | MCS10 | MCS11 | MCS12 | MCS13 | MCS14 | MCS15 See rate list in method RsCmwWlanSig.Configure.Connection.MfDef.set"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WLAN:SIGNaling<Instance>:PACKrate?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Coderate)
