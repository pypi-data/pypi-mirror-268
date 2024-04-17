from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProtocolCls:
	"""Protocol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("protocol", core, parent)

	def get(self, file: str) -> str:
		"""SCPI: DIAGnostic:COMPass:DBASe:RLOGging:PROTocol \n
		Snippet: value: str = driver.diagnostic.compass.dbase.rlogging.protocol.get(file = 'abc') \n
		No command help available \n
			:param file: No help available
			:return: protocol: No help available"""
		param = Conversions.value_to_quoted_str(file)
		response = self._core.io.query_str(f'DIAGnostic:COMPass:DBASe:RLOGging:PROTocol? {param}')
		return trim_str_response(response)
