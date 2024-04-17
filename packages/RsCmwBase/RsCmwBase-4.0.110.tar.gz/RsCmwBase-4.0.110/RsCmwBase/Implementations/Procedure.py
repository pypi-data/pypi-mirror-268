from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from ..Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProcedureCls:
	"""Procedure commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("procedure", core, parent)

	def get_cmwd(self) -> str:
		"""SCPI: PROCedure:CMWD \n
		Snippet: value: str = driver.procedure.get_cmwd() \n
		No command help available \n
			:return: command_string: No help available
		"""
		response = self._core.io.query_str('PROCedure:CMWD?')
		return trim_str_response(response)

	def set_cmwd(self, command_string: str) -> None:
		"""SCPI: PROCedure:CMWD \n
		Snippet: driver.procedure.set_cmwd(command_string = 'abc') \n
		No command help available \n
			:param command_string: No help available
		"""
		param = Conversions.value_to_quoted_str(command_string)
		self._core.io.write(f'PROCedure:CMWD {param}')
