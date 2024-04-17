from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SecurityCls:
	"""Security commands group definition. 15 total commands, 6 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("security", core, parent)

	@property
	def eaka(self):
		"""eaka commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eaka'):
			from .Eaka import EakaCls
			self._eaka = EakaCls(self._core, self._cmd_group)
		return self._eaka

	@property
	def esim(self):
		"""esim commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_esim'):
			from .Esim import EsimCls
			self._esim = EsimCls(self._core, self._cmd_group)
		return self._esim

	@property
	def rserver(self):
		"""rserver commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_rserver'):
			from .Rserver import RserverCls
			self._rserver = RserverCls(self._core, self._cmd_group)
		return self._rserver

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	@property
	def passphrase(self):
		"""passphrase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_passphrase'):
			from .Passphrase import PassphraseCls
			self._passphrase = PassphraseCls(self._core, self._cmd_group)
		return self._passphrase

	@property
	def pkey(self):
		"""pkey commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pkey'):
			from .Pkey import PkeyCls
			self._pkey = PkeyCls(self._core, self._cmd_group)
		return self._pkey

	# noinspection PyTypeChecker
	def get_encryption(self) -> enums.EncryptionType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:ENCRyption \n
		Snippet: value: enums.EncryptionType = driver.configure.connection.security.get_encryption() \n
		Sets the encryption type for AP operation mode, if WPA, WPA2, or WPA3 personal security mode is selected. \n
			:return: encryption_type: AES | TKIP | DISabled | GCMP AES: AES basd CCMP-128 with PSK (for WPA2) TKIP: TKIP with PSK (for WPA) DISabled: encryption not used GCMP: CCMP-128 with SAE and PMF (WPA3)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:ENCRyption?')
		return Conversions.str_to_scalar_enum(response, enums.EncryptionType)

	def set_encryption(self, encryption_type: enums.EncryptionType) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:ENCRyption \n
		Snippet: driver.configure.connection.security.set_encryption(encryption_type = enums.EncryptionType.AES) \n
		Sets the encryption type for AP operation mode, if WPA, WPA2, or WPA3 personal security mode is selected. \n
			:param encryption_type: AES | TKIP | DISabled | GCMP AES: AES basd CCMP-128 with PSK (for WPA2) TKIP: TKIP with PSK (for WPA) DISabled: encryption not used GCMP: CCMP-128 with SAE and PMF (WPA3)
		"""
		param = Conversions.enum_scalar_to_str(encryption_type, enums.EncryptionType)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:ENCRyption {param}')

	# noinspection PyTypeChecker
	def get_pmf(self) -> enums.Protection:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:PMF \n
		Snippet: value: enums.Protection = driver.configure.connection.security.get_pmf() \n
		Selects, whether the protection management frames are unsupported, supported or required. This parameter applies to WPA2,
		WPA3 in AP operation mode. \n
			:return: protection: UNSupported | SUPPorted | REQuired
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:PMF?')
		return Conversions.str_to_scalar_enum(response, enums.Protection)

	def set_pmf(self, protection: enums.Protection) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:PMF \n
		Snippet: driver.configure.connection.security.set_pmf(protection = enums.Protection.REQuired) \n
		Selects, whether the protection management frames are unsupported, supported or required. This parameter applies to WPA2,
		WPA3 in AP operation mode. \n
			:param protection: UNSupported | SUPPorted | REQuired
		"""
		param = Conversions.enum_scalar_to_str(protection, enums.Protection)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:PMF {param}')

	# noinspection PyTypeChecker
	def get_gtransform(self) -> enums.GroupTransform:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:GTRansform \n
		Snippet: value: enums.GroupTransform = driver.configure.connection.security.get_gtransform() \n
		Specifies the group transform for WPA3 personal security mode. \n
			:return: group_transform: ECP256 | ECP384 256-bit ECP or 384-bit ECP
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:GTRansform?')
		return Conversions.str_to_scalar_enum(response, enums.GroupTransform)

	def set_gtransform(self, group_transform: enums.GroupTransform) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:GTRansform \n
		Snippet: driver.configure.connection.security.set_gtransform(group_transform = enums.GroupTransform.ECP256) \n
		Specifies the group transform for WPA3 personal security mode. \n
			:param group_transform: ECP256 | ECP384 256-bit ECP or 384-bit ECP
		"""
		param = Conversions.enum_scalar_to_str(group_transform, enums.GroupTransform)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:GTRansform {param}')

	# noinspection PyTypeChecker
	def get_hashto_elem(self) -> enums.HashMode:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:HASHtoelem \n
		Snippet: value: enums.HashMode = driver.configure.connection.security.get_hashto_elem() \n
		Selects authentication and key management mechanism supported by the R&S CMW: \n
			:return: mode: HUNT | H2E | BOTH HUNT: hunting-and-pecking negotiated in SAE exchange H2E:SAE hash-to-element is mandatory for WPA3 and for SAE in 6 GHz band BOTH: the R&S CMW supports both techniques
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:HASHtoelem?')
		return Conversions.str_to_scalar_enum(response, enums.HashMode)

	def set_hashto_elem(self, mode: enums.HashMode) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SECurity:HASHtoelem \n
		Snippet: driver.configure.connection.security.set_hashto_elem(mode = enums.HashMode.BOTH) \n
		Selects authentication and key management mechanism supported by the R&S CMW: \n
			:param mode: HUNT | H2E | BOTH HUNT: hunting-and-pecking negotiated in SAE exchange H2E:SAE hash-to-element is mandatory for WPA3 and for SAE in 6 GHz band BOTH: the R&S CMW supports both techniques
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HashMode)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SECurity:HASHtoelem {param}')

	def clone(self) -> 'SecurityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SecurityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
