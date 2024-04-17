from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ActivateCls:
	"""Activate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("activate", core, parent)

	def set(self, connector: str, table: str, direction: enums.RxTxDirection = None, rf_converter: enums.RfConverterInPath = None) -> None:
		"""SCPI: CONFigure:FDCorrection:ACTivate \n
		Snippet: driver.configure.freqCorrection.activate.set(connector = rawAbc, table = 'abc', direction = enums.RxTxDirection.RX, rf_converter = enums.RfConverterInPath.RF1) \n
		Activates a correction table for one or more signal paths using a specific RF connector. For bidirectional connectors,
		the table can be applied to both directions or to one direction. It is possible to assign different tables to the
		directions of a bidirectional connector. A table can be assigned to all paths using the connector or to paths with a
		specific connector / converter combination. \n
			:param connector: Selects a single RF connector For possible connector values, see 'Values for RF path selection'.
			:param table: string To display a list of existing tables, use the command CONFigure:BASE:FDCorrection:CTABle:CATalog?. You can add the prefix 'instn/' to address subinstrument number n+1.
			:param direction: RXTX | RX | TX Specifies the direction to which the correction table is applied. RX means input and TX means output. For a pure output connector, RX is ignored. RXTX: both directions (for output connector same effect as TX) RX: input (not allowed for output connector) TX: output Default: RXTX
			:param rf_converter: RF1 | RF2 | RF3 | RF4 RX or TX module in the path (RFn = RXn / TXn) If omitted, the table is activated for any paths using the specified connector, independent of the used RX/TX module.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.RawString), ArgSingle('table', table, DataType.String), ArgSingle('direction', direction, DataType.Enum, enums.RxTxDirection, is_optional=True), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.RfConverterInPath, is_optional=True))
		self._core.io.write(f'CONFigure:FDCorrection:ACTivate {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Table_Rx: str: No parameter help available
			- Table_Tx: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Table_Rx'),
			ArgStruct.scalar_str('Table_Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Table_Rx: str = None
			self.Table_Tx: str = None

	def get(self, connector: str) -> GetStruct:
		"""SCPI: CONFigure:FDCorrection:ACTivate \n
		Snippet: value: GetStruct = driver.configure.freqCorrection.activate.get(connector = rawAbc) \n
		Activates a correction table for one or more signal paths using a specific RF connector. For bidirectional connectors,
		the table can be applied to both directions or to one direction. It is possible to assign different tables to the
		directions of a bidirectional connector. A table can be assigned to all paths using the connector or to paths with a
		specific connector / converter combination. \n
			:param connector: Selects a single RF connector For possible connector values, see 'Values for RF path selection'.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_str(connector)
		return self._core.io.query_struct(f'CONFigure:FDCorrection:ACTivate? {param}', self.__class__.GetStruct())
