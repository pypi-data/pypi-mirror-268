from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SinfoCls:
	"""Sinfo commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import AntennaCls
			self._antenna = AntennaCls(self._core, self._cmd_group)
		return self._antenna

	# noinspection PyTypeChecker
	class EapStatStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- State: enums.ResultState: IDLE | SUCCess | FAILure EAP connection state
			- Type_Py: enums.AuthType: IDENtity | NOTification | NAK | MD5 | OTP | GTC | TLS | CLEap | SIM | TTLS | AKA | AKAPrime Authentication stage"""
		__meta_args_list = [
			ArgStruct.scalar_enum('State', enums.ResultState),
			ArgStruct.scalar_enum('Type_Py', enums.AuthType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: enums.ResultState = None
			self.Type_Py: enums.AuthType = None

	def get_eap_stat(self) -> EapStatStruct:
		"""SCPI: SENSe:WLAN:SIGNaling<instance>:SINFo:EAPStat \n
		Snippet: value: EapStatStruct = driver.sense.sinfo.get_eap_stat() \n
		Queries the current state of the EAP connection for the security mode 'WPA / WPA2 Enterprise'. \n
			:return: structure: for return value, see the help for EapStatStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WLAN:SIGNaling<Instance>:SINFo:EAPStat?', self.__class__.EapStatStruct())

	def clone(self) -> 'SinfoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SinfoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
