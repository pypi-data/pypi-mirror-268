from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlmnCls:
	"""Plmn commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Plnm, default value after init: Plnm.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plmn", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_plnm_get', 'repcap_plnm_set', repcap.Plnm.Nr1)

	def repcap_plnm_set(self, plnm: repcap.Plnm) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Plnm.Default
		Default value after init: Plnm.Nr1"""
		self._cmd_group.set_repcap_enum_value(plnm)

	def repcap_plnm_get(self) -> repcap.Plnm:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, state: bool, mcc: int, mnc: int, num_of_digits: enums.NumOfDigits, plnm=repcap.Plnm.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HOTSpot:PLMN<nr> \n
		Snippet: driver.configure.connection.hotspot.plmn.set(state = False, mcc = 1, mnc = 1, num_of_digits = enums.NumOfDigits.THDigits, plnm = repcap.Plnm.Default) \n
		Defines a list of 3GPP networks that the hotspot provides service for. The MCC and MNC of the first PLMN can also be
		defined via method RsCmwWlanSig.Configure.Connection.Hotspot.hspar. \n
			:param state: OFF | ON Disables/enables the list entry
			:param mcc: integer Mobile country code Range: 1 to 999
			:param mnc: integer Mobile network code Range: Depends on NumOfDigits
			:param num_of_digits: TWDigits | THDigits Length of the MNC TWDigits: two digits (1 to 99) THDigits: three digits (1 to 999)
			:param plnm: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plmn')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('mcc', mcc, DataType.Integer), ArgSingle('mnc', mnc, DataType.Integer), ArgSingle('num_of_digits', num_of_digits, DataType.Enum, enums.NumOfDigits))
		plnm_cmd_val = self._cmd_group.get_repcap_cmd_value(plnm, repcap.Plnm)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HOTSpot:PLMN{plnm_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class PlmnStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: OFF | ON Disables/enables the list entry
			- Mcc: int: integer Mobile country code Range: 1 to 999
			- Mnc: int: integer Mobile network code Range: Depends on NumOfDigits
			- Num_Of_Digits: enums.NumOfDigits: TWDigits | THDigits Length of the MNC TWDigits: two digits (1 to 99) THDigits: three digits (1 to 999)"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_int('Mcc'),
			ArgStruct.scalar_int('Mnc'),
			ArgStruct.scalar_enum('Num_Of_Digits', enums.NumOfDigits)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Mcc: int = None
			self.Mnc: int = None
			self.Num_Of_Digits: enums.NumOfDigits = None

	def get(self, plnm=repcap.Plnm.Default) -> PlmnStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:HOTSpot:PLMN<nr> \n
		Snippet: value: PlmnStruct = driver.configure.connection.hotspot.plmn.get(plnm = repcap.Plnm.Default) \n
		Defines a list of 3GPP networks that the hotspot provides service for. The MCC and MNC of the first PLMN can also be
		defined via method RsCmwWlanSig.Configure.Connection.Hotspot.hspar. \n
			:param plnm: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plmn')
			:return: structure: for return value, see the help for PlmnStruct structure arguments."""
		plnm_cmd_val = self._cmd_group.get_repcap_cmd_value(plnm, repcap.Plnm)
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:HOTSpot:PLMN{plnm_cmd_val}?', self.__class__.PlmnStruct())

	def clone(self) -> 'PlmnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlmnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
