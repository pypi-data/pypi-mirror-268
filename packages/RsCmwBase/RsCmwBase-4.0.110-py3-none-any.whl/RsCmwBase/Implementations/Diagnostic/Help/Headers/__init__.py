from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HeadersCls:
	"""Headers commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("headers", core, parent)

	@property
	def access(self):
		"""access commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_access'):
			from .Access import AccessCls
			self._access = AccessCls(self._core, self._cmd_group)
		return self._access

	def get_value(self) -> bytes:
		"""SCPI: DIAGnostic:HELP:HEADers \n
		Snippet: value: bytes = driver.diagnostic.help.headers.get_value() \n
		No command help available \n
			:return: header: No help available
		"""
		response = self._core.io.query_bin_block('DIAGnostic:HELP:HEADers?')
		return response

	def clone(self) -> 'HeadersCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HeadersCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
