from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OperatingCls:
	"""Operating commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("operating", core, parent)

	def get_internal(self) -> float:
		"""SCPI: SENSe:BASE:TEMPerature:OPERating:INTernal \n
		Snippet: value: float = driver.sense.temperature.operating.get_internal() \n
		Queries the temperature within the instrument. The returned value indicates the average of the temperatures measured at
		the individual RF modules. The recommended temperature range is illustrated in the following figure. \n
			:return: temperature: float Temperature in degrees Unit: °C
		"""
		response = self._core.io.query_str('SENSe:BASE:TEMPerature:OPERating:INTernal?')
		return Conversions.str_to_float(response)
