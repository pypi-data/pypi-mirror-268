from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatisticCls:
	"""Statistic commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistic", core, parent)

	def get(self, formatting: enums.TextFormatting = None) -> bytes:
		"""SCPI: DIAGnostic:KREMote:TMONitor:STATistic \n
		Snippet: value: bytes = driver.diagnostic.kremote.tmonitor.statistic.get(formatting = enums.TextFormatting.TXT) \n
		No command help available \n
			:param formatting: No help available
			:return: coverage_report: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('formatting', formatting, DataType.Enum, enums.TextFormatting, is_optional=True))
		response = self._core.io.query_bin_block_ERROR(f'DIAGnostic:KREMote:TMONitor:STATistic? {param}'.rstrip())
		return response
