from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OperationCls:
	"""Operation commands group definition. 10 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("operation", core, parent)

	@property
	def bit(self):
		"""bit commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_bit'):
			from .Bit import BitCls
			self._bit = BitCls(self._core, self._cmd_group)
		return self._bit

	def get_event(self) -> int:
		"""SCPI: STATus:OPERation[:EVENt] \n
		Snippet: value: int = driver.status.operation.get_event() \n
		Returns the contents of the EVENt part of the status register. Reading an EVENt part clears it. For a description of the
		variables <netw_std>, <func_grp> and <appl>, refer to Table 'Variables in STATus:OPERation commands'. \n
			:return: register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		response = self._core.io.query_str('STATus:OPERation:EVENt?')
		return Conversions.str_to_int(response)

	def get_condition(self) -> int:
		"""SCPI: STATus:OPERation:CONDition \n
		Snippet: value: int = driver.status.operation.get_condition() \n
		Returns the contents of the CONDition part of the status register. Reading the CONDition registers is nondestructive. For
		a description of the variables <netw_std>, <func_grp> and <appl>, refer to Table 'Variables in STATus:OPERation commands'. \n
			:return: register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		response = self._core.io.query_str('STATus:OPERation:CONDition?')
		return Conversions.str_to_int(response)

	def get_enable(self) -> int:
		"""SCPI: STATus:OPERation:ENABle \n
		Snippet: value: int = driver.status.operation.get_enable() \n
		Sets the enable mask which allows true conditions in the EVENt part of the status register to be reported to the next
		higher level in the summary bit. If a bit is 1 in the enable register and the associated event bit changes to true, a
		positive transition occurs in the summary bit. For a description of the variables <netw_std>, <func_grp> and <appl>,
		refer to Table 'Variables in STATus:OPERation commands'. \n
			:return: register_value: No help available
		"""
		response = self._core.io.query_str('STATus:OPERation:ENABle?')
		return Conversions.str_to_int(response)

	def set_enable(self, register_value: int) -> None:
		"""SCPI: STATus:OPERation:ENABle \n
		Snippet: driver.status.operation.set_enable(register_value = 1) \n
		Sets the enable mask which allows true conditions in the EVENt part of the status register to be reported to the next
		higher level in the summary bit. If a bit is 1 in the enable register and the associated event bit changes to true, a
		positive transition occurs in the summary bit. For a description of the variables <netw_std>, <func_grp> and <appl>,
		refer to Table 'Variables in STATus:OPERation commands'. \n
			:param register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		param = Conversions.decimal_value_to_str(register_value)
		self._core.io.write(f'STATus:OPERation:ENABle {param}')

	def get_ptransition(self) -> int:
		"""SCPI: STATus:OPERation:PTRansition \n
		Snippet: value: int = driver.status.operation.get_ptransition() \n
		Sets the positive transition filter. If a bit is set, a 0 to 1 transition in the corresponding bit of the condition
		register writes a 1 to the corresponding bit of the event register. For a description of the variables <netw_std>,
		<func_grp> and <appl>, refer to Table 'Variables in STATus:OPERation commands'. \n
			:return: register_value: No help available
		"""
		response = self._core.io.query_str('STATus:OPERation:PTRansition?')
		return Conversions.str_to_int(response)

	def set_ptransition(self, register_value: int) -> None:
		"""SCPI: STATus:OPERation:PTRansition \n
		Snippet: driver.status.operation.set_ptransition(register_value = 1) \n
		Sets the positive transition filter. If a bit is set, a 0 to 1 transition in the corresponding bit of the condition
		register writes a 1 to the corresponding bit of the event register. For a description of the variables <netw_std>,
		<func_grp> and <appl>, refer to Table 'Variables in STATus:OPERation commands'. \n
			:param register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		param = Conversions.decimal_value_to_str(register_value)
		self._core.io.write(f'STATus:OPERation:PTRansition {param}')

	def get_ntransition(self) -> int:
		"""SCPI: STATus:OPERation:NTRansition \n
		Snippet: value: int = driver.status.operation.get_ntransition() \n
		Sets the negative transition filter. If a bit is set, a 1 to 0 transition in the corresponding bit of the condition
		register writes a 1 to the corresponding bit of the event register. For a description of the variables <netw_std>,
		<func_grp> and <appl>, refer to Table 'Variables in STATus:OPERation commands'. \n
			:return: register_value: No help available
		"""
		response = self._core.io.query_str('STATus:OPERation:NTRansition?')
		return Conversions.str_to_int(response)

	def set_ntransition(self, register_value: int) -> None:
		"""SCPI: STATus:OPERation:NTRansition \n
		Snippet: driver.status.operation.set_ntransition(register_value = 1) \n
		Sets the negative transition filter. If a bit is set, a 1 to 0 transition in the corresponding bit of the condition
		register writes a 1 to the corresponding bit of the event register. For a description of the variables <netw_std>,
		<func_grp> and <appl>, refer to Table 'Variables in STATus:OPERation commands'. \n
			:param register_value: integer Range: 0 to 65535 (decimal representation)
		"""
		param = Conversions.decimal_value_to_str(register_value)
		self._core.io.write(f'STATus:OPERation:NTRansition {param}')

	def clone(self) -> 'OperationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OperationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
