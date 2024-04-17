from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyntaxCls:
	"""Syntax commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("syntax", core, parent)

	def get(self, header: str) -> bytes:
		"""SCPI: SYSTem:HELP:SYNTax \n
		Snippet: value: bytes = driver.system.help.syntax.get(header = 'abc') \n
		No command help available \n
			:param header: No help available
			:return: syntax: No help available"""
		param = Conversions.value_to_quoted_str(header)
		response = self._core.io.query_bin_block_ERROR(f'SYSTem:HELP:SYNTax? {param}')
		return response

	def get_all(self) -> bytes:
		"""SCPI: SYSTem:HELP:SYNTax:ALL \n
		Snippet: value: bytes = driver.system.help.syntax.get_all() \n
		No command help available \n
			:return: syntax: No help available
		"""
		response = self._core.io.query_bin_block('SYSTem:HELP:SYNTax:ALL?')
		return response
