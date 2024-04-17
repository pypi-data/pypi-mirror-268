from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LockCls:
	"""Lock commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lock", core, parent)

	def get(self, name: str, timeout: float = None) -> int:
		"""SCPI: CONFigure:MUTex:LOCK \n
		Snippet: value: int = driver.configure.mutex.lock.get(name = 'abc', timeout = 1.0) \n
		No command help available \n
			:param name: No help available
			:param timeout: No help available
			:return: key: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('timeout', timeout, DataType.Float, None, is_optional=True))
		response = self._core.io.query_str(f'CONFigure:MUTex:LOCK? {param}'.rstrip())
		return Conversions.str_to_int(response)
