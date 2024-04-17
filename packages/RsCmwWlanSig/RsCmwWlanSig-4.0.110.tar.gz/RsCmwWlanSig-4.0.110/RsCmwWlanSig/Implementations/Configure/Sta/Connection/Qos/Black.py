from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlackCls:
	"""Black commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("black", core, parent)

	# noinspection PyTypeChecker
	class BlackStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Tid_0: bool: No parameter help available
			- Tid_1: bool: No parameter help available
			- Tid_2: bool: No parameter help available
			- Tid_3: bool: No parameter help available
			- Tid_4: bool: No parameter help available
			- Tid_5: bool: No parameter help available
			- Tid_6: bool: No parameter help available
			- Tid_7: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Tid_0'),
			ArgStruct.scalar_bool('Tid_1'),
			ArgStruct.scalar_bool('Tid_2'),
			ArgStruct.scalar_bool('Tid_3'),
			ArgStruct.scalar_bool('Tid_4'),
			ArgStruct.scalar_bool('Tid_5'),
			ArgStruct.scalar_bool('Tid_6'),
			ArgStruct.scalar_bool('Tid_7')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tid_0: bool = None
			self.Tid_1: bool = None
			self.Tid_2: bool = None
			self.Tid_3: bool = None
			self.Tid_4: bool = None
			self.Tid_5: bool = None
			self.Tid_6: bool = None
			self.Tid_7: bool = None

	def set(self, structure: BlackStruct, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:QOS:BLACk \n
		Snippet with structure: \n
		structure = driver.configure.sta.connection.qos.black.BlackStruct() \n
		structure.Tid_0: bool = False \n
		structure.Tid_1: bool = False \n
		structure.Tid_2: bool = False \n
		structure.Tid_3: bool = False \n
		structure.Tid_4: bool = False \n
		structure.Tid_5: bool = False \n
		structure.Tid_6: bool = False \n
		structure.Tid_7: bool = False \n
		driver.configure.sta.connection.qos.black.set(structure, station = repcap.Station.Default) \n
		Enables/ disables a block ack session per TID (8 values) . \n
			:param structure: for set value, see the help for BlackStruct structure arguments.
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write_struct(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:QOS:BLACk', structure)

	def get(self, station=repcap.Station.Default) -> BlackStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:STA<s>:CONNection:QOS:BLACk \n
		Snippet: value: BlackStruct = driver.configure.sta.connection.qos.black.get(station = repcap.Station.Default) \n
		Enables/ disables a block ack session per TID (8 values) . \n
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: structure: for return value, see the help for BlackStruct structure arguments."""
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:STA{station_cmd_val}:CONNection:QOS:BLACk?', self.__class__.BlackStruct())
