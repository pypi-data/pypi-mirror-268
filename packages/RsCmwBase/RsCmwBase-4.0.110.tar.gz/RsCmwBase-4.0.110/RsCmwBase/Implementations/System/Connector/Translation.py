from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TranslationCls:
	"""Translation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("translation", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Virtual_Connector: str: Returned virtual connector name
			- Absolute_Connector: str: Returned physical connector name"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Virtual_Connector'),
			ArgStruct.scalar_raw_str('Absolute_Connector')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Virtual_Connector: str = None
			self.Absolute_Connector: str = None

	def get(self, connector: str) -> GetStruct:
		"""SCPI: SYSTem:CONNector:TRANslation \n
		Snippet: value: GetStruct = driver.system.connector.translation.get(connector = rawAbc) \n
		Queries the relation between physical and virtual connector names. You can query this relation for either a physical or a
		virtual name. As a result, both physical and virtual name are returned. For background information and possible connector
		values, see 'Values for RF path selection'. \n
			:param connector: Physical or virtual connector name to be queried
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_str(connector)
		return self._core.io.query_struct(f'SYSTem:CONNector:TRANslation? {param}', self.__class__.GetStruct())
