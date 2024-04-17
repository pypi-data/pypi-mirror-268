from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetupCls:
	"""Setup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	def set(self, routing_name: str, data: List[enums.ExpertSetup]) -> None:
		"""SCPI: DIAGnostic:ROUTing:EXPert:SETup \n
		Snippet: driver.diagnostic.routing.expert.setup.set(routing_name = 'abc', data = [ExpertSetup.BBG1, ExpertSetup.SUW7]) \n
		No command help available \n
			:param routing_name: No help available
			:param data: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('routing_name', routing_name, DataType.String), ArgSingle.as_open_list('data', data, DataType.EnumList, enums.ExpertSetup))
		self._core.io.write(f'DIAGnostic:ROUTing:EXPert:SETup {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, routing_name: str) -> List[enums.ExpertSetup]:
		"""SCPI: DIAGnostic:ROUTing:EXPert:SETup \n
		Snippet: value: List[enums.ExpertSetup] = driver.diagnostic.routing.expert.setup.get(routing_name = 'abc') \n
		No command help available \n
			:param routing_name: No help available
			:return: data: No help available"""
		param = Conversions.value_to_quoted_str(routing_name)
		response = self._core.io.query_str(f'DIAGnostic:ROUTing:EXPert:SETup? {param}')
		return Conversions.str_to_list_enum(response, enums.ExpertSetup)
