from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DnameCls:
	"""Dname commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: DomainName, default value after init: DomainName.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dname", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_domainName_get', 'repcap_domainName_set', repcap.DomainName.Nr1)

	def repcap_domainName_set(self, domainName: repcap.DomainName) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to DomainName.Default
		Default value after init: DomainName.Nr1"""
		self._cmd_group.set_repcap_enum_value(domainName)

	def repcap_domainName_get(self) -> repcap.DomainName:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, state: bool, name: str, domainName=repcap.DomainName.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HOTSpot:DNAMe<nr> \n
		Snippet: driver.configure.connection.hotspot.dname.set(state = False, name = 'abc', domainName = repcap.DomainName.Default) \n
		Defines a list of domain names of the entity operating the IEEE 802.11 access network. The first domain name can also be
		defined via method RsCmwWlanSig.Configure.Connection.Hotspot.hspar. \n
			:param state: OFF | ON Disables/enables the list entry
			:param name: string Domain name as string
			:param domainName: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dname')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('name', name, DataType.String))
		domainName_cmd_val = self._cmd_group.get_repcap_cmd_value(domainName, repcap.DomainName)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HOTSpot:DNAMe{domainName_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class DnameStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: OFF | ON Disables/enables the list entry
			- Name: str: string Domain name as string"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_str('Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Name: str = None

	def get(self, domainName=repcap.DomainName.Default) -> DnameStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HOTSpot:DNAMe<nr> \n
		Snippet: value: DnameStruct = driver.configure.connection.hotspot.dname.get(domainName = repcap.DomainName.Default) \n
		Defines a list of domain names of the entity operating the IEEE 802.11 access network. The first domain name can also be
		defined via method RsCmwWlanSig.Configure.Connection.Hotspot.hspar. \n
			:param domainName: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dname')
			:return: structure: for return value, see the help for DnameStruct structure arguments."""
		domainName_cmd_val = self._cmd_group.get_repcap_cmd_value(domainName, repcap.DomainName)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HOTSpot:DNAMe{domainName_cmd_val}?', self.__class__.DnameStruct())

	def clone(self) -> 'DnameCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DnameCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
