from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 54 total commands, 12 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def spoint(self):
		"""spoint commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_spoint'):
			from .Spoint import SpointCls
			self._spoint = SpointCls(self._core, self._cmd_group)
		return self._spoint

	@property
	def semaphore(self):
		"""semaphore commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_semaphore'):
			from .Semaphore import SemaphoreCls
			self._semaphore = SemaphoreCls(self._core, self._cmd_group)
		return self._semaphore

	@property
	def mutex(self):
		"""mutex commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_mutex'):
			from .Mutex import MutexCls
			self._mutex = MutexCls(self._core, self._cmd_group)
		return self._mutex

	@property
	def multiCmw(self):
		"""multiCmw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiCmw'):
			from .MultiCmw import MultiCmwCls
			self._multiCmw = MultiCmwCls(self._core, self._cmd_group)
		return self._multiCmw

	@property
	def ipSet(self):
		"""ipSet commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSet'):
			from .IpSet import IpSetCls
			self._ipSet = IpSetCls(self._core, self._cmd_group)
		return self._ipSet

	@property
	def adjustment(self):
		"""adjustment commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_adjustment'):
			from .Adjustment import AdjustmentCls
			self._adjustment = AdjustmentCls(self._core, self._cmd_group)
		return self._adjustment

	@property
	def ipcr(self):
		"""ipcr commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ipcr'):
			from .Ipcr import IpcrCls
			self._ipcr = IpcrCls(self._core, self._cmd_group)
		return self._ipcr

	@property
	def freqCorrection(self):
		"""freqCorrection commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_freqCorrection'):
			from .FreqCorrection import FreqCorrectionCls
			self._freqCorrection = FreqCorrectionCls(self._core, self._cmd_group)
		return self._freqCorrection

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmwCls
			self._singleCmw = SingleCmwCls(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def cmwd(self):
		"""cmwd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmwd'):
			from .Cmwd import CmwdCls
			self._cmwd = CmwdCls(self._core, self._cmd_group)
		return self._cmwd

	@property
	def correction(self):
		"""correction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import CorrectionCls
			self._correction = CorrectionCls(self._core, self._cmd_group)
		return self._correction

	@property
	def mmonitor(self):
		"""mmonitor commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mmonitor'):
			from .Mmonitor import MmonitorCls
			self._mmonitor = MmonitorCls(self._core, self._cmd_group)
		return self._mmonitor

	# noinspection PyTypeChecker
	def get_fcontrol(self) -> enums.FanMode:
		"""SCPI: CONFigure:BASE:FCONtrol \n
		Snippet: value: enums.FanMode = driver.configure.get_fcontrol() \n
		Selects a fan control mode. \n
			:return: mode: LOW | NORMal | HIGH LOW: less cooling than in normal mode NORMal: default mode HIGH: more cooling than in normal mode
		"""
		response = self._core.io.query_str('CONFigure:BASE:FCONtrol?')
		return Conversions.str_to_scalar_enum(response, enums.FanMode)

	def set_fcontrol(self, mode: enums.FanMode) -> None:
		"""SCPI: CONFigure:BASE:FCONtrol \n
		Snippet: driver.configure.set_fcontrol(mode = enums.FanMode.HIGH) \n
		Selects a fan control mode. \n
			:param mode: LOW | NORMal | HIGH LOW: less cooling than in normal mode NORMal: default mode HIGH: more cooling than in normal mode
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FanMode)
		self._core.io.write(f'CONFigure:BASE:FCONtrol {param}')

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
