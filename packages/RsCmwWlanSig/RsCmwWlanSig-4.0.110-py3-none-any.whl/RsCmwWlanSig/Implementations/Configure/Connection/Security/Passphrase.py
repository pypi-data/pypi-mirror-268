from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PassphraseCls:
	"""Passphrase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("passphrase", core, parent)

	def set(self, security_type: enums.SecurityType, passphrase: str = None) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:PASSphrase \n
		Snippet: driver.configure.connection.security.passphrase.set(security_type = enums.SecurityType.AUTO, passphrase = 'abc') \n
		Selects the WLAN security mechanism to be used and defines the passphrase for WPA/WPA2/WPA3 personal. For supported
		values depending on operation mode, see Table 'Supported security mechanisms'. \n
			:param security_type: DISabled | AUTO | WPERsonal | WENTerprise | W2Personal | W2ENterprise | OWE | W3Personal | W3ENterprise DISabled: no security (only for the 2.4 and 5 GHz bands) AUTO: automatic selection of any supported security type WPERsonal: WPA personal WENTerprise: WPA enterprise W2Personal: WPA2 personal W2ENterprise: WPA2 enterprise OWE: opportunistic wireless encryption with protected management frames (PMF) W3Personal: WPA3 personal W3ENterprise: WPA3 enterprise
			:param passphrase: string Passphrase for AP operation mode as a string, 1 to 63 characters
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('security_type', security_type, DataType.Enum, enums.SecurityType), ArgSingle('passphrase', passphrase, DataType.String, None, is_optional=True))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:PASSphrase {param}'.rstrip())

	# noinspection PyTypeChecker
	class PassphraseStruct(StructBase):
		"""Response structure. Fields: \n
			- Security_Type: enums.SecurityType: DISabled | AUTO | WPERsonal | WENTerprise | W2Personal | W2ENterprise | OWE | W3Personal | W3ENterprise DISabled: no security (only for the 2.4 and 5 GHz bands) AUTO: automatic selection of any supported security type WPERsonal: WPA personal WENTerprise: WPA enterprise W2Personal: WPA2 personal W2ENterprise: WPA2 enterprise OWE: opportunistic wireless encryption with protected management frames (PMF) W3Personal: WPA3 personal W3ENterprise: WPA3 enterprise
			- Passphrase: str: string Passphrase for AP operation mode as a string, 1 to 63 characters"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Security_Type', enums.SecurityType),
			ArgStruct.scalar_str('Passphrase')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Security_Type: enums.SecurityType = None
			self.Passphrase: str = None

	def get(self) -> PassphraseStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:PASSphrase \n
		Snippet: value: PassphraseStruct = driver.configure.connection.security.passphrase.get() \n
		Selects the WLAN security mechanism to be used and defines the passphrase for WPA/WPA2/WPA3 personal. For supported
		values depending on operation mode, see Table 'Supported security mechanisms'. \n
			:return: structure: for return value, see the help for PassphraseStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:PASSphrase?', self.__class__.PassphraseStruct())
