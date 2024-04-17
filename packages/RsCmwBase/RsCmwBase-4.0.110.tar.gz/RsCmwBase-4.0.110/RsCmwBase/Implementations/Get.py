from typing import List

from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GetCls:
	"""Get commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("get", core, parent)

	def get_xvalues(self) -> List[float]:
		"""SCPI: GET:XVALues \n
		Snippet: value: List[float] = driver.get.get_xvalues() \n
		No command help available \n
			:return: value: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('GET:XVALues?')
		return response
