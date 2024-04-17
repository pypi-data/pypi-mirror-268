from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CtypeCls:
	"""Ctype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctype", core, parent)

	def set(self, coding_type: enums.CodingType, user=repcap.User.Default) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DFRame:HEMU:USER<index>:CTYPe \n
		Snippet: driver.configure.per.dframe.hemu.user.ctype.set(coding_type = enums.CodingType.BCC, user = repcap.User.Default) \n
		Selects the coding type related to a user for HE MU PPDU. \n
			:param coding_type: LDPC | BCC
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(coding_type, enums.CodingType)
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DFRame:HEMU:USER{user_cmd_val}:CTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, user=repcap.User.Default) -> enums.CodingType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:PER:DFRame:HEMU:USER<index>:CTYPe \n
		Snippet: value: enums.CodingType = driver.configure.per.dframe.hemu.user.ctype.get(user = repcap.User.Default) \n
		Selects the coding type related to a user for HE MU PPDU. \n
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: coding_type: LDPC | BCC"""
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		response = self._core.io.query_str(f'CONFigure:WLAN:SIGNaling<Instance>:PER:DFRame:HEMU:USER{user_cmd_val}:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.CodingType)
