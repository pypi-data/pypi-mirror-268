from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RualCls:
	"""Rual commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rual", core, parent)

	def set(self, ru_allocation: enums.RuAllocation, channel_80_mh_z: enums.Channel80MhZ = None, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:RUAL \n
		Snippet: driver.configure.sta.connection.hetf.rual.set(ru_allocation = enums.RuAllocation.OFF, channel_80_mh_z = enums.Channel80MhZ.PRIMary, station = repcap.Station.Default) \n
		Specifies the RU used by the HE TB PPDU. Refer to IEEE Std 802.11ax-2021, table 9-29i B7–B1 of the RU Allocation subfield. \n
			:param ru_allocation: RU0 | RU1 | RU2 | RU3 | RU4 | RU5 | RU6 | RU7 | RU8 | RU9 | RU10 | RU11 | RU12 | RU13 | RU14 | RU15 | RU16 | RU17 | RU18 | RU19 | RU20 | RU21 | RU22 | RU23 | RU24 | RU25 | RU26 | RU27 | RU28 | RU29 | RU30 | RU31 | RU32 | RU33 | RU34 | RU35 | RU36 | RU37 | RU38 | RU39 | RU40 | RU41 | RU42 | RU43 | RU44 | RU45 | RU46 | RU47 | RU48 | RU49 | RU50 | RU51 | RU52 | RU53 | RU54 | RU55 | RU56 | RU57 | RU58 | RU59 | RU60 | RU61 | RU62 | RU63 | RU64 | RU65 | RU66 | RU67 | RU68 | OFF 'OFF': No resource unit for the specified station is allocated 'RUx': Bits 7 to 1 of the RU allocation subfield, see table below.
			:param channel_80_mh_z: PRIMary | SECondary For RU67 and RU68 applying 160 MHz channel, sets the bit 0 of the RU allocation subfield that indicates primary 80 MHz or secondary 80 MHz channel.
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ru_allocation', ru_allocation, DataType.Enum, enums.RuAllocation), ArgSingle('channel_80_mh_z', channel_80_mh_z, DataType.Enum, enums.Channel80MhZ, is_optional=True))
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:RUAL {param}'.rstrip())

	# noinspection PyTypeChecker
	class RualStruct(StructBase):
		"""Response structure. Fields: \n
			- Ru_Allocation: enums.RuAllocation: RU0 | RU1 | RU2 | RU3 | RU4 | RU5 | RU6 | RU7 | RU8 | RU9 | RU10 | RU11 | RU12 | RU13 | RU14 | RU15 | RU16 | RU17 | RU18 | RU19 | RU20 | RU21 | RU22 | RU23 | RU24 | RU25 | RU26 | RU27 | RU28 | RU29 | RU30 | RU31 | RU32 | RU33 | RU34 | RU35 | RU36 | RU37 | RU38 | RU39 | RU40 | RU41 | RU42 | RU43 | RU44 | RU45 | RU46 | RU47 | RU48 | RU49 | RU50 | RU51 | RU52 | RU53 | RU54 | RU55 | RU56 | RU57 | RU58 | RU59 | RU60 | RU61 | RU62 | RU63 | RU64 | RU65 | RU66 | RU67 | RU68 | OFF 'OFF': No resource unit for the specified station is allocated 'RUx': Bits 7 to 1 of the RU allocation subfield, see table below.
			- Channel_80_Mh_Z: enums.Channel80MhZ: PRIMary | SECondary For RU67 and RU68 applying 160 MHz channel, sets the bit 0 of the RU allocation subfield that indicates primary 80 MHz or secondary 80 MHz channel."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ru_Allocation', enums.RuAllocation),
			ArgStruct.scalar_enum('Channel_80_Mh_Z', enums.Channel80MhZ)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ru_Allocation: enums.RuAllocation = None
			self.Channel_80_Mh_Z: enums.Channel80MhZ = None

	def get(self, station=repcap.Station.Default) -> RualStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:HETF:RUAL \n
		Snippet: value: RualStruct = driver.configure.sta.connection.hetf.rual.get(station = repcap.Station.Default) \n
		Specifies the RU used by the HE TB PPDU. Refer to IEEE Std 802.11ax-2021, table 9-29i B7–B1 of the RU Allocation subfield. \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for RualStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:HETF:RUAL?', self.__class__.RualStruct())
