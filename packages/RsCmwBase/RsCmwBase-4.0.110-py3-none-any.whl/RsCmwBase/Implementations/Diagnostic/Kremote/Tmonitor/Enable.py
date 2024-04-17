from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def get_statistic(self) -> bool:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle:STATistic \n
		Snippet: value: bool = driver.diagnostic.kremote.tmonitor.enable.get_statistic() \n
		No command help available \n
			:return: performance_mode: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:KREMote:TMONitor:ENABle:STATistic?')
		return Conversions.str_to_bool(response)

	def set_statistic(self, performance_mode: bool) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle:STATistic \n
		Snippet: driver.diagnostic.kremote.tmonitor.enable.set_statistic(performance_mode = False) \n
		No command help available \n
			:param performance_mode: No help available
		"""
		param = Conversions.bool_to_str(performance_mode)
		self._core.io.write(f'DIAGnostic:KREMote:TMONitor:ENABle:STATistic {param}')

	def get_timing(self) -> bool:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle:TIMing \n
		Snippet: value: bool = driver.diagnostic.kremote.tmonitor.enable.get_timing() \n
		No command help available \n
			:return: timing_enable: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:KREMote:TMONitor:ENABle:TIMing?')
		return Conversions.str_to_bool(response)

	def set_timing(self, timing_enable: bool) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle:TIMing \n
		Snippet: driver.diagnostic.kremote.tmonitor.enable.set_timing(timing_enable = False) \n
		No command help available \n
			:param timing_enable: No help available
		"""
		param = Conversions.bool_to_str(timing_enable)
		self._core.io.write(f'DIAGnostic:KREMote:TMONitor:ENABle:TIMing {param}')

	def get_trace(self) -> bool:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle:TRACe \n
		Snippet: value: bool = driver.diagnostic.kremote.tmonitor.enable.get_trace() \n
		No command help available \n
			:return: trace_mode: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:KREMote:TMONitor:ENABle:TRACe?')
		return Conversions.str_to_bool(response)

	def set_trace(self, trace_mode: bool) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle:TRACe \n
		Snippet: driver.diagnostic.kremote.tmonitor.enable.set_trace(trace_mode = False) \n
		No command help available \n
			:param trace_mode: No help available
		"""
		param = Conversions.bool_to_str(trace_mode)
		self._core.io.write(f'DIAGnostic:KREMote:TMONitor:ENABle:TRACe {param}')

	def get_rpc(self) -> bool:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle:RPC \n
		Snippet: value: bool = driver.diagnostic.kremote.tmonitor.enable.get_rpc() \n
		No command help available \n
			:return: rpc_enable: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:KREMote:TMONitor:ENABle:RPC?')
		return Conversions.str_to_bool(response)

	def set_rpc(self, rpc_enable: bool) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle:RPC \n
		Snippet: driver.diagnostic.kremote.tmonitor.enable.set_rpc(rpc_enable = False) \n
		No command help available \n
			:param rpc_enable: No help available
		"""
		param = Conversions.bool_to_str(rpc_enable)
		self._core.io.write(f'DIAGnostic:KREMote:TMONitor:ENABle:RPC {param}')

	def get_value(self) -> bool:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle \n
		Snippet: value: bool = driver.diagnostic.kremote.tmonitor.enable.get_value() \n
		No command help available \n
			:return: remote_diagnose: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:KREMote:TMONitor:ENABle?')
		return Conversions.str_to_bool(response)

	def set_value(self, remote_diagnose: bool) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:ENABle \n
		Snippet: driver.diagnostic.kremote.tmonitor.enable.set_value(remote_diagnose = False) \n
		No command help available \n
			:param remote_diagnose: No help available
		"""
		param = Conversions.bool_to_str(remote_diagnose)
		self._core.io.write(f'DIAGnostic:KREMote:TMONitor:ENABle {param}')
