from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DisplayCls:
	"""Display commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	def get_cat(self) -> str:
		"""SCPI: INSTrument:DISPlay:CAT \n
		Snippet: value: str = driver.instrument.display.get_cat() \n
		No command help available \n
			:return: list_py: No help available
		"""
		response = self._core.io.query_str('INSTrument:DISPlay:CAT?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DisplayMode:
		"""SCPI: INSTrument:DISPlay:MODE \n
		Snippet: value: enums.DisplayMode = driver.instrument.display.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('INSTrument:DISPlay:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DisplayMode)

	def set_mode(self, mode: enums.DisplayMode) -> None:
		"""SCPI: INSTrument:DISPlay:MODE \n
		Snippet: driver.instrument.display.set_mode(mode = enums.DisplayMode.AUTomatic) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DisplayMode)
		self._core.io.write(f'INSTrument:DISPlay:MODE {param}')

	def open(self, item: str) -> None:
		"""SCPI: INSTrument:DISPlay:OPEN \n
		Snippet: driver.instrument.display.open(item = 'abc') \n
		No command help available \n
			:param item: No help available
		"""
		param = Conversions.value_to_quoted_str(item)
		self._core.io.write(f'INSTrument:DISPlay:OPEN {param}')

	def close(self, item: str) -> None:
		"""SCPI: INSTrument:DISPlay:CLOSe \n
		Snippet: driver.instrument.display.close(item = 'abc') \n
		No command help available \n
			:param item: No help available
		"""
		param = Conversions.value_to_quoted_str(item)
		self._core.io.write(f'INSTrument:DISPlay:CLOSe {param}')

	def get_value(self) -> int:
		"""SCPI: INSTrument:DISPlay \n
		Snippet: value: int = driver.instrument.display.get_value() \n
		No command help available \n
			:return: instr: No help available
		"""
		response = self._core.io.query_str('INSTrument:DISPlay?')
		return Conversions.str_to_int(response)

	def set_value(self, instr: int) -> None:
		"""SCPI: INSTrument:DISPlay \n
		Snippet: driver.instrument.display.set_value(instr = 1) \n
		No command help available \n
			:param instr: No help available
		"""
		param = Conversions.decimal_value_to_str(instr)
		self._core.io.write(f'INSTrument:DISPlay {param}')
