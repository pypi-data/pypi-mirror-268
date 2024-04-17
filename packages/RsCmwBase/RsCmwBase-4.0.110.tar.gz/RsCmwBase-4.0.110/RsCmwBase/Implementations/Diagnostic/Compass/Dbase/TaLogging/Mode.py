from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, name: str, mod: enums.DiagLoggigMode) -> None:
		"""SCPI: DIAGnostic:COMPass:DBASe:TALogging:MODE \n
		Snippet: driver.diagnostic.compass.dbase.taLogging.mode.set(name = 'abc', mod = enums.DiagLoggigMode.DETailed) \n
		No command help available \n
			:param name: No help available
			:param mod: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('mod', mod, DataType.Enum, enums.DiagLoggigMode))
		self._core.io.write(f'DIAGnostic:COMPass:DBASe:TALogging:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, name: str) -> enums.DiagLoggigMode:
		"""SCPI: DIAGnostic:COMPass:DBASe:TALogging:MODE \n
		Snippet: value: enums.DiagLoggigMode = driver.diagnostic.compass.dbase.taLogging.mode.get(name = 'abc') \n
		No command help available \n
			:param name: No help available
			:return: mod: No help available"""
		param = Conversions.value_to_quoted_str(name)
		response = self._core.io.query_str(f'DIAGnostic:COMPass:DBASe:TALogging:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.DiagLoggigMode)
