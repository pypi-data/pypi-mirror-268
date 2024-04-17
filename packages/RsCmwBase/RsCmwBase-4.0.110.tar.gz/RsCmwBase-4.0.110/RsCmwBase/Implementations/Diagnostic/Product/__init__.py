from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProductCls:
	"""Product commands group definition. 9 total commands, 2 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("product", core, parent)

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	@property
	def macAddress(self):
		"""macAddress commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_macAddress'):
			from .MacAddress import MacAddressCls
			self._macAddress = MacAddressCls(self._core, self._cmd_group)
		return self._macAddress

	# noinspection PyTypeChecker
	class IdStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Manufacturer: str: No parameter help available
			- Device_Id: str: No parameter help available
			- Version: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Manufacturer'),
			ArgStruct.scalar_str('Device_Id'),
			ArgStruct.scalar_str('Version')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Manufacturer: str = None
			self.Device_Id: str = None
			self.Version: str = None

	def get_id(self) -> IdStruct:
		"""SCPI: DIAGnostic:PRODuct:ID \n
		Snippet: value: IdStruct = driver.diagnostic.product.get_id() \n
		No command help available \n
			:return: structure: for return value, see the help for IdStruct structure arguments.
		"""
		return self._core.io.query_struct('DIAGnostic:PRODuct:ID?', self.__class__.IdStruct())

	def get_description(self) -> bytes:
		"""SCPI: DIAGnostic:PRODuct:DESCription \n
		Snippet: value: bytes = driver.diagnostic.product.get_description() \n
		No command help available \n
			:return: product_description: No help available
		"""
		response = self._core.io.query_bin_block('DIAGnostic:PRODuct:DESCription?')
		return response

	def get_catalog(self) -> str:
		"""SCPI: DIAGnostic:PRODuct:CATalog \n
		Snippet: value: str = driver.diagnostic.product.get_catalog() \n
		No command help available \n
			:return: material_number: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:PRODuct:CATalog?')
		return trim_str_response(response)

	def get_select(self) -> str:
		"""SCPI: DIAGnostic:PRODuct:SELect \n
		Snippet: value: str = driver.diagnostic.product.get_select() \n
		No command help available \n
			:return: material_number: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:PRODuct:SELect?')
		return trim_str_response(response)

	def set_select(self, material_number: str) -> None:
		"""SCPI: DIAGnostic:PRODuct:SELect \n
		Snippet: driver.diagnostic.product.set_select(material_number = 'abc') \n
		No command help available \n
			:param material_number: No help available
		"""
		param = Conversions.value_to_quoted_str(material_number)
		self._core.io.write(f'DIAGnostic:PRODuct:SELect {param}')

	def get_group(self) -> str:
		"""SCPI: DIAGnostic:PRODuct:GROup \n
		Snippet: value: str = driver.diagnostic.product.get_group() \n
		No command help available \n
			:return: group: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:PRODuct:GROup?')
		return trim_str_response(response)

	def set_group(self, group: str) -> None:
		"""SCPI: DIAGnostic:PRODuct:GROup \n
		Snippet: driver.diagnostic.product.set_group(group = 'abc') \n
		No command help available \n
			:param group: No help available
		"""
		param = Conversions.value_to_quoted_str(group)
		self._core.io.write(f'DIAGnostic:PRODuct:GROup {param}')

	def clone(self) -> 'ProductCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ProductCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
