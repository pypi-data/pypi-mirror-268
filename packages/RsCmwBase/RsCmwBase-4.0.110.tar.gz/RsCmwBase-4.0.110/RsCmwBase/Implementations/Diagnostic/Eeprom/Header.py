from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.Utilities import trim_str_response
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HeaderCls:
	"""Header commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("header", core, parent)

	def set(self, board: str, board_instance: int = None) -> None:
		"""SCPI: DIAGnostic:EEPRom:HEADer \n
		Snippet: driver.diagnostic.eeprom.header.set(board = 'abc', board_instance = 1) \n
		No command help available \n
			:param board: No help available
			:param board_instance: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('board', board, DataType.String), ArgSingle('board_instance', board_instance, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'DIAGnostic:EEPRom:HEADer {param}'.rstrip())

	def get(self) -> str:
		"""SCPI: DIAGnostic:EEPRom:HEADer \n
		Snippet: value: str = driver.diagnostic.eeprom.header.get() \n
		No command help available \n
			:return: header: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:EEPRom:HEADer?')
		return trim_str_response(response)
