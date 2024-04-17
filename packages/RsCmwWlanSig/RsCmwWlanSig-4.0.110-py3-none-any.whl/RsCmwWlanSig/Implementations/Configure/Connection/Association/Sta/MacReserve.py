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
class MacReserveCls:
	"""MacReserve commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("macReserve", core, parent)

	def set(self, reservation: enums.Reservation, address: str = None, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:ASSociation:STA<s>:MACReserve \n
		Snippet: driver.configure.connection.association.sta.macReserve.set(reservation = enums.Reservation.ANY, address = 'abc', station = repcap.Station.Default) \n
		Configures three slots available for STAs, if method RsCmwWlanSig.Configure.Connection.mstation is set to ON \n
			:param reservation: ANY | SET | OFF ANY - the slot is available to a STA of any MAC address SET - reserves the slot for a particular MAC address OFF - the slot is disabled
			:param address: string MAC address of the DUT for Reservation = SET
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('reservation', reservation, DataType.Enum, enums.Reservation), ArgSingle('address', address, DataType.String, None, is_optional=True))
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:ASSociation:STA{station_cmd_val}:MACReserve {param}'.rstrip())

	# noinspection PyTypeChecker
	class MacReserveStruct(StructBase):
		"""Response structure. Fields: \n
			- Reservation: enums.Reservation: ANY | SET | OFF ANY - the slot is available to a STA of any MAC address SET - reserves the slot for a particular MAC address OFF - the slot is disabled
			- Address: str: string MAC address of the DUT for Reservation = SET"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Reservation', enums.Reservation),
			ArgStruct.scalar_str('Address')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reservation: enums.Reservation = None
			self.Address: str = None

	def get(self, station=repcap.Station.Default) -> MacReserveStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:ASSociation:STA<s>:MACReserve \n
		Snippet: value: MacReserveStruct = driver.configure.connection.association.sta.macReserve.get(station = repcap.Station.Default) \n
		Configures three slots available for STAs, if method RsCmwWlanSig.Configure.Connection.mstation is set to ON \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for MacReserveStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:ASSociation:STA{station_cmd_val}:MACReserve?', self.__class__.MacReserveStruct())
