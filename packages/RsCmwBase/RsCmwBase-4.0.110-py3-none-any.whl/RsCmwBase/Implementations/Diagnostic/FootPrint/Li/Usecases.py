from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsecasesCls:
	"""Usecases commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usecases", core, parent)

	def get(self, ili_id: int) -> str:
		"""SCPI: DIAGnostic:FOOTprint:LI:USECases \n
		Snippet: value: str = driver.diagnostic.footPrint.li.usecases.get(ili_id = 1) \n
		No command help available \n
			:param ili_id: No help available
			:return: the_result: No help available"""
		param = Conversions.decimal_value_to_str(ili_id)
		response = self._core.io.query_str(f'DIAGnostic:FOOTprint:LI:USECases? {param}')
		return trim_str_response(response)
