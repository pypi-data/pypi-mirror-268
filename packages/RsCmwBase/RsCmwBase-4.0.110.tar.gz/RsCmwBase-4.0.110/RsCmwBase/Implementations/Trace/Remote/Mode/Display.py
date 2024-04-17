from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DisplayCls:
	"""Display commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	def clear(self) -> None:
		"""SCPI: TRACe:REMote:MODE:DISPlay:CLEar \n
		Snippet: driver.trace.remote.mode.display.clear() \n
		Clears the display of the SCPI remote trace in analysis mode. \n
		"""
		self._core.io.write(f'TRACe:REMote:MODE:DISPlay:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: TRACe:REMote:MODE:DISPlay:CLEar \n
		Snippet: driver.trace.remote.mode.display.clear_with_opc() \n
		Clears the display of the SCPI remote trace in analysis mode. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TRACe:REMote:MODE:DISPlay:CLEar', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_enable(self) -> enums.RemoteTraceEnable:
		"""SCPI: TRACe:REMote:MODE:DISPlay:ENABle \n
		Snippet: value: enums.RemoteTraceEnable = driver.trace.remote.mode.display.get_enable() \n
		Enables or disables the display of the SCPI remote trace. Two modes are available when the display is enabled: a live
		mode and an analysis mode. \n
			:return: benable: No help available
		"""
		response = self._core.io.query_str('TRACe:REMote:MODE:DISPlay:ENABle?')
		return Conversions.str_to_scalar_enum(response, enums.RemoteTraceEnable)

	def set_enable(self, benable: enums.RemoteTraceEnable) -> None:
		"""SCPI: TRACe:REMote:MODE:DISPlay:ENABle \n
		Snippet: driver.trace.remote.mode.display.set_enable(benable = enums.RemoteTraceEnable.ANALysis) \n
		Enables or disables the display of the SCPI remote trace. Two modes are available when the display is enabled: a live
		mode and an analysis mode. \n
			:param benable: ANALysis | LIVE | OFF ANALysis: Stop tracing to analyze already traced messages. LIVE: Trace messages and display them. OFF: Disable the report display. Default value: OFF
		"""
		param = Conversions.enum_scalar_to_str(benable, enums.RemoteTraceEnable)
		self._core.io.write(f'TRACe:REMote:MODE:DISPlay:ENABle {param}')
