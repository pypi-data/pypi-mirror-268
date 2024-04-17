from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyntaxCls:
	"""Syntax commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("syntax", core, parent)

	def get(self, header: str) -> str:
		"""SCPI: DIAGnostic:HELP:SYNTax \n
		Snippet: value: str = driver.diagnostic.help.syntax.get(header = 'abc') \n
		No command help available \n
			:param header: No help available
			:return: syntax: No help available"""
		param = Conversions.value_to_quoted_str(header)
		response = self._core.io.query_str(f'DIAGnostic:HELP:SYNTax? {param}')
		return trim_str_response(response)

	def get_all(self) -> bytes:
		"""SCPI: DIAGnostic:HELP:SYNTax:ALL \n
		Snippet: value: bytes = driver.diagnostic.help.syntax.get_all() \n
		No command help available \n
			:return: commands: No help available
		"""
		response = self._core.io.query_bin_block('DIAGnostic:HELP:SYNTax:ALL?')
		return response
