from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PropertiesCls:
	"""Properties commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("properties", core, parent)

	def get(self, ielement_id: float, bnormalized: bool) -> str:
		"""SCPI: DIAGnostic:FOOTprint:ELEMent:PROPerties \n
		Snippet: value: str = driver.diagnostic.footPrint.element.properties.get(ielement_id = 1.0, bnormalized = False) \n
		No command help available \n
			:param ielement_id: No help available
			:param bnormalized: No help available
			:return: sproperties: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ielement_id', ielement_id, DataType.Float), ArgSingle('bnormalized', bnormalized, DataType.Boolean))
		response = self._core.io.query_str(f'DIAGnostic:FOOTprint:ELEMent:PROPerties? {param}'.rstrip())
		return trim_str_response(response)
