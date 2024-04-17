from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DisplayCls:
	"""Display commands group definition. 8 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	@property
	def monitor(self):
		"""monitor commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_monitor'):
			from .Monitor import MonitorCls
			self._monitor = MonitorCls(self._core, self._cmd_group)
		return self._monitor

	def get_mwindow(self) -> bool:
		"""SCPI: SYSTem:BASE:DISPlay:MWINdow \n
		Snippet: value: bool = driver.system.display.get_mwindow() \n
		Enables or disables the multiple-window mode of the graphical user interface. \n
			:return: on_off: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:DISPlay:MWINdow?')
		return Conversions.str_to_bool(response)

	def set_mwindow(self, on_off: bool) -> None:
		"""SCPI: SYSTem:BASE:DISPlay:MWINdow \n
		Snippet: driver.system.display.set_mwindow(on_off = False) \n
		Enables or disables the multiple-window mode of the graphical user interface. \n
			:param on_off: ON | OFF | 1 | 0 ON | 1: multiple-window mode OFF | 0: single-window mode
		"""
		param = Conversions.bool_to_str(on_off)
		self._core.io.write(f'SYSTem:BASE:DISPlay:MWINdow {param}')

	# noinspection PyTypeChecker
	def get_color_set(self) -> enums.ColorSet:
		"""SCPI: SYSTem:BASE:DISPlay:COLorset \n
		Snippet: value: enums.ColorSet = driver.system.display.get_color_set() \n
		No command help available \n
			:return: color_set: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:DISPlay:COLorset?')
		return Conversions.str_to_scalar_enum(response, enums.ColorSet)

	def set_color_set(self, color_set: enums.ColorSet) -> None:
		"""SCPI: SYSTem:BASE:DISPlay:COLorset \n
		Snippet: driver.system.display.set_color_set(color_set = enums.ColorSet.DEF) \n
		No command help available \n
			:param color_set: No help available
		"""
		param = Conversions.enum_scalar_to_str(color_set, enums.ColorSet)
		self._core.io.write(f'SYSTem:BASE:DISPlay:COLorset {param}')

	# noinspection PyTypeChecker
	def get_font_set(self) -> enums.FontType:
		"""SCPI: SYSTem:BASE:DISPlay:FONTset \n
		Snippet: value: enums.FontType = driver.system.display.get_font_set() \n
		Selects the font size for the GUI labels. \n
			:return: fonset: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:DISPlay:FONTset?')
		return Conversions.str_to_scalar_enum(response, enums.FontType)

	def set_font_set(self, fonset: enums.FontType) -> None:
		"""SCPI: SYSTem:BASE:DISPlay:FONTset \n
		Snippet: driver.system.display.set_font_set(fonset = enums.FontType.DEF) \n
		Selects the font size for the GUI labels. \n
			:param fonset: DEF | LRG DEF: Small fonts LRG: Large fonts
		"""
		param = Conversions.enum_scalar_to_str(fonset, enums.FontType)
		self._core.io.write(f'SYSTem:BASE:DISPlay:FONTset {param}')

	# noinspection PyTypeChecker
	def get_rollkey_mode(self) -> enums.RollkeyMode:
		"""SCPI: SYSTem:BASE:DISPlay:ROLLkeymode \n
		Snippet: value: enums.RollkeyMode = driver.system.display.get_rollkey_mode() \n
		No command help available \n
			:return: rollkey_mode: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:DISPlay:ROLLkeymode?')
		return Conversions.str_to_scalar_enum(response, enums.RollkeyMode)

	def set_rollkey_mode(self, rollkey_mode: enums.RollkeyMode) -> None:
		"""SCPI: SYSTem:BASE:DISPlay:ROLLkeymode \n
		Snippet: driver.system.display.set_rollkey_mode(rollkey_mode = enums.RollkeyMode.CURSors) \n
		No command help available \n
			:param rollkey_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(rollkey_mode, enums.RollkeyMode)
		self._core.io.write(f'SYSTem:BASE:DISPlay:ROLLkeymode {param}')

	# noinspection PyTypeChecker
	def get_language(self) -> enums.DisplayLanguage:
		"""SCPI: SYSTem:BASE:DISPlay:LANGuage \n
		Snippet: value: enums.DisplayLanguage = driver.system.display.get_language() \n
		No command help available \n
			:return: language: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:DISPlay:LANGuage?')
		return Conversions.str_to_scalar_enum(response, enums.DisplayLanguage)

	def set_language(self, language: enums.DisplayLanguage) -> None:
		"""SCPI: SYSTem:BASE:DISPlay:LANGuage \n
		Snippet: driver.system.display.set_language(language = enums.DisplayLanguage.AR) \n
		No command help available \n
			:param language: No help available
		"""
		param = Conversions.enum_scalar_to_str(language, enums.DisplayLanguage)
		self._core.io.write(f'SYSTem:BASE:DISPlay:LANGuage {param}')

	def get_update(self) -> bool:
		"""SCPI: SYSTem:DISPlay:UPDate \n
		Snippet: value: bool = driver.system.display.get_update() \n
		Defines whether the display is updated or not while the instrument is in the remote state. If the display update is
		switched off, the normal GUI is replaced by a static image while the instrument is in the remote state. Switching off the
		display can speed up the measurement and is the recommended state. See also 'Using the display during remote control' \n
			:return: display_update: No help available
		"""
		response = self._core.io.query_str('SYSTem:DISPlay:UPDate?')
		return Conversions.str_to_bool(response)

	def set_update(self, display_update: bool) -> None:
		"""SCPI: SYSTem:DISPlay:UPDate \n
		Snippet: driver.system.display.set_update(display_update = False) \n
		Defines whether the display is updated or not while the instrument is in the remote state. If the display update is
		switched off, the normal GUI is replaced by a static image while the instrument is in the remote state. Switching off the
		display can speed up the measurement and is the recommended state. See also 'Using the display during remote control' \n
			:param display_update: ON | OFF | 1 | 0 ON | 1: Display is shown and updated during remote control. OFF | 0: Display shows static image during remote control.
		"""
		param = Conversions.bool_to_str(display_update)
		self._core.io.write(f'SYSTem:DISPlay:UPDate {param}')

	def clone(self) -> 'DisplayCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DisplayCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
