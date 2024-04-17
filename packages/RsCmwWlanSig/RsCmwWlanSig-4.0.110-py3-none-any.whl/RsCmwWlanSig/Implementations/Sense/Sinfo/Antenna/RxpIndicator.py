from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxpIndicatorCls:
	"""RxpIndicator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rxpIndicator", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Power_Value: float: float Unit: dBm
			- Power_Indicator: enums.PowerIndicator: UNDerdriven | RANGe | OVERdriven"""
		__meta_args_list = [
			ArgStruct.scalar_float('Power_Value'),
			ArgStruct.scalar_enum('Power_Indicator', enums.PowerIndicator)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Power_Value: float = None
			self.Power_Indicator: enums.PowerIndicator = None

	def get(self, antenna=repcap.Antenna.Default) -> GetStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:SINFo[:ANTenna<n>]:RXPindicator \n
		Snippet: value: GetStruct = driver.sense.sinfo.antenna.rxpIndicator.get(antenna = repcap.Antenna.Default) \n
		Queries the Rx burst power per individual antenna and evaluates the quality of the RX signal from the connected DUT.
		Antenna 2 is only available in a MIMO scenario. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		return self._core.io.query_struct(f'SENSe:WLAN:SIGNaling<Instance>:SINFo:ANTenna{antenna_cmd_val}:RXPindicator?', self.__class__.GetStruct())
