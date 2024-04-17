from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeCls:
	"""Time commands group definition. 10 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	@property
	def daylightSavingTime(self):
		"""daylightSavingTime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_daylightSavingTime'):
			from .DaylightSavingTime import DaylightSavingTimeCls
			self._daylightSavingTime = DaylightSavingTimeCls(self._core, self._cmd_group)
		return self._daylightSavingTime

	@property
	def local(self):
		"""local commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_local'):
			from .Local import LocalCls
			self._local = LocalCls(self._core, self._cmd_group)
		return self._local

	@property
	def utc(self):
		"""utc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_utc'):
			from .Utc import UtcCls
			self._utc = UtcCls(self._core, self._cmd_group)
		return self._utc

	@property
	def hrTimer(self):
		"""hrTimer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_hrTimer'):
			from .HrTimer import HrTimerCls
			self._hrTimer = HrTimerCls(self._core, self._cmd_group)
		return self._hrTimer

	def set(self, hour: int, min_py: int, sec: int) -> None:
		"""SCPI: SYSTem:TIME \n
		Snippet: driver.system.time.set(hour = 1, min_py = 1, sec = 1) \n
		No command help available \n
			:param hour: No help available
			:param min_py: No help available
			:param sec: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hour', hour, DataType.Integer), ArgSingle('min_py', min_py, DataType.Integer), ArgSingle('sec', sec, DataType.Integer))
		self._core.io.write(f'SYSTem:TIME {param}'.rstrip())

	# noinspection PyTypeChecker
	class TimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Hour: int: No parameter help available
			- Min_Py: int: No parameter help available
			- Sec: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Min_Py'),
			ArgStruct.scalar_int('Sec')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Min_Py: int = None
			self.Sec: int = None

	def get(self) -> TimeStruct:
		"""SCPI: SYSTem:TIME \n
		Snippet: value: TimeStruct = driver.system.time.get() \n
		No command help available \n
			:return: structure: for return value, see the help for TimeStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:TIME?', self.__class__.TimeStruct())

	def clone(self) -> 'TimeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TimeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
