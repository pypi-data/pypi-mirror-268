from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PossibleCls:
	"""Possible commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("possible", core, parent)

	def get(self, item: str = None) -> List[str]:
		"""SCPI: SYSTem:ROUTing:POSSible \n
		Snippet: value: List[str] = driver.system.routing.possible.get(item = 'abc') \n
		No command help available \n
			:param item: No help available
			:return: routing: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item', item, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'SYSTem:ROUTing:POSSible? {param}'.rstrip())
		return Conversions.str_to_str_list(response)
