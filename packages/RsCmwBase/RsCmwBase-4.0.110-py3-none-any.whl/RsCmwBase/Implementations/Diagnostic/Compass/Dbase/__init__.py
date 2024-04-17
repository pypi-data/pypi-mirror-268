from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DbaseCls:
	"""Dbase commands group definition. 8 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbase", core, parent)

	@property
	def rlogging(self):
		"""rlogging commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_rlogging'):
			from .Rlogging import RloggingCls
			self._rlogging = RloggingCls(self._core, self._cmd_group)
		return self._rlogging

	@property
	def taLogging(self):
		"""taLogging commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_taLogging'):
			from .TaLogging import TaLoggingCls
			self._taLogging = TaLoggingCls(self._core, self._cmd_group)
		return self._taLogging

	def clone(self) -> 'DbaseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DbaseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
