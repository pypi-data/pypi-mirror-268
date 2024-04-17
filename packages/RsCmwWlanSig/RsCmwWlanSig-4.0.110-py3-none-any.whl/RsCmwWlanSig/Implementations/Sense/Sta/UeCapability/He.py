from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HeCls:
	"""He commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("he", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Device_Class: enums.DeviceClass: A | B
			- Dyn_Fragment: enums.DynFragment: NO | L1 | L2 | L3 Dynamic fragmentation not supported, or dynamic fragmentation supported with level 1 to 3.
			- Absr: enums.YesNoStatus: NO | YES Indicates support of a buffer status report (BSR) control field.
			- Broadcast_Twt: enums.YesNoStatus: NO | YES Indicates support of broadcast target wake time (TWT) operation.
			- Ofdma_Rand_Acc: enums.YesNoStatus: NO | YES Indicates support of OFDMA random access procedure."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Device_Class', enums.DeviceClass),
			ArgStruct.scalar_enum('Dyn_Fragment', enums.DynFragment),
			ArgStruct.scalar_enum('Absr', enums.YesNoStatus),
			ArgStruct.scalar_enum('Broadcast_Twt', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ofdma_Rand_Acc', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Device_Class: enums.DeviceClass = None
			self.Dyn_Fragment: enums.DynFragment = None
			self.Absr: enums.YesNoStatus = None
			self.Broadcast_Twt: enums.YesNoStatus = None
			self.Ofdma_Rand_Acc: enums.YesNoStatus = None

	def get(self, station=repcap.Station.Default) -> GetStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:STA<s>:UECapability:HE \n
		Snippet: value: GetStruct = driver.sense.sta.ueCapability.he.get(station = repcap.Station.Default) \n
		Indicates the reported UE HE capabilities. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'SENSe:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:UECapability:HE?', self.__class__.GetStruct())
