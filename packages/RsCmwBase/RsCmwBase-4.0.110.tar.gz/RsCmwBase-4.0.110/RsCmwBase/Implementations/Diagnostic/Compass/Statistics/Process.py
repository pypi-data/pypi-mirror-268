from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProcessCls:
	"""Process commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("process", core, parent)

	def get(self, token: str) -> str:
		"""SCPI: DIAGnostic:COMPass:STATistics:PROCess \n
		Snippet: value: str = driver.diagnostic.compass.statistics.process.get(token = 'abc') \n
		No command help available \n
			:param token: No help available
			:return: statistics: No help available"""
		param = Conversions.value_to_quoted_str(token)
		response = self._core.io.query_str(f'DIAGnostic:COMPass:STATistics:PROCess? {param}')
		return trim_str_response(response)
