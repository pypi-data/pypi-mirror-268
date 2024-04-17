from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScenarioCls:
	"""Scenario commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenario", core, parent)

	def set(self, enabled: List[bool] = None, instruments_mask: List[int] = None, use_case: List[str] = None) -> None:
		"""SCPI: DIAGnostic:ACCess:SCENario \n
		Snippet: driver.diagnostic.access.scenario.set(enabled = [True, False, True], instruments_mask = [1, 2, 3], use_case = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param enabled: No help available
			:param instruments_mask: No help available
			:param use_case: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enabled', enabled, DataType.BooleanList, None, True, True, 1), ArgSingle('instruments_mask', instruments_mask, DataType.IntegerList, None, True, True, 1), ArgSingle('use_case', use_case, DataType.StringList, None, True, True, 1))
		self._core.io.write(f'DIAGnostic:ACCess:SCENario {param}'.rstrip())
