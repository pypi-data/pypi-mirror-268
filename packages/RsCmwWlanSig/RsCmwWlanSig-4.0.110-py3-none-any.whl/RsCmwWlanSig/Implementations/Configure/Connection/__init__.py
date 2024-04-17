from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectionCls:
	"""Connection commands group definition. 114 total commands, 21 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connection", core, parent)

	@property
	def association(self):
		"""association commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_association'):
			from .Association import AssociationCls
			self._association = AssociationCls(self._core, self._cmd_group)
		return self._association

	@property
	def hotspot(self):
		"""hotspot commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_hotspot'):
			from .Hotspot import HotspotCls
			self._hotspot = HotspotCls(self._core, self._cmd_group)
		return self._hotspot

	@property
	def wdirect(self):
		"""wdirect commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_wdirect'):
			from .Wdirect import WdirectCls
			self._wdirect = WdirectCls(self._core, self._cmd_group)
		return self._wdirect

	@property
	def station(self):
		"""station commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_station'):
			from .Station import StationCls
			self._station = StationCls(self._core, self._cmd_group)
		return self._station

	@property
	def security(self):
		"""security commands group. 6 Sub-classes, 4 commands."""
		if not hasattr(self, '_security'):
			from .Security import SecurityCls
			self._security = SecurityCls(self._core, self._cmd_group)
		return self._security

	@property
	def qos(self):
		"""qos commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_qos'):
			from .Qos import QosCls
			self._qos = QosCls(self._core, self._cmd_group)
		return self._qos

	@property
	def srates(self):
		"""srates commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_srates'):
			from .Srates import SratesCls
			self._srates = SratesCls(self._core, self._cmd_group)
		return self._srates

	@property
	def mfDef(self):
		"""mfDef commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mfDef'):
			from .MfDef import MfDefCls
			self._mfDef = MfDefCls(self._core, self._cmd_group)
		return self._mfDef

	@property
	def sta(self):
		"""sta commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sta'):
			from .Sta import StaCls
			self._sta = StaCls(self._core, self._cmd_group)
		return self._sta

	@property
	def hetf(self):
		"""hetf commands group. 1 Sub-classes, 10 commands."""
		if not hasattr(self, '_hetf'):
			from .Hetf import HetfCls
			self._hetf = HetfCls(self._core, self._cmd_group)
		return self._hetf

	@property
	def ccode(self):
		"""ccode commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccode'):
			from .Ccode import CcodeCls
			self._ccode = CcodeCls(self._core, self._cmd_group)
		return self._ccode

	@property
	def edca(self):
		"""edca commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_edca'):
			from .Edca import EdcaCls
			self._edca = EdcaCls(self._core, self._cmd_group)
		return self._edca

	@property
	def muedca(self):
		"""muedca commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_muedca'):
			from .Muedca import MuedcaCls
			self._muedca = MuedcaCls(self._core, self._cmd_group)
		return self._muedca

	@property
	def tpControl(self):
		"""tpControl commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tpControl'):
			from .TpControl import TpControlCls
			self._tpControl = TpControlCls(self._core, self._cmd_group)
		return self._tpControl

	@property
	def oobDiscovery(self):
		"""oobDiscovery commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_oobDiscovery'):
			from .OobDiscovery import OobDiscoveryCls
			self._oobDiscovery = OobDiscoveryCls(self._core, self._cmd_group)
		return self._oobDiscovery

	@property
	def hemac(self):
		"""hemac commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hemac'):
			from .Hemac import HemacCls
			self._hemac = HemacCls(self._core, self._cmd_group)
		return self._hemac

	@property
	def ndpSounding(self):
		"""ndpSounding commands group. 1 Sub-classes, 13 commands."""
		if not hasattr(self, '_ndpSounding'):
			from .NdpSounding import NdpSoundingCls
			self._ndpSounding = NdpSoundingCls(self._core, self._cmd_group)
		return self._ndpSounding

	@property
	def aid(self):
		"""aid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aid'):
			from .Aid import AidCls
			self._aid = AidCls(self._core, self._cmd_group)
		return self._aid

	@property
	def dyFragment(self):
		"""dyFragment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dyFragment'):
			from .DyFragment import DyFragmentCls
			self._dyFragment = DyFragmentCls(self._core, self._cmd_group)
		return self._dyFragment

	@property
	def twt(self):
		"""twt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_twt'):
			from .Twt import TwtCls
			self._twt = TwtCls(self._core, self._cmd_group)
		return self._twt

	@property
	def btwt(self):
		"""btwt commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_btwt'):
			from .Btwt import BtwtCls
			self._btwt = BtwtCls(self._core, self._cmd_group)
		return self._btwt

	# noinspection PyTypeChecker
	def get_iv_support(self) -> enums.IpVersionExt:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:IVSupport \n
		Snippet: value: enums.IpVersionExt = driver.configure.connection.get_iv_support() \n
		Defines the required IP version support. \n
			:return: version: IV4 | IV6 | IV4V6 IPv4 only, IPv6 only, or both
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:IVSupport?')
		return Conversions.str_to_scalar_enum(response, enums.IpVersionExt)

	def set_iv_support(self, version: enums.IpVersionExt) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:IVSupport \n
		Snippet: driver.configure.connection.set_iv_support(version = enums.IpVersionExt.IV4) \n
		Defines the required IP version support. \n
			:param version: IV4 | IV6 | IV4V6 IPv4 only, IPv6 only, or both
		"""
		param = Conversions.enum_scalar_to_str(version, enums.IpVersionExt)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:IVSupport {param}')

	# noinspection PyTypeChecker
	def get_omode(self) -> enums.EntityOperationMode:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OMODe \n
		Snippet: value: enums.EntityOperationMode = driver.configure.connection.get_omode() \n
		Selects the operation mode, that is the type of WLAN entity simulated by the WLAN signaling application. \n
			:return: mode: AP | STATion | HSPot2 AP: access point in infrastructure mode STATion: WLAN station HSPot2: WiFi Hotspot 2.0 access point
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:OMODe?')
		return Conversions.str_to_scalar_enum(response, enums.EntityOperationMode)

	def set_omode(self, mode: enums.EntityOperationMode) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:OMODe \n
		Snippet: driver.configure.connection.set_omode(mode = enums.EntityOperationMode.AP) \n
		Selects the operation mode, that is the type of WLAN entity simulated by the WLAN signaling application. \n
			:param mode: AP | STATion | HSPot2 AP: access point in infrastructure mode STATion: WLAN station HSPot2: WiFi Hotspot 2.0 access point
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EntityOperationMode)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:OMODe {param}')

	def get_mstation(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:MSTation \n
		Snippet: value: bool = driver.configure.connection.get_mstation() \n
		Enables or disables the support of multi-station connection. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:MSTation?')
		return Conversions.str_to_bool(response)

	def set_mstation(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:MSTation \n
		Snippet: driver.configure.connection.set_mstation(enable = False) \n
		Enables or disables the support of multi-station connection. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:MSTation {param}')

	# noinspection PyTypeChecker
	def get_smoothing(self) -> enums.SmoothingBit:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SMOothing \n
		Snippet: value: enums.SmoothingBit = driver.configure.connection.get_smoothing() \n
		Indicates to the receiver whether the frequency-domain smoothing is recommended for channel estimation. \n
			:return: bit: NRECommended | RECommended Not recommended or recommended
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SMOothing?')
		return Conversions.str_to_scalar_enum(response, enums.SmoothingBit)

	def set_smoothing(self, bit: enums.SmoothingBit) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SMOothing \n
		Snippet: driver.configure.connection.set_smoothing(bit = enums.SmoothingBit.NRECommended) \n
		Indicates to the receiver whether the frequency-domain smoothing is recommended for channel estimation. \n
			:param bit: NRECommended | RECommended Not recommended or recommended
		"""
		param = Conversions.enum_scalar_to_str(bit, enums.SmoothingBit)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SMOothing {param}')

	def get_pa_interrupt(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:PAINterrupt \n
		Snippet: value: bool = driver.configure.connection.get_pa_interrupt() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:PAINterrupt?')
		return Conversions.str_to_bool(response)

	def set_pa_interrupt(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:PAINterrupt \n
		Snippet: driver.configure.connection.set_pa_interrupt(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:PAINterrupt {param}')

	def get_sync(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SYNC \n
		Snippet: value: bool = driver.configure.connection.get_sync() \n
		If enabled, the PER measurements use identical settings as configured in the signaling application. Refer to the 'Data
		frame control settings'. \n
			:return: sync: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SYNC?')
		return Conversions.str_to_bool(response)

	def set_sync(self, sync: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SYNC \n
		Snippet: driver.configure.connection.set_sync(sync = False) \n
		If enabled, the PER measurements use identical settings as configured in the signaling application. Refer to the 'Data
		frame control settings'. \n
			:param sync: OFF | ON
		"""
		param = Conversions.bool_to_str(sync)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SYNC {param}')

	def get_ssid(self) -> str:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SSID \n
		Snippet: value: str = driver.configure.connection.get_ssid() \n
		Sets the service set identifier (SSID) . \n
			:return: ssid: string String with up to 32 characters (7-bit ASCII only)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:SSID?')
		return trim_str_response(response)

	def set_ssid(self, ssid: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:SSID \n
		Snippet: driver.configure.connection.set_ssid(ssid = 'abc') \n
		Sets the service set identifier (SSID) . \n
			:param ssid: string String with up to 32 characters (7-bit ASCII only)
		"""
		param = Conversions.value_to_quoted_str(ssid)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:SSID {param}')

	def get_bss_color(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BSSColor \n
		Snippet: value: int = driver.configure.connection.get_bss_color() \n
		Specifies the color code of basic service set (BSS) . \n
			:return: value: numeric Range: 1 to 63
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:BSSColor?')
		return Conversions.str_to_int(response)

	def set_bss_color(self, value: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BSSColor \n
		Snippet: driver.configure.connection.set_bss_color(value = 1) \n
		Specifies the color code of basic service set (BSS) . \n
			:param value: numeric Range: 1 to 63
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BSSColor {param}')

	def get_bssid(self) -> str:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BSSid \n
		Snippet: value: str = driver.configure.connection.get_bssid() \n
		Sets the 48-bit MAC address of the WLAN interface. \n
			:return: bssid: hex Hexadecimal number with 12 digits Leading zeros can be omitted. Range: #H0 to #HFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:BSSid?')
		return trim_str_response(response)

	def set_bssid(self, bssid: str) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BSSid \n
		Snippet: driver.configure.connection.set_bssid(bssid = rawAbc) \n
		Sets the 48-bit MAC address of the WLAN interface. \n
			:param bssid: hex Hexadecimal number with 12 digits Leading zeros can be omitted. Range: #H0 to #HFFFFFFFFFFFF
		"""
		param = Conversions.value_to_str(bssid)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BSSid {param}')

	def get_beacon(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BEACon \n
		Snippet: value: int = driver.configure.connection.get_beacon() \n
		Sets the interval between two beacon frame transmissions for a simulated infrastructure/ ad-hoc network. \n
			:return: beacon_intervall: integer Interval in time units (1 TU = 1024 µs) Range: 20 to 16000
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:BEACon?')
		return Conversions.str_to_int(response)

	def set_beacon(self, beacon_intervall: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:BEACon \n
		Snippet: driver.configure.connection.set_beacon(beacon_intervall = 1) \n
		Sets the interval between two beacon frame transmissions for a simulated infrastructure/ ad-hoc network. \n
			:param beacon_intervall: integer Interval in time units (1 TU = 1024 µs) Range: 20 to 16000
		"""
		param = Conversions.decimal_value_to_str(beacon_intervall)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:BEACon {param}')

	def get_dperiod(self) -> int:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:DPERiod \n
		Snippet: value: int = driver.configure.connection.get_dperiod() \n
		Sets the number of beacon intervals between successive delivery traffic indication messages (DTIM) . \n
			:return: period: integer Number of beacon intervals Range: 1 to 10
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:DPERiod?')
		return Conversions.str_to_int(response)

	def set_dperiod(self, period: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:DPERiod \n
		Snippet: driver.configure.connection.set_dperiod(period = 1) \n
		Sets the number of beacon intervals between successive delivery traffic indication messages (DTIM) . \n
			:param period: integer Number of beacon intervals Range: 1 to 10
		"""
		param = Conversions.decimal_value_to_str(period)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:DPERiod {param}')

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.StandardType:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STANdard \n
		Snippet: value: enums.StandardType = driver.configure.connection.get_standard() \n
		Selects the IEEE 802.11 WLAN standard to be used. \n
			:return: typ: ASTD | GOSTd | ANSTd | GONStd | BSTD | GSTD | GNSTd | ACSTd | AXSTd BSTD: 802.11b ASTD: 802.11a GSTD: 802.11g GOSTd: 802.11g (OFDM) ANSTd: 802.11a/n GNSTd: 802.11g/n GONStd: 802.11g (OFDM) /n ACSTd: 802.11ac AXSTd: 802.11ax
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.StandardType)

	def set_standard(self, typ: enums.StandardType) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:STANdard \n
		Snippet: driver.configure.connection.set_standard(typ = enums.StandardType.ACSTd) \n
		Selects the IEEE 802.11 WLAN standard to be used. \n
			:param typ: ASTD | GOSTd | ANSTd | GONStd | BSTD | GSTD | GNSTd | ACSTd | AXSTd BSTD: 802.11b ASTD: 802.11a GSTD: 802.11g GOSTd: 802.11g (OFDM) ANSTd: 802.11a/n GNSTd: 802.11g/n GONStd: 802.11g (OFDM) /n ACSTd: 802.11ac AXSTd: 802.11ax
		"""
		param = Conversions.enum_scalar_to_str(typ, enums.StandardType)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:STANdard {param}')

	def get_dsss(self) -> bool:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:DSSS \n
		Snippet: value: bool = driver.configure.connection.get_dsss() \n
		Enables you to associate an 802.11b device using 802.11ac or ax standard. Also, it enables you to use non-HT management
		frames within 802.11ac and ax. \n
			:return: support_of_dsss: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:SIGNaling<Instance>:CONNection:DSSS?')
		return Conversions.str_to_bool(response)

	def set_dsss(self, support_of_dsss: bool) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:CONNection:DSSS \n
		Snippet: driver.configure.connection.set_dsss(support_of_dsss = False) \n
		Enables you to associate an 802.11b device using 802.11ac or ax standard. Also, it enables you to use non-HT management
		frames within 802.11ac and ax. \n
			:param support_of_dsss: OFF | ON
		"""
		param = Conversions.bool_to_str(support_of_dsss)
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:CONNection:DSSS {param}')

	def clone(self) -> 'ConnectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConnectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
