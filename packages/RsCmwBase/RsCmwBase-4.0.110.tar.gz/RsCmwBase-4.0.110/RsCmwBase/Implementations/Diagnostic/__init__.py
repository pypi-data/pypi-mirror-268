from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DiagnosticCls:
	"""Diagnostic commands group definition. 68 total commands, 17 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("diagnostic", core, parent)

	@property
	def routing(self):
		"""routing commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_routing'):
			from .Routing import RoutingCls
			self._routing = RoutingCls(self._core, self._cmd_group)
		return self._routing

	@property
	def eeprom(self):
		"""eeprom commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eeprom'):
			from .Eeprom import EepromCls
			self._eeprom = EepromCls(self._core, self._cmd_group)
		return self._eeprom

	@property
	def bgInfo(self):
		"""bgInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bgInfo'):
			from .BgInfo import BgInfoCls
			self._bgInfo = BgInfoCls(self._core, self._cmd_group)
		return self._bgInfo

	@property
	def singleCmw(self):
		"""singleCmw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmwCls
			self._singleCmw = SingleCmwCls(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def cmw(self):
		"""cmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmw'):
			from .Cmw import CmwCls
			self._cmw = CmwCls(self._core, self._cmd_group)
		return self._cmw

	@property
	def log(self):
		"""log commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_log'):
			from .Log import LogCls
			self._log = LogCls(self._core, self._cmd_group)
		return self._log

	@property
	def footPrint(self):
		"""footPrint commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_footPrint'):
			from .FootPrint import FootPrintCls
			self._footPrint = FootPrintCls(self._core, self._cmd_group)
		return self._footPrint

	@property
	def status(self):
		"""status commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_status'):
			from .Status import StatusCls
			self._status = StatusCls(self._core, self._cmd_group)
		return self._status

	@property
	def error(self):
		"""error commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_error'):
			from .Error import ErrorCls
			self._error = ErrorCls(self._core, self._cmd_group)
		return self._error

	@property
	def help(self):
		"""help commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_help'):
			from .Help import HelpCls
			self._help = HelpCls(self._core, self._cmd_group)
		return self._help

	@property
	def access(self):
		"""access commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_access'):
			from .Access import AccessCls
			self._access = AccessCls(self._core, self._cmd_group)
		return self._access

	@property
	def instrument(self):
		"""instrument commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_instrument'):
			from .Instrument import InstrumentCls
			self._instrument = InstrumentCls(self._core, self._cmd_group)
		return self._instrument

	@property
	def kremote(self):
		"""kremote commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_kremote'):
			from .Kremote import KremoteCls
			self._kremote = KremoteCls(self._core, self._cmd_group)
		return self._kremote

	@property
	def compass(self):
		"""compass commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_compass'):
			from .Compass import CompassCls
			self._compass = CompassCls(self._core, self._cmd_group)
		return self._compass

	@property
	def record(self):
		"""record commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_record'):
			from .Record import RecordCls
			self._record = RecordCls(self._core, self._cmd_group)
		return self._record

	@property
	def pias(self):
		"""pias commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_pias'):
			from .Pias import PiasCls
			self._pias = PiasCls(self._core, self._cmd_group)
		return self._pias

	@property
	def product(self):
		"""product commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_product'):
			from .Product import ProductCls
			self._product = ProductCls(self._core, self._cmd_group)
		return self._product

	def set_sdbm(self, text: str) -> None:
		"""SCPI: DIAGnostic:SDBM \n
		Snippet: driver.diagnostic.set_sdbm(text = 'abc') \n
		No command help available \n
			:param text: No help available
		"""
		param = Conversions.value_to_quoted_str(text)
		self._core.io.write(f'DIAGnostic:SDBM {param}')

	def clone(self) -> 'DiagnosticCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DiagnosticCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
