from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FirmwareUpdateCls:
	"""FirmwareUpdate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("firmwareUpdate", core, parent)

	def get_info(self) -> str:
		"""SCPI: SENSe:FWUPdate:INFO \n
		Snippet: value: str = driver.sense.firmwareUpdate.get_info() \n
		No command help available \n
			:return: info: No help available
		"""
		response = self._core.io.query_str('SENSe:FWUPdate:INFO?')
		return trim_str_response(response)
