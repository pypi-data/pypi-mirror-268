from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ErrorCls:
	"""Error commands group definition. 3 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("error", core, parent)

	@property
	def queue(self):
		"""queue commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_queue'):
			from .Queue import QueueCls
			self._queue = QueueCls(self._core, self._cmd_group)
		return self._queue

	def clone(self) -> 'ErrorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ErrorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
