from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.Utilities import trim_str_response
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, board: str, table_id: int, board_instance: int = None) -> None:
		"""SCPI: DIAGnostic:EEPRom:DATA \n
		Snippet: driver.diagnostic.eeprom.data.set(board = 'abc', table_id = 1, board_instance = 1) \n
		No command help available \n
			:param board: No help available
			:param table_id: No help available
			:param board_instance: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('board', board, DataType.String), ArgSingle('table_id', table_id, DataType.Integer), ArgSingle('board_instance', board_instance, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'DIAGnostic:EEPRom:DATA {param}'.rstrip())

	def get(self) -> str:
		"""SCPI: DIAGnostic:EEPRom:DATA \n
		Snippet: value: str = driver.diagnostic.eeprom.data.get() \n
		No command help available \n
			:return: data_folder: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:EEPRom:DATA?')
		return trim_str_response(response)
