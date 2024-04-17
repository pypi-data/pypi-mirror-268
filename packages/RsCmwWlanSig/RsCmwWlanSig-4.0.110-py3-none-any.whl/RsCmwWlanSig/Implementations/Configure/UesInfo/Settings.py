from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SettingsCls:
	"""Settings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("settings", core, parent)

	def set(self, reporting_interval: float, time_span: int) -> None:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:UESinfo:SETTings \n
		Snippet: driver.configure.uesInfo.settings.set(reporting_interval = 1.0, time_span = 1) \n
		Sets reporting interval and time span used for enhanced statistics of user data traffic. \n
			:param reporting_interval: float Range: 0.2 s to 5 s
			:param time_span: integer Range: 1 to 1500
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('reporting_interval', reporting_interval, DataType.Float), ArgSingle('time_span', time_span, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:SIGNaling<Instance>:UESinfo:SETTings {param}'.rstrip())

	# noinspection PyTypeChecker
	class SettingsStruct(StructBase):
		"""Response structure. Fields: \n
			- Reporting_Interval: float: float Range: 0.2 s to 5 s
			- Time_Span: int: integer Range: 1 to 1500"""
		__meta_args_list = [
			ArgStruct.scalar_float('Reporting_Interval'),
			ArgStruct.scalar_int('Time_Span')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reporting_Interval: float = None
			self.Time_Span: int = None

	def get(self) -> SettingsStruct:
		"""SCPI: CONFigure:WLAN:SIGNaling<instance>:UESinfo:SETTings \n
		Snippet: value: SettingsStruct = driver.configure.uesInfo.settings.get() \n
		Sets reporting interval and time span used for enhanced statistics of user data traffic. \n
			:return: structure: for return value, see the help for SettingsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:SIGNaling<Instance>:UESinfo:SETTings?', self.__class__.SettingsStruct())
