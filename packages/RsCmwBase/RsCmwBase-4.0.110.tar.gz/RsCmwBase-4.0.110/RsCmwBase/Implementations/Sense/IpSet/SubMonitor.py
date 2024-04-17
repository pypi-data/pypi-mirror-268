from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubMonitorCls:
	"""SubMonitor commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subMonitor", core, parent)

	def get_name(self) -> List[str]:
		"""SCPI: SENSe:BASE:IPSet:SMONitor:NAME \n
		Snippet: value: List[str] = driver.sense.ipSet.subMonitor.get_name() \n
		Queries the name of all network nodes detected by the subnet monitor. \n
			:return: names: string Comma-separated list of strings, one per network node
		"""
		response = self._core.io.query_str('SENSe:BASE:IPSet:SMONitor:NAME?')
		return Conversions.str_to_str_list(response)

	def get_type_py(self) -> List[str]:
		"""SCPI: SENSe:BASE:IPSet:SMONitor:TYPE \n
		Snippet: value: List[str] = driver.sense.ipSet.subMonitor.get_type_py() \n
		Queries the type of all network nodes detected by the subnet monitor. \n
			:return: types: string Comma-separated list of strings, one per network node
		"""
		response = self._core.io.query_str('SENSe:BASE:IPSet:SMONitor:TYPE?')
		return Conversions.str_to_str_list(response)

	def get_id(self) -> List[int]:
		"""SCPI: SENSe:BASE:IPSet:SMONitor:ID \n
		Snippet: value: List[int] = driver.sense.ipSet.subMonitor.get_id() \n
		Queries the ID (third segment of IP address) of all network nodes detected by the subnet monitor. \n
			:return: ids: decimal Comma-separated list of values, one per network node Range: 1 to 254
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SENSe:BASE:IPSet:SMONitor:ID?')
		return response

	def get_description(self) -> List[str]:
		"""SCPI: SENSe:BASE:IPSet:SMONitor:DESCription \n
		Snippet: value: List[str] = driver.sense.ipSet.subMonitor.get_description() \n
		Queries the description of all network nodes detected by the subnet monitor. \n
			:return: descriptions: string Comma-separated list of strings, one per network node
		"""
		response = self._core.io.query_str('SENSe:BASE:IPSet:SMONitor:DESCription?')
		return Conversions.str_to_str_list(response)
