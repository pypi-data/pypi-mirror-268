from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ElementCls:
	"""Element commands group definition. 5 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("element", core, parent)

	@property
	def connection(self):
		"""connection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import ConnectionCls
			self._connection = ConnectionCls(self._core, self._cmd_group)
		return self._connection

	@property
	def properties(self):
		"""properties commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_properties'):
			from .Properties import PropertiesCls
			self._properties = PropertiesCls(self._core, self._cmd_group)
		return self._properties

	@property
	def references(self):
		"""references commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_references'):
			from .References import ReferencesCls
			self._references = ReferencesCls(self._core, self._cmd_group)
		return self._references

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	def get_ids(self) -> List[int]:
		"""SCPI: DIAGnostic:FOOTprint:ELEMent:IDS \n
		Snippet: value: List[int] = driver.diagnostic.footPrint.element.get_ids() \n
		No command help available \n
			:return: element_ids: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('DIAGnostic:FOOTprint:ELEMent:IDS?')
		return response

	def clone(self) -> 'ElementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ElementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
