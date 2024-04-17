from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CreateCls:
	"""Create commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("create", core, parent)

	def set(self, table_name: str, frequency: List[float] = None, correction: List[float] = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:CREate \n
		Snippet: driver.configure.freqCorrection.correctionTable.create.set(table_name = 'abc', frequency = [1.1, 2.2, 3.3], correction = [1.1, 2.2, 3.3]) \n
		Creates a correction table for frequency-dependent attenuation and stores it in the RAM. If a table with the given name
		exists for the addressed subinstrument, it is overwritten. The parameter pairs <Frequency>, <Correction> are used to fill
		the table. A command with an incomplete pair (e.g. <Frequency> without <Correction>) is ignored completely.
		To add entries to an existing table, see method RsCmwBase.Configure.FreqCorrection.CorrectionTable.Add.set. You can enter
		parameter pairs in any order. The table entries (pairs) are automatically sorted from lowest to highest frequency.
		For the supported frequency range, see 'Frequency range'. \n
			:param table_name: string The table name is used to identify the table in other commands and to store the table on the system drive. The string must comply to Windows™ file name conventions, see 'Mass memory commands'. You can add the prefix 'instn/' to address subinstrument number n+1. Example: 'inst2/mytable' means 'mytable' for subinstrument number 3.
			:param frequency: numeric Unit: Hz
			:param correction: numeric Range: -50 dB to 90 dB, Unit: dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('table_name', table_name, DataType.String), ArgSingle('frequency', frequency, DataType.FloatList, None, True, True, 1), ArgSingle('correction', correction, DataType.FloatList, None, True, True, 1))
		self._core.io.write(f'CONFigure:BASE:FDCorrection:CTABle:CREate {param}'.rstrip())
