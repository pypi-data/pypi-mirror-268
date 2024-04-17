from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DebugCls:
	"""Debug commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("debug", core, parent)

	def get_mode(self) -> bool:
		"""SCPI: DIAGnostic:COMPass:DEBug:MODE \n
		Snippet: value: bool = driver.diagnostic.compass.debug.get_mode() \n
		No command help available \n
			:return: debug_mode: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:COMPass:DEBug:MODE?')
		return Conversions.str_to_bool(response)

	def set_mode(self, debug_mode: bool) -> None:
		"""SCPI: DIAGnostic:COMPass:DEBug:MODE \n
		Snippet: driver.diagnostic.compass.debug.set_mode(debug_mode = False) \n
		No command help available \n
			:param debug_mode: No help available
		"""
		param = Conversions.bool_to_str(debug_mode)
		self._core.io.write(f'DIAGnostic:COMPass:DEBug:MODE {param}')
