from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReleaseCls:
	"""Release commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("release", core, parent)

	def set(self, name: str, key: int) -> None:
		"""SCPI: CONFigure:SEMaphore:RELease \n
		Snippet: driver.configure.semaphore.release.set(name = 'abc', key = 1) \n
		No command help available \n
			:param name: No help available
			:param key: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('key', key, DataType.Integer))
		self._core.io.write(f'CONFigure:SEMaphore:RELease {param}'.rstrip())
