from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FileCls:
	"""File commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def get_size(self) -> int:
		"""SCPI: DIAGnostic:RECord:MACRo:FILE:SIZE \n
		Snippet: value: int = driver.diagnostic.record.macro.file.get_size() \n
		No command help available \n
			:return: ifile_size: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:RECord:MACRo:FILE:SIZE?')
		return Conversions.str_to_int(response)

	def set_size(self, ifile_size: int) -> None:
		"""SCPI: DIAGnostic:RECord:MACRo:FILE:SIZE \n
		Snippet: driver.diagnostic.record.macro.file.set_size(ifile_size = 1) \n
		No command help available \n
			:param ifile_size: No help available
		"""
		param = Conversions.decimal_value_to_str(ifile_size)
		self._core.io.write(f'DIAGnostic:RECord:MACRo:FILE:SIZE {param}')

	# noinspection PyTypeChecker
	class FilterPyStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Binput: bool: No parameter help available
			- Boutput: bool: No parameter help available
			- Berror: bool: No parameter help available
			- Btrigger: bool: No parameter help available
			- Bdevice_Clear: bool: No parameter help available
			- Bstatus_Register: bool: No parameter help available
			- Bconnection: bool: No parameter help available
			- Bremote_Local_Events: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Binput'),
			ArgStruct.scalar_bool('Boutput'),
			ArgStruct.scalar_bool('Berror'),
			ArgStruct.scalar_bool('Btrigger'),
			ArgStruct.scalar_bool('Bdevice_Clear'),
			ArgStruct.scalar_bool('Bstatus_Register'),
			ArgStruct.scalar_bool('Bconnection'),
			ArgStruct.scalar_bool('Bremote_Local_Events')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Binput: bool = None
			self.Boutput: bool = None
			self.Berror: bool = None
			self.Btrigger: bool = None
			self.Bdevice_Clear: bool = None
			self.Bstatus_Register: bool = None
			self.Bconnection: bool = None
			self.Bremote_Local_Events: bool = None

	def get_filter_py(self) -> FilterPyStruct:
		"""SCPI: DIAGnostic:RECord:MACRo:FILE:FILTer \n
		Snippet: value: FilterPyStruct = driver.diagnostic.record.macro.file.get_filter_py() \n
		No command help available \n
			:return: structure: for return value, see the help for FilterPyStruct structure arguments.
		"""
		return self._core.io.query_struct('DIAGnostic:RECord:MACRo:FILE:FILTer?', self.__class__.FilterPyStruct())

	def set_filter_py(self, value: FilterPyStruct) -> None:
		"""SCPI: DIAGnostic:RECord:MACRo:FILE:FILTer \n
		Snippet with structure: \n
		structure = driver.diagnostic.record.macro.file.FilterPyStruct() \n
		structure.Binput: bool = False \n
		structure.Boutput: bool = False \n
		structure.Berror: bool = False \n
		structure.Btrigger: bool = False \n
		structure.Bdevice_Clear: bool = False \n
		structure.Bstatus_Register: bool = False \n
		structure.Bconnection: bool = False \n
		structure.Bremote_Local_Events: bool = False \n
		driver.diagnostic.record.macro.file.set_filter_py(value = structure) \n
		No command help available \n
			:param value: see the help for FilterPyStruct structure arguments.
		"""
		self._core.io.write_struct('DIAGnostic:RECord:MACRo:FILE:FILTer', value)
