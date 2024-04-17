from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SystemCls:
	"""System commands group definition. 98 total commands, 25 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	@property
	def ipSet(self):
		"""ipSet commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSet'):
			from .IpSet import IpSetCls
			self._ipSet = IpSetCls(self._core, self._cmd_group)
		return self._ipSet

	@property
	def device(self):
		"""device commands group. 2 Sub-classes, 6 commands."""
		if not hasattr(self, '_device'):
			from .Device import DeviceCls
			self._device = DeviceCls(self._core, self._cmd_group)
		return self._device

	@property
	def connector(self):
		"""connector commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connector'):
			from .Connector import ConnectorCls
			self._connector = ConnectorCls(self._core, self._cmd_group)
		return self._connector

	@property
	def routing(self):
		"""routing commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_routing'):
			from .Routing import RoutingCls
			self._routing = RoutingCls(self._core, self._cmd_group)
		return self._routing

	@property
	def reference(self):
		"""reference commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import ReferenceCls
			self._reference = ReferenceCls(self._core, self._cmd_group)
		return self._reference

	@property
	def ssync(self):
		"""ssync commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ssync'):
			from .Ssync import SsyncCls
			self._ssync = SsyncCls(self._core, self._cmd_group)
		return self._ssync

	@property
	def help(self):
		"""help commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_help'):
			from .Help import HelpCls
			self._help = HelpCls(self._core, self._cmd_group)
		return self._help

	@property
	def record(self):
		"""record commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_record'):
			from .Record import RecordCls
			self._record = RecordCls(self._core, self._cmd_group)
		return self._record

	@property
	def startup(self):
		"""startup commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_startup'):
			from .Startup import StartupCls
			self._startup = StartupCls(self._core, self._cmd_group)
		return self._startup

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Update import UpdateCls
			self._update = UpdateCls(self._core, self._cmd_group)
		return self._update

	@property
	def communicate(self):
		"""communicate commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_communicate'):
			from .Communicate import CommunicateCls
			self._communicate = CommunicateCls(self._core, self._cmd_group)
		return self._communicate

	@property
	def cmw(self):
		"""cmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmw'):
			from .Cmw import CmwCls
			self._cmw = CmwCls(self._core, self._cmd_group)
		return self._cmw

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmwCls
			self._singleCmw = SingleCmwCls(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def option(self):
		"""option commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_option'):
			from .Option import OptionCls
			self._option = OptionCls(self._core, self._cmd_group)
		return self._option

	@property
	def password(self):
		"""password commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_password'):
			from .Password import PasswordCls
			self._password = PasswordCls(self._core, self._cmd_group)
		return self._password

	@property
	def display(self):
		"""display commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_display'):
			from .Display import DisplayCls
			self._display = DisplayCls(self._core, self._cmd_group)
		return self._display

	@property
	def stIcon(self):
		"""stIcon commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_stIcon'):
			from .StIcon import StIconCls
			self._stIcon = StIconCls(self._core, self._cmd_group)
		return self._stIcon

	@property
	def deviceFootprint(self):
		"""deviceFootprint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deviceFootprint'):
			from .DeviceFootprint import DeviceFootprintCls
			self._deviceFootprint = DeviceFootprintCls(self._core, self._cmd_group)
		return self._deviceFootprint

	@property
	def generator(self):
		"""generator commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import GeneratorCls
			self._generator = GeneratorCls(self._core, self._cmd_group)
		return self._generator

	@property
	def measurement(self):
		"""measurement commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import MeasurementCls
			self._measurement = MeasurementCls(self._core, self._cmd_group)
		return self._measurement

	@property
	def signaling(self):
		"""signaling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signaling'):
			from .Signaling import SignalingCls
			self._signaling = SignalingCls(self._core, self._cmd_group)
		return self._signaling

	@property
	def time(self):
		"""time commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	@property
	def date(self):
		"""date commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import DateCls
			self._date = DateCls(self._core, self._cmd_group)
		return self._date

	@property
	def tzone(self):
		"""tzone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tzone'):
			from .Tzone import TzoneCls
			self._tzone = TzoneCls(self._core, self._cmd_group)
		return self._tzone

	@property
	def error(self):
		"""error commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_error'):
			from .Error import ErrorCls
			self._error = ErrorCls(self._core, self._cmd_group)
		return self._error

	def get_reliability(self) -> int:
		"""SCPI: SYSTem:BASE:RELiability \n
		Snippet: value: int = driver.system.get_reliability() \n
		Returns a reliability value indicating errors detected by the base software. \n
			:return: value: decimal For reliability indicator values, see 'Checking the reliability indicator'
		"""
		response = self._core.io.query_str('SYSTem:BASE:RELiability?')
		return Conversions.str_to_int(response)

	def get_did(self) -> str:
		"""SCPI: SYSTem:DID \n
		Snippet: value: str = driver.system.get_did() \n
		No command help available \n
			:return: device_id: No help available
		"""
		response = self._core.io.query_str('SYSTem:DID?')
		return trim_str_response(response)

	def get_klock(self) -> bool:
		"""SCPI: SYSTem:KLOCk \n
		Snippet: value: bool = driver.system.get_klock() \n
		Locks or unlocks the local controls of the instrument, including the (soft-) front panel keys. \n
			:return: klock: No help available
		"""
		response = self._core.io.query_str('SYSTem:KLOCk?')
		return Conversions.str_to_bool(response)

	def set_klock(self, klock: bool) -> None:
		"""SCPI: SYSTem:KLOCk \n
		Snippet: driver.system.set_klock(klock = False) \n
		Locks or unlocks the local controls of the instrument, including the (soft-) front panel keys. \n
			:param klock: ON | OFF | 1 | 0 ON | 1: Local key locked (key lock enabled) OFF | 0: Local keys unlocked
		"""
		param = Conversions.bool_to_str(klock)
		self._core.io.write(f'SYSTem:KLOCk {param}')

	def preset(self, appl_name_and_li_number: str = None) -> None:
		"""SCPI: SYSTem:PRESet \n
		Snippet: driver.system.preset(appl_name_and_li_number = 'abc') \n
		A PRESet sets the parameters of the subinstrument to default values suitable for local/manual interaction. A RESet sets
		them to default values suitable for remote operation. Optionally, the preset/reset can be limited to a specific
		application instance. \n
			:param appl_name_and_li_number: string Application and instance to be reset/preset. Example: 'LTE Meas1' for LTE UE measurements instance 1 Omitting the instance (e.g. 'LTE Meas') selects instance 1. The supported strings are listed in the table below.
		"""
		param = ''
		if appl_name_and_li_number:
			param = Conversions.value_to_quoted_str(appl_name_and_li_number)
		self._core.io.write(f'SYSTem:PRESet {param}'.strip())

	def preset_all(self) -> None:
		"""SCPI: SYSTem:PRESet:ALL \n
		Snippet: driver.system.preset_all() \n
		A PRESet sets the parameters of all subinstruments and the base settings to default values suitable for local/manual
		interaction. A RESet sets them to default values suitable for remote operation. \n
		"""
		self._core.io.write(f'SYSTem:PRESet:ALL')

	def preset_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:PRESet:ALL \n
		Snippet: driver.system.preset_all_with_opc() \n
		A PRESet sets the parameters of all subinstruments and the base settings to default values suitable for local/manual
		interaction. A RESet sets them to default values suitable for remote operation. \n
		Same as preset_all, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:PRESet:ALL', opc_timeout_ms)

	def preset_base(self) -> None:
		"""SCPI: SYSTem:PRESet:BASE \n
		Snippet: driver.system.preset_base() \n
		A PRESet sets the base settings to default values suitable for local/manual interaction. A RESet sets them to default
		values suitable for remote operation. \n
		"""
		self._core.io.write(f'SYSTem:PRESet:BASE')

	def preset_base_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:PRESet:BASE \n
		Snippet: driver.system.preset_base_with_opc() \n
		A PRESet sets the base settings to default values suitable for local/manual interaction. A RESet sets them to default
		values suitable for remote operation. \n
		Same as preset_base, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:PRESet:BASE', opc_timeout_ms)

	def reset(self, appl_name_and_li_number: str = None) -> None:
		"""SCPI: SYSTem:RESet \n
		Snippet: driver.system.reset(appl_name_and_li_number = 'abc') \n
		A PRESet sets the parameters of the subinstrument to default values suitable for local/manual interaction. A RESet sets
		them to default values suitable for remote operation. Optionally, the preset/reset can be limited to a specific
		application instance. \n
			:param appl_name_and_li_number: string Application and instance to be reset/preset. Example: 'LTE Meas1' for LTE UE measurements instance 1 Omitting the instance (e.g. 'LTE Meas') selects instance 1. The supported strings are listed in the table below.
		"""
		param = ''
		if appl_name_and_li_number:
			param = Conversions.value_to_quoted_str(appl_name_and_li_number)
		self._core.io.write(f'SYSTem:RESet {param}'.strip())

	def reset_all(self) -> None:
		"""SCPI: SYSTem:RESet:ALL \n
		Snippet: driver.system.reset_all() \n
		A PRESet sets the parameters of all subinstruments and the base settings to default values suitable for local/manual
		interaction. A RESet sets them to default values suitable for remote operation. \n
		"""
		self._core.io.write(f'SYSTem:RESet:ALL')

	def reset_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:RESet:ALL \n
		Snippet: driver.system.reset_all_with_opc() \n
		A PRESet sets the parameters of all subinstruments and the base settings to default values suitable for local/manual
		interaction. A RESet sets them to default values suitable for remote operation. \n
		Same as reset_all, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:RESet:ALL', opc_timeout_ms)

	def reset_base(self) -> None:
		"""SCPI: SYSTem:RESet:BASE \n
		Snippet: driver.system.reset_base() \n
		A PRESet sets the base settings to default values suitable for local/manual interaction. A RESet sets them to default
		values suitable for remote operation. \n
		"""
		self._core.io.write(f'SYSTem:RESet:BASE')

	def reset_base_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:RESet:BASE \n
		Snippet: driver.system.reset_base_with_opc() \n
		A PRESet sets the base settings to default values suitable for local/manual interaction. A RESet sets them to default
		values suitable for remote operation. \n
		Same as reset_base, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:RESet:BASE', opc_timeout_ms)

	def get_version(self) -> float:
		"""SCPI: SYSTem:VERSion \n
		Snippet: value: float = driver.system.get_version() \n
		Queries the SCPI version number to which the instrument complies. \n
			:return: version: string '1999.0' is the final SCPI version.
		"""
		response = self._core.io.query_str('SYSTem:VERSion?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SystemCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SystemCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
