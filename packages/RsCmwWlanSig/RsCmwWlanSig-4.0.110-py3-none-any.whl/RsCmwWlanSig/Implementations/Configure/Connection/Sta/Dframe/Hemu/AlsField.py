from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlsFieldCls:
	"""AlsField commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alsField", core, parent)

	def set(self, ch_20_index: enums.Ch20Index, subfield: enums.Subfield, station=repcap.Station.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:ALSField \n
		Snippet: driver.configure.connection.sta.dframe.hemu.alsField.set(ch_20_index = enums.Ch20Index.CHA1, subfield = enums.Subfield.A000, station = repcap.Station.Default) \n
		Sets 8-bit indices for resource unit (RU) allocation for the selected channel. The <Subfield> parameter specifies the
		number of RUs, their position and size. Refer to IEEE Std 802.11ax-2021, table 27-26, RU allocation subfield. \n
			:param ch_20_index: CHA1 | CHA2 | CHA3 | CHA4
			:param subfield: A000 | A001 | A002 | A003 | A004 | A005 | A006 | A007 | A008 | A009 | A010 | A011 | A012 | A013 | A014 | A015 | A016 | A024 | A032 | A040 | A048 | A056 | A064 | A072 | A080 | A088 | A096 | A112 | A113 | A114 | A115 | A116 | A120 | A128 | A192 | A200 | A208 | A216 | A224
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ch_20_index', ch_20_index, DataType.Enum, enums.Ch20Index), ArgSingle('subfield', subfield, DataType.Enum, enums.Subfield))
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:ALSField {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, ch_20_index: enums.Ch20Index, station=repcap.Station.Default) -> enums.Subfield:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STA<s>:DFRame:HEMU:ALSField \n
		Snippet: value: enums.Subfield = driver.configure.connection.sta.dframe.hemu.alsField.get(ch_20_index = enums.Ch20Index.CHA1, station = repcap.Station.Default) \n
		Sets 8-bit indices for resource unit (RU) allocation for the selected channel. The <Subfield> parameter specifies the
		number of RUs, their position and size. Refer to IEEE Std 802.11ax-2021, table 27-26, RU allocation subfield. \n
			:param ch_20_index: CHA1 | CHA2 | CHA3 | CHA4
			:param station: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sta')
			:return: subfield: A000 | A001 | A002 | A003 | A004 | A005 | A006 | A007 | A008 | A009 | A010 | A011 | A012 | A013 | A014 | A015 | A016 | A024 | A032 | A040 | A048 | A056 | A064 | A072 | A080 | A088 | A096 | A112 | A113 | A114 | A115 | A116 | A120 | A128 | A192 | A200 | A208 | A216 | A224"""
		param = Conversions.enum_scalar_to_str(ch_20_index, enums.Ch20Index)
		station_cmd_val = self._cmd_group.get_repcap_cmd_value(station, repcap.Station)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STA{station_cmd_val}:DFRame:HEMU:ALSField? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Subfield)
