from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExistCls:
	"""Exist commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("exist", core, parent)

	def get(self, table_name: str) -> int:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:EXISt \n
		Snippet: value: int = driver.configure.freqCorrection.correctionTable.exist.get(table_name = 'abc') \n
		Queries whether a correction table with the specified name exists or not. \n
			:param table_name: string You can add the prefix 'instn/' to the table name, to address subinstrument number n+1.
			:return: exists: 0 | 1 0: table does not exist 1: table exists"""
		param = Conversions.value_to_quoted_str(table_name)
		response = self._core.io.query_str(f'CONFigure:BASE:FDCorrection:CTABle:EXISt? {param}')
		return Conversions.str_to_int(response)
