from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VresourceCls:
	"""Vresource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vresource", core, parent)

	def get(self, vxiInstance=repcap.VxiInstance.Default) -> str:
		"""SCPI: SYSTem:COMMunicate:VXI<inst>:VRESource \n
		Snippet: value: str = driver.system.communicate.vxi.vresource.get(vxiInstance = repcap.VxiInstance.Default) \n
		Queries the VISA resource string for the VXI-11 protocol. \n
			:param vxiInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Vxi')
			:return: visa_resource: No help available"""
		vxiInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(vxiInstance, repcap.VxiInstance)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:VXI{vxiInstance_cmd_val}:VRESource?')
		return trim_str_response(response)
