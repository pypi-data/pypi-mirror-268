from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InstrumentCls:
	"""Instrument commands group definition. 8 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("instrument", core, parent)

	@property
	def select(self):
		"""select commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import SelectCls
			self._select = SelectCls(self._core, self._cmd_group)
		return self._select

	@property
	def display(self):
		"""display commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_display'):
			from .Display import DisplayCls
			self._display = DisplayCls(self._core, self._cmd_group)
		return self._display

	def get_nselect(self) -> int:
		"""SCPI: INSTrument:NSELect \n
		Snippet: value: int = driver.instrument.get_nselect() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('INSTrument:NSELect?')
		return Conversions.str_to_int(response)

	def set_nselect(self, arg_0: int) -> None:
		"""SCPI: INSTrument:NSELect \n
		Snippet: driver.instrument.set_nselect(arg_0 = 1) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'INSTrument:NSELect {param}')

	def clone(self) -> 'InstrumentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InstrumentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
