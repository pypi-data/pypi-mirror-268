from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StIconCls:
	"""StIcon commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stIcon", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: SYSTem:BASE:STICon:ENABle \n
		Snippet: value: bool = driver.system.stIcon.get_enable() \n
		Selects whether an icon for the CMW software is added to the system tray of the operating system. \n
			:return: on_off: ON | OFF | 1 | 0 ON | 1: icon in system tray OFF | 0: no icon in system tray
		"""
		response = self._core.io.query_str('SYSTem:BASE:STICon:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, on_off: bool) -> None:
		"""SCPI: SYSTem:BASE:STICon:ENABle \n
		Snippet: driver.system.stIcon.set_enable(on_off = False) \n
		Selects whether an icon for the CMW software is added to the system tray of the operating system. \n
			:param on_off: ON | OFF | 1 | 0 ON | 1: icon in system tray OFF | 0: no icon in system tray
		"""
		param = Conversions.bool_to_str(on_off)
		self._core.io.write(f'SYSTem:BASE:STICon:ENABle {param}')

	def open(self) -> None:
		"""SCPI: SYSTem:BASE:STICon:OPEN \n
		Snippet: driver.system.stIcon.open() \n
		Restores the windows and taskbar entries of the CMW application after they have been hidden by the CLOSe command.
		Prerequisite: A CMW software icon has been added to the system tray (ENABle command) . \n
		"""
		self._core.io.write(f'SYSTem:BASE:STICon:OPEN')

	def open_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:BASE:STICon:OPEN \n
		Snippet: driver.system.stIcon.open_with_opc() \n
		Restores the windows and taskbar entries of the CMW application after they have been hidden by the CLOSe command.
		Prerequisite: A CMW software icon has been added to the system tray (ENABle command) . \n
		Same as open, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:BASE:STICon:OPEN', opc_timeout_ms)

	def close(self) -> None:
		"""SCPI: SYSTem:BASE:STICon:CLOSe \n
		Snippet: driver.system.stIcon.close() \n
		Hides all windows and taskbar entries of the CMW application. Prerequisite: A CMW software icon has been added to the
		system tray (ENABle command) . \n
		"""
		self._core.io.write(f'SYSTem:BASE:STICon:CLOSe')

	def close_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:BASE:STICon:CLOSe \n
		Snippet: driver.system.stIcon.close_with_opc() \n
		Hides all windows and taskbar entries of the CMW application. Prerequisite: A CMW software icon has been added to the
		system tray (ENABle command) . \n
		Same as close, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:BASE:STICon:CLOSe', opc_timeout_ms)
