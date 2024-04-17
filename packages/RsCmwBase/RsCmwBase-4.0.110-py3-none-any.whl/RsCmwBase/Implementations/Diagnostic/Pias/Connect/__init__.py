from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectCls:
	"""Connect commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connect", core, parent)

	@property
	def multiple(self):
		"""multiple commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiple'):
			from .Multiple import MultipleCls
			self._multiple = MultipleCls(self._core, self._cmd_group)
		return self._multiple

	def get(self, handle: str, pias_id: str) -> int:
		"""SCPI: DIAGnostic:PIAS:CONNect \n
		Snippet: value: int = driver.diagnostic.pias.connect.get(handle = 'abc', pias_id = 'abc') \n
		No command help available \n
			:param handle: No help available
			:param pias_id: No help available
			:return: result: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('handle', handle, DataType.String), ArgSingle('pias_id', pias_id, DataType.String))
		response = self._core.io.query_str(f'DIAGnostic:PIAS:CONNect? {param}'.rstrip())
		return Conversions.str_to_int(response)

	def clone(self) -> 'ConnectCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConnectCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
