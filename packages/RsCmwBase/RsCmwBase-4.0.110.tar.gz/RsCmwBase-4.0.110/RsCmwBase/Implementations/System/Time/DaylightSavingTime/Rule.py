from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RuleCls:
	"""Rule commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rule", core, parent)

	def get_catalog(self) -> str:
		"""SCPI: SYSTem:TIME:DSTime:RULE:CATalog \n
		Snippet: value: str = driver.system.time.daylightSavingTime.rule.get_catalog() \n
		No command help available \n
			:return: cat: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:DSTime:RULE:CATalog?')
		return trim_str_response(response)

	def get_value(self) -> str:
		"""SCPI: SYSTem:TIME:DSTime:RULE \n
		Snippet: value: str = driver.system.time.daylightSavingTime.rule.get_value() \n
		No command help available \n
			:return: rule: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:DSTime:RULE?')
		return trim_str_response(response)

	def set_value(self, rule: str) -> None:
		"""SCPI: SYSTem:TIME:DSTime:RULE \n
		Snippet: driver.system.time.daylightSavingTime.rule.set_value(rule = 'abc') \n
		No command help available \n
			:param rule: No help available
		"""
		param = Conversions.value_to_quoted_str(rule)
		self._core.io.write(f'SYSTem:TIME:DSTime:RULE {param}')
