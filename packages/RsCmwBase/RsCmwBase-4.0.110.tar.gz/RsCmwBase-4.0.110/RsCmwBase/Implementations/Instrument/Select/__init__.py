from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	@property
	def dstrategy(self):
		"""dstrategy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dstrategy'):
			from .Dstrategy import DstrategyCls
			self._dstrategy = DstrategyCls(self._core, self._cmd_group)
		return self._dstrategy

	def get_value(self) -> str:
		"""SCPI: INSTrument[:SELect] \n
		Snippet: value: str = driver.instrument.select.get_value() \n
		No command help available \n
			:return: instrument: No help available
		"""
		response = self._core.io.query_str('INSTrument:SELect?')
		return trim_str_response(response)

	def set_value(self, instrument: str) -> None:
		"""SCPI: INSTrument[:SELect] \n
		Snippet: driver.instrument.select.set_value(instrument = rawAbc) \n
		No command help available \n
			:param instrument: No help available
		"""
		param = Conversions.value_to_str(instrument)
		self._core.io.write(f'INSTrument:SELect {param}')

	def clone(self) -> 'SelectCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SelectCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
