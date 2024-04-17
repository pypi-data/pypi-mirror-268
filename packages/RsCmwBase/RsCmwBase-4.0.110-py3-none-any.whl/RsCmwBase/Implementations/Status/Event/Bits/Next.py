from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NextCls:
	"""Next commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("next", core, parent)

	def get(self, filter_py: str = None, mode: enums.ExpressionMode = None) -> str:
		"""SCPI: STATus:EVENt:BITS:NEXT \n
		Snippet: value: str = driver.status.event.bits.next.get(filter_py = 'abc', mode = enums.ExpressionMode.REGex) \n
		Searches, returns and deletes the next event at the lowest level of the STATus:OPERation register hierarchy. This command
		can be used to supply state transitions to a remote control program one by one. The program can then react on the
		transitions, e.g. fetch the results of a measurement that reached the RDY or SDR state. Or start a new measurement after
		a measurement has been finished. A list of all events in the STATus:OPERation register hierarchy can be returned using
		method RsCmwBase.Status.Event.Bits.All.get_. \n
			:param filter_py: No help available
			:param mode: No help available
			:return: bit: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True), ArgSingle('mode', mode, DataType.Enum, enums.ExpressionMode, is_optional=True))
		response = self._core.io.query_str(f'STATus:EVENt:BITS:NEXT? {param}'.rstrip())
		return trim_str_response(response)
