from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DstrategyCls:
	"""Dstrategy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dstrategy", core, parent)

	def set(self, arg_0: enums.OperationMode, arg_1: enums.DisplayStrategy = None) -> None:
		"""SCPI: INSTrument[:SELect]:DSTRategy \n
		Snippet: driver.instrument.select.dstrategy.set(arg_0 = enums.OperationMode.LOCal, arg_1 = enums.DisplayStrategy.BYLayout) \n
		No command help available \n
			:param arg_0: No help available
			:param arg_1: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.Enum, enums.OperationMode), ArgSingle('arg_1', arg_1, DataType.Enum, enums.DisplayStrategy, is_optional=True))
		self._core.io.write(f'INSTrument:SELect:DSTRategy {param}'.rstrip())

	# noinspection PyTypeChecker
	class DstrategyStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: enums.OperationMode: No parameter help available
			- Arg_1: enums.DisplayStrategy: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Arg_0', enums.OperationMode),
			ArgStruct.scalar_enum('Arg_1', enums.DisplayStrategy)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: enums.OperationMode = None
			self.Arg_1: enums.DisplayStrategy = None

	def get(self) -> DstrategyStruct:
		"""SCPI: INSTrument[:SELect]:DSTRategy \n
		Snippet: value: DstrategyStruct = driver.instrument.select.dstrategy.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DstrategyStruct structure arguments."""
		return self._core.io.query_struct(f'INSTrument:SELect:DSTRategy?', self.__class__.DstrategyStruct())
