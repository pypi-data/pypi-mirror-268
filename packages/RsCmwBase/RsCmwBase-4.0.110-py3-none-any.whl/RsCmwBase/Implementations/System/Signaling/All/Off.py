from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffCls:
	"""Off commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("off", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:SIGNaling:ALL:OFF \n
		Snippet: driver.system.signaling.all.off.set() \n
		Switch off all signaling applications, generators or measurements. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:SIGNaling:ALL:OFF', opc_timeout_ms)
