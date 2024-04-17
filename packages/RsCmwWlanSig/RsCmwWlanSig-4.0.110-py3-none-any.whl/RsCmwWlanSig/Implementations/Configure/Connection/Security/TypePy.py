from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, security_type: enums.SecurityType, end_part: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:TYPE \n
		Snippet: driver.configure.connection.security.typePy.set(security_type = enums.SecurityType.AUTO, end_part = 'abc') \n
		Selects the WLAN security mechanism to be used and defines the last character of the passphrase for WPA/WPA2/WPA3
		personal. For supported values depending on operation mode, see Table 'Supported security mechanisms'. \n
			:param security_type: DISabled | AUTO | WPERsonal | WENTerprise | W2Personal | W2ENterprise | OWE | W3Personal | W3ENterprise DISabled: no security (only for the 2.4 GHz and 5 GHz bands) AUTO: automatic selection of any supported security type (station mode only) WPERsonal: WPA personal (only for the 2.4 GHz and 5 GHz bands) WENTerprise: WPA enterprise (only for the 2.4 GHz and 5 GHz bands) W2Personal: WPA2 personal (only for the 2.4 GHz and 5 GHz bands) W2ENterprise: WPA2 enterprise (only for the 2.4 GHz and 5 GHz bands) OWE: opportunistic wireless encryption (only for 6 GHz band) W3Personal: WPA3 personal (all bands) W3ENterprise: WPA3 enterprise (all bands)
			:param end_part: string Last passphrase character as string
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('security_type', security_type, DataType.Enum, enums.SecurityType), ArgSingle('end_part', end_part, DataType.String))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:TYPE {param}'.rstrip())

	# noinspection PyTypeChecker
	class TypePyStruct(StructBase):
		"""Response structure. Fields: \n
			- Security_Type: enums.SecurityType: DISabled | AUTO | WPERsonal | WENTerprise | W2Personal | W2ENterprise | OWE | W3Personal | W3ENterprise DISabled: no security (only for the 2.4 GHz and 5 GHz bands) AUTO: automatic selection of any supported security type (station mode only) WPERsonal: WPA personal (only for the 2.4 GHz and 5 GHz bands) WENTerprise: WPA enterprise (only for the 2.4 GHz and 5 GHz bands) W2Personal: WPA2 personal (only for the 2.4 GHz and 5 GHz bands) W2ENterprise: WPA2 enterprise (only for the 2.4 GHz and 5 GHz bands) OWE: opportunistic wireless encryption (only for 6 GHz band) W3Personal: WPA3 personal (all bands) W3ENterprise: WPA3 enterprise (all bands)
			- End_Part: str: string Last passphrase character as string"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Security_Type', enums.SecurityType),
			ArgStruct.scalar_str('End_Part')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Security_Type: enums.SecurityType = None
			self.End_Part: str = None

	def get(self) -> TypePyStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:TYPE \n
		Snippet: value: TypePyStruct = driver.configure.connection.security.typePy.get() \n
		Selects the WLAN security mechanism to be used and defines the last character of the passphrase for WPA/WPA2/WPA3
		personal. For supported values depending on operation mode, see Table 'Supported security mechanisms'. \n
			:return: structure: for return value, see the help for TypePyStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:TYPE?', self.__class__.TypePyStruct())
