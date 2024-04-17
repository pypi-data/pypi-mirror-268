from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OnCls:
	"""On commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("on", core, parent)

	def get(self, filter_py: str = None, mode: enums.ExpressionMode = None) -> str:
		"""SCPI: STATus:GENerator:CONDition:ON \n
		Snippet: value: str = driver.status.generator.condition.on.get(filter_py = 'abc', mode = enums.ExpressionMode.REGex) \n
		Lists all generator tasks or measurement tasks whose current state equals the state indicated by the last mnemonic. The
		results are collected from the CONDition parts of the lowest level registers of the STATus:OPERation register hierarchy. \n
			:param filter_py: No help available
			:param mode: No help available
			:return: bitname: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True), ArgSingle('mode', mode, DataType.Enum, enums.ExpressionMode, is_optional=True))
		response = self._core.io.query_str(f'STATus:GENerator:CONDition:ON? {param}'.rstrip())
		return trim_str_response(response)
