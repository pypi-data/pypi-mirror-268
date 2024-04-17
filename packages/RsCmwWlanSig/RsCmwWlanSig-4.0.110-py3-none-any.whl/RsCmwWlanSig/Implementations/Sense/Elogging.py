from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EloggingCls:
	"""Elogging commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("elogging", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Category: List[enums.LogCategoryB]: INFO | WARNing | ERRor | EMPTy Category of the entry, as indicated in the main view by an icon EMPTy means that there are no entries.
			- Timestamp: List[str]: string Timestamp of the entry as string in the format 'hh:mm:ss'
			- Description: List[str]: string Text string describing the event"""
		__meta_args_list = [
			ArgStruct('Category', DataType.EnumList, enums.LogCategoryB, False, True, 1),
			ArgStruct('Timestamp', DataType.StringList, None, False, True, 1),
			ArgStruct('Description', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Category: List[enums.LogCategoryB] = None
			self.Timestamp: List[str] = None
			self.Description: List[str] = None

	def get_all(self) -> AllStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:ELOGging:ALL \n
		Snippet: value: AllStruct = driver.sense.elogging.get_all() \n
		Queries all entries of the event log. For each entry, three parameters are returned, from oldest to latest entry:
		{<Category>, <Timestamp>, <Description>}entry 1, {<Category>, <Timestamp>, <Description>}entry 2, ... \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WLAN:SIGNaling<Instance>:ELOGging:ALL?', self.__class__.AllStruct())
