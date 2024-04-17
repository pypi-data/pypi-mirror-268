from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeCls:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def get_operating(self) -> str:
		"""SCPI: DIAGnostic:PRODuct:TIME:OPERating \n
		Snippet: value: str = driver.diagnostic.product.time.get_operating() \n
		No command help available \n
			:return: operating_time: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:PRODuct:TIME:OPERating?')
		return trim_str_response(response)
