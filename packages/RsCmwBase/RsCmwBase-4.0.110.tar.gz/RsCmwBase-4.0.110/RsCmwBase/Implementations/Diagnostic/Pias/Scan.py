from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.Utilities import trim_str_response
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScanCls:
	"""Scan commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scan", core, parent)

	def get(self, timeout: int, subnet: enums.SubnetScope, device_group_count: int, ids: List[str]) -> str:
		"""SCPI: DIAGnostic:PIAS:SCAN \n
		Snippet: value: str = driver.diagnostic.pias.scan.get(timeout = 1, subnet = enums.SubnetScope.ALL, device_group_count = 1, ids = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param timeout: No help available
			:param subnet: No help available
			:param device_group_count: No help available
			:param ids: No help available
			:return: result: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('timeout', timeout, DataType.Integer), ArgSingle('subnet', subnet, DataType.Enum, enums.SubnetScope), ArgSingle('device_group_count', device_group_count, DataType.Integer), ArgSingle.as_open_list('ids', ids, DataType.StringList, None))
		response = self._core.io.query_str(f'DIAGnostic:PIAS:SCAN? {param}'.rstrip())
		return trim_str_response(response)
