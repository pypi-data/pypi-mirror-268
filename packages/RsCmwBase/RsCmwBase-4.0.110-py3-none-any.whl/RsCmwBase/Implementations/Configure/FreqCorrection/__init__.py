from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqCorrectionCls:
	"""FreqCorrection commands group definition. 16 total commands, 3 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("freqCorrection", core, parent)

	@property
	def correctionTable(self):
		"""correctionTable commands group. 9 Sub-classes, 1 commands."""
		if not hasattr(self, '_correctionTable'):
			from .CorrectionTable import CorrectionTableCls
			self._correctionTable = CorrectionTableCls(self._core, self._cmd_group)
		return self._correctionTable

	@property
	def activate(self):
		"""activate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_activate'):
			from .Activate import ActivateCls
			self._activate = ActivateCls(self._core, self._cmd_group)
		return self._activate

	@property
	def usage(self):
		"""usage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .Usage import UsageCls
			self._usage = UsageCls(self._core, self._cmd_group)
		return self._usage

	def save(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:SAV \n
		Snippet: driver.configure.freqCorrection.save(table_path = rawAbc) \n
		Saves the correction tables for a selected subinstrument from the RAM to the system drive. This action is performed
		automatically when the R&S CMW application software is closed, for example, by pressing the standby key. However, you can
		use the command to save your work manually after creating or configuring correction tables. \n
			:param table_path: string Selects the subinstrument If omitted: subinstrument addressed by the remote channel. 'instn': subinstrument n+1
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_str(table_path)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:SAV {param}'.strip())

	def recall(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:RCL \n
		Snippet: driver.configure.freqCorrection.recall(table_path = rawAbc) \n
		Loads all correction tables for a selected subinstrument from the system drive into the RAM. This action is performed
		automatically when the R&S CMW application software is started. However, you can use the command to retrieve the
		correction tables after the disk contents have been modified. Or you can use it to undo changes and fall back to the
		tables stored on the system drive. \n
			:param table_path: string Selects the subinstrument If omitted: subinstrument addressed by the remote channel. 'instn': subinstrument n+1
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_str(table_path)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:RCL {param}'.strip())

	def deactivate(self, connector: str, direction: enums.RxTxDirection = None, rf_converter: enums.RfConverterInPath = None) -> None:
		"""SCPI: CONFigure:FDCorrection:DEACtivate \n
		Snippet: driver.configure.freqCorrection.deactivate(connector = rawAbc, direction = enums.RxTxDirection.RX, rf_converter = enums.RfConverterInPath.RF1) \n
		Deactivates any correction tables for a specific RF connector or a specific connector / converter combination.
		For bidirectional connectors, the tables can be deactivated for both directions or for one direction. \n
			:param connector: Selects a single RF connector For possible connector values, see 'Values for RF path selection'.
			:param direction: RXTX | RX | TX Specifies the direction for which the tables are deactivated. RX means input and TX means output. For a pure output connector, RX is ignored. RXTX: both directions (for output connector same effect as TX) RX: input (not allowed for output connector) TX: output Default: RXTX
			:param rf_converter: RF1 | RF2 | RF3 | RF4 RX and TX module in the path (RFn = RXn, TXn)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.RawString), ArgSingle('direction', direction, DataType.Enum, enums.RxTxDirection, is_optional=True), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.RfConverterInPath, is_optional=True))
		self._core.io.write(f'CONFigure:FDCorrection:DEACtivate {param}'.rstrip())

	def deactivate_all(self, direction: enums.RxTxDirection = None, table_path: str = None) -> None:
		"""SCPI: CONFigure:FDCorrection:DEACtivate:ALL \n
		Snippet: driver.configure.freqCorrection.deactivate_all(direction = enums.RxTxDirection.RX, table_path = rawAbc) \n
		Deactivates all correction tables for all RF connectors of a selected subinstrument. For bidirectional connectors, the
		tables can be deactivated for both directions or for one direction. \n
			:param direction: RXTX | RX | TX Specifies the direction for which the tables are deactivated. RX means input and TX means output. For a pure output connector, RX is ignored. RXTX: both directions (for output connector same effect as TX) RX: input (not allowed for output connector) TX: output Default: RXTX
			:param table_path: string Selects the subinstrument If omitted: subinstrument addressed by the remote channel. 'instn': subinstrument n+1
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('direction', direction, DataType.Enum, enums.RxTxDirection, is_optional=True), ArgSingle('table_path', table_path, DataType.RawString, None, is_optional=True))
		self._core.io.write(f'CONFigure:FDCorrection:DEACtivate:ALL {param}'.rstrip())

	def clone(self) -> 'FreqCorrectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FreqCorrectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
