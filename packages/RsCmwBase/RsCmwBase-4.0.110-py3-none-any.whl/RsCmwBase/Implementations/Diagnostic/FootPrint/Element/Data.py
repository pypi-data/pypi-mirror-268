from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Stype_Name: str: No parameter help available
			- Spart_Name: str: No parameter help available
			- Efunctionality: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Stype_Name'),
			ArgStruct.scalar_str('Spart_Name'),
			ArgStruct.scalar_int('Efunctionality')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Stype_Name: str = None
			self.Spart_Name: str = None
			self.Efunctionality: int = None

	def get(self, ielement_id: float) -> GetStruct:
		"""SCPI: DIAGnostic:FOOTprint:ELEMent:DATA \n
		Snippet: value: GetStruct = driver.diagnostic.footPrint.element.data.get(ielement_id = 1.0) \n
		No command help available \n
			:param ielement_id: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(ielement_id)
		return self._core.io.query_struct(f'DIAGnostic:FOOTprint:ELEMent:DATA? {param}', self.__class__.GetStruct())
