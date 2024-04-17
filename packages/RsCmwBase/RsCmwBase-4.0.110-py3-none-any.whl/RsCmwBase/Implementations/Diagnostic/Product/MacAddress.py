from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MacAddressCls:
	"""MacAddress commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("macAddress", core, parent)

	def set_store(self, target: enums.StoragePlace) -> None:
		"""SCPI: DIAGnostic:PRODuct:MACaddress:STORe \n
		Snippet: driver.diagnostic.product.macAddress.set_store(target = enums.StoragePlace.EEPRom) \n
		No command help available \n
			:param target: No help available
		"""
		param = Conversions.enum_scalar_to_str(target, enums.StoragePlace)
		self._core.io.write(f'DIAGnostic:PRODuct:MACaddress:STORe {param}')

	def set_restore(self, source: enums.StoragePlace) -> None:
		"""SCPI: DIAGnostic:PRODuct:MACaddress:RESTore \n
		Snippet: driver.diagnostic.product.macAddress.set_restore(source = enums.StoragePlace.EEPRom) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.StoragePlace)
		self._core.io.write(f'DIAGnostic:PRODuct:MACaddress:RESTore {param}')

	def get_value(self) -> str:
		"""SCPI: DIAGnostic:PRODuct:MACaddress \n
		Snippet: value: str = driver.diagnostic.product.macAddress.get_value() \n
		No command help available \n
			:return: mac_addr: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:PRODuct:MACaddress?')
		return trim_str_response(response)
