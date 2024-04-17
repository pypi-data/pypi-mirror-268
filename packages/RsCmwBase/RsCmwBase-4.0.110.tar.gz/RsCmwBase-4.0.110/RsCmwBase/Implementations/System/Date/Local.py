from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LocalCls:
	"""Local commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("local", core, parent)

	def set(self, year: int, month: int, day: int) -> None:
		"""SCPI: SYSTem:DATE:LOCal \n
		Snippet: driver.system.date.local.set(year = 1, month = 1, day = 1) \n
		No command help available \n
			:param year: No help available
			:param month: No help available
			:param day: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('year', year, DataType.Integer), ArgSingle('month', month, DataType.Integer), ArgSingle('day', day, DataType.Integer))
		self._core.io.write(f'SYSTem:DATE:LOCal {param}'.rstrip())

	# noinspection PyTypeChecker
	class LocalStruct(StructBase):
		"""Response structure. Fields: \n
			- Year: int: No parameter help available
			- Month: int: No parameter help available
			- Day: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Year'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Day')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: int = None
			self.Month: int = None
			self.Day: int = None

	def get(self) -> LocalStruct:
		"""SCPI: SYSTem:DATE:LOCal \n
		Snippet: value: LocalStruct = driver.system.date.local.get() \n
		No command help available \n
			:return: structure: for return value, see the help for LocalStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:DATE:LOCal?', self.__class__.LocalStruct())
