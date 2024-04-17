from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DetailsCls:
	"""Details commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("details", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency: List[float]: No parameter help available
			- Correction: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Correction', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: List[float] = None
			self.Correction: List[float] = None

	def get(self, table_name: str, start_index: float = None, count: float = None) -> GetStruct:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:DETails \n
		Snippet: value: GetStruct = driver.configure.freqCorrection.correctionTable.details.get(table_name = 'abc', start_index = 1.0, count = 1.0) \n
		Returns the entries of a correction table. \n
			:param table_name: string To display a list of existing tables, use the command CONFigure:BASE:FDCorrection:CTABle:CATalog?. You can add the prefix 'instn/' to address subinstrument number n+1.
			:param start_index: numeric Index number of the first entry to be listed. The first entry of a table has index number 0. Default: 0
			:param count: numeric Maximum number of entries to be listed. By default, all entries from StartIndex to the end of the table are listed.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('table_name', table_name, DataType.String), ArgSingle('start_index', start_index, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True))
		return self._core.io.query_struct(f'CONFigure:BASE:FDCorrection:CTABle:DETails? {param}'.rstrip(), self.__class__.GetStruct())
