from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxCls:
	"""Tx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Connector_Bench: str: No parameter help available
			- Table_1: str: No parameter help available
			- Table_2: str: No parameter help available
			- Table_3: str: No parameter help available
			- Table_4: str: No parameter help available
			- Table_5: str: No parameter help available
			- Table_6: str: No parameter help available
			- Table_7: str: No parameter help available
			- Table_8: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Connector_Bench'),
			ArgStruct.scalar_str('Table_1'),
			ArgStruct.scalar_str_optional('Table_2'),
			ArgStruct.scalar_str_optional('Table_3'),
			ArgStruct.scalar_str_optional('Table_4'),
			ArgStruct.scalar_str_optional('Table_5'),
			ArgStruct.scalar_str_optional('Table_6'),
			ArgStruct.scalar_str_optional('Table_7'),
			ArgStruct.scalar_str_optional('Table_8')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Connector_Bench: str = None
			self.Table_1: str = None
			self.Table_2: str = None
			self.Table_3: str = None
			self.Table_4: str = None
			self.Table_5: str = None
			self.Table_6: str = None
			self.Table_7: str = None
			self.Table_8: str = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: CONFigure:CMWS:FDCorrection:ACTivate:TX \n
		Snippet with structure: \n
		structure = driver.configure.singleCmw.freqCorrection.activate.tx.SetStruct() \n
		structure.Connector_Bench: str = rawAbc \n
		structure.Table_1: str = 'abc' \n
		structure.Table_2: str = 'abc' \n
		structure.Table_3: str = 'abc' \n
		structure.Table_4: str = 'abc' \n
		structure.Table_5: str = 'abc' \n
		structure.Table_6: str = 'abc' \n
		structure.Table_7: str = 'abc' \n
		structure.Table_8: str = 'abc' \n
		driver.configure.singleCmw.freqCorrection.activate.tx.set(structure) \n
		No command help available \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:CMWS:FDCorrection:ACTivate:TX', structure)
