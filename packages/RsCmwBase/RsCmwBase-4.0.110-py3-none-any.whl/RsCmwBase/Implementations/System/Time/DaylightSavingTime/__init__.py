from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DaylightSavingTimeCls:
	"""DaylightSavingTime commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("daylightSavingTime", core, parent)

	@property
	def rule(self):
		"""rule commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rule'):
			from .Rule import RuleCls
			self._rule = RuleCls(self._core, self._cmd_group)
		return self._rule

	def get_mode(self) -> bool:
		"""SCPI: SYSTem:TIME:DSTime:MODE \n
		Snippet: value: bool = driver.system.time.daylightSavingTime.get_mode() \n
		No command help available \n
			:return: dst: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:DSTime:MODE?')
		return Conversions.str_to_bool(response)

	def set_mode(self, dst: bool) -> None:
		"""SCPI: SYSTem:TIME:DSTime:MODE \n
		Snippet: driver.system.time.daylightSavingTime.set_mode(dst = False) \n
		No command help available \n
			:param dst: No help available
		"""
		param = Conversions.bool_to_str(dst)
		self._core.io.write(f'SYSTem:TIME:DSTime:MODE {param}')

	def clone(self) -> 'DaylightSavingTimeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DaylightSavingTimeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
