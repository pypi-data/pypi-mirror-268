from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdCls:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def get(self, cmwVariant=repcap.CmwVariant.Default) -> str:
		"""SCPI: SYSTem:CMW<n>:DEVice:ID \n
		Snippet: value: str = driver.system.cmw.device.id.get(cmwVariant = repcap.CmwVariant.Default) \n
		No command help available \n
			:param cmwVariant: optional repeated capability selector. Default value: Cmw1 (settable in the interface 'Cmw')
			:return: idn: No help available"""
		cmwVariant_cmd_val = self._cmd_group.get_repcap_cmd_value(cmwVariant, repcap.CmwVariant)
		response = self._core.io.query_str(f'SYSTem:CMW{cmwVariant_cmd_val}:DEVice:ID?')
		return trim_str_response(response)
