from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HelpCls:
	"""Help commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("help", core, parent)

	@property
	def status(self):
		"""status commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_status'):
			from .Status import StatusCls
			self._status = StatusCls(self._core, self._cmd_group)
		return self._status

	@property
	def headers(self):
		"""headers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_headers'):
			from .Headers import HeadersCls
			self._headers = HeadersCls(self._core, self._cmd_group)
		return self._headers

	@property
	def syntax(self):
		"""syntax commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_syntax'):
			from .Syntax import SyntaxCls
			self._syntax = SyntaxCls(self._core, self._cmd_group)
		return self._syntax

	def clone(self) -> 'HelpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HelpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
