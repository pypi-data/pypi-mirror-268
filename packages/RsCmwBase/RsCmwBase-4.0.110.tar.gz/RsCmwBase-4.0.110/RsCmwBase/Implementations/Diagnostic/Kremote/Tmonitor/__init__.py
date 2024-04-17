from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TmonitorCls:
	"""Tmonitor commands group definition. 9 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmonitor", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def dump(self):
		"""dump commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dump'):
			from .Dump import DumpCls
			self._dump = DumpCls(self._core, self._cmd_group)
		return self._dump

	@property
	def statistic(self):
		"""statistic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_statistic'):
			from .Statistic import StatisticCls
			self._statistic = StatisticCls(self._core, self._cmd_group)
		return self._statistic

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	def reset(self) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:RESet \n
		Snippet: driver.diagnostic.kremote.tmonitor.reset() \n
		No command help available \n
		"""
		self._core.io.write(f'DIAGnostic:KREMote:TMONitor:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:RESet \n
		Snippet: driver.diagnostic.kremote.tmonitor.reset_with_opc() \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DIAGnostic:KREMote:TMONitor:RESet', opc_timeout_ms)

	def clone(self) -> 'TmonitorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TmonitorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
