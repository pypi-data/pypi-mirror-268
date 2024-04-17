from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TzoneCls:
	"""Tzone commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tzone", core, parent)

	def set(self, hour: int, minute: int) -> None:
		"""SCPI: SYSTem:TZONe \n
		Snippet: driver.system.tzone.set(hour = 1, minute = 1) \n
		No command help available \n
			:param hour: No help available
			:param minute: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hour', hour, DataType.Integer), ArgSingle('minute', minute, DataType.Integer))
		self._core.io.write(f'SYSTem:TZONe {param}'.rstrip())

	# noinspection PyTypeChecker
	class TzoneStruct(StructBase):
		"""Response structure. Fields: \n
			- Hour: int: No parameter help available
			- Minute: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None

	def get(self) -> TzoneStruct:
		"""SCPI: SYSTem:TZONe \n
		Snippet: value: TzoneStruct = driver.system.tzone.get() \n
		No command help available \n
			:return: structure: for return value, see the help for TzoneStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:TZONe?', self.__class__.TzoneStruct())
