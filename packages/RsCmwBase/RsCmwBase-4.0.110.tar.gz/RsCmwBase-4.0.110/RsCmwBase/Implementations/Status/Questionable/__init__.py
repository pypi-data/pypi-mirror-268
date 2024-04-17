from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QuestionableCls:
	"""Questionable commands group definition. 10 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("questionable", core, parent)

	@property
	def bit(self):
		"""bit commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_bit'):
			from .Bit import BitCls
			self._bit = BitCls(self._core, self._cmd_group)
		return self._bit

	def get_event(self) -> int:
		"""SCPI: STATus:QUEStionable[:EVENt] \n
		Snippet: value: int = driver.status.questionable.get_event() \n
		Returns the contents of the EVENt part of the status register. Reading an EVENt register clears it. \n
			:return: register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		response = self._core.io.query_str('STATus:QUEStionable:EVENt?')
		return Conversions.str_to_int(response)

	def get_condition(self) -> int:
		"""SCPI: STATus:QUEStionable:CONDition \n
		Snippet: value: int = driver.status.questionable.get_condition() \n
		Returns the contents of the CONDition part of the status register. Reading the CONDition registers is nondestructive. \n
			:return: register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		response = self._core.io.query_str('STATus:QUEStionable:CONDition?')
		return Conversions.str_to_int(response)

	def get_enable(self) -> int:
		"""SCPI: STATus:QUEStionable:ENABle \n
		Snippet: value: int = driver.status.questionable.get_enable() \n
		Sets the enable mask which allows true conditions in the EVENt part of the status register to be reported to the next
		higher level in the summary bit. If a bit is 1 in the enable register and its associated event bit changes to true, a
		positive transition occurs in the summary bit. \n
			:return: register_value: No help available
		"""
		response = self._core.io.query_str('STATus:QUEStionable:ENABle?')
		return Conversions.str_to_int(response)

	def set_enable(self, register_value: int) -> None:
		"""SCPI: STATus:QUEStionable:ENABle \n
		Snippet: driver.status.questionable.set_enable(register_value = 1) \n
		Sets the enable mask which allows true conditions in the EVENt part of the status register to be reported to the next
		higher level in the summary bit. If a bit is 1 in the enable register and its associated event bit changes to true, a
		positive transition occurs in the summary bit. \n
			:param register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		param = Conversions.decimal_value_to_str(register_value)
		self._core.io.write(f'STATus:QUEStionable:ENABle {param}')

	def get_ptransition(self) -> int:
		"""SCPI: STATus:QUEStionable:PTRansition \n
		Snippet: value: int = driver.status.questionable.get_ptransition() \n
		Sets the positive transition filter. If a bit is set, a 0 to 1 transition in the corresponding bit of the condition
		register writes a 1 to the corresponding bit of the event register. \n
			:return: register_value: No help available
		"""
		response = self._core.io.query_str('STATus:QUEStionable:PTRansition?')
		return Conversions.str_to_int(response)

	def set_ptransition(self, register_value: int) -> None:
		"""SCPI: STATus:QUEStionable:PTRansition \n
		Snippet: driver.status.questionable.set_ptransition(register_value = 1) \n
		Sets the positive transition filter. If a bit is set, a 0 to 1 transition in the corresponding bit of the condition
		register writes a 1 to the corresponding bit of the event register. \n
			:param register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		param = Conversions.decimal_value_to_str(register_value)
		self._core.io.write(f'STATus:QUEStionable:PTRansition {param}')

	def get_ntransition(self) -> int:
		"""SCPI: STATus:QUEStionable:NTRansition \n
		Snippet: value: int = driver.status.questionable.get_ntransition() \n
		Sets the negative transition filter. If a bit is set, a 1 to 0 transition in the corresponding bit of the condition
		register writes a 1 to the corresponding bit of the event register. \n
			:return: register_value: No help available
		"""
		response = self._core.io.query_str('STATus:QUEStionable:NTRansition?')
		return Conversions.str_to_int(response)

	def set_ntransition(self, register_value: int) -> None:
		"""SCPI: STATus:QUEStionable:NTRansition \n
		Snippet: driver.status.questionable.set_ntransition(register_value = 1) \n
		Sets the negative transition filter. If a bit is set, a 1 to 0 transition in the corresponding bit of the condition
		register writes a 1 to the corresponding bit of the event register. \n
			:param register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		param = Conversions.decimal_value_to_str(register_value)
		self._core.io.write(f'STATus:QUEStionable:NTRansition {param}')

	def clone(self) -> 'QuestionableCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = QuestionableCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
