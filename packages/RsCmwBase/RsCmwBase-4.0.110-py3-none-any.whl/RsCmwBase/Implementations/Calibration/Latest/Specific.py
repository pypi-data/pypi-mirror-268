from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpecificCls:
	"""Specific commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("specific", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Date: str: string Date of the calibration
			- Time: str: string Time of the calibration"""
		__meta_args_list = [
			ArgStruct.scalar_str('Date'),
			ArgStruct.scalar_str('Time')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Date: str = None
			self.Time: str = None

	def get(self, mode: enums.Type) -> GetStruct:
		"""SCPI: CALibration:BASE:LATest:SPECific \n
		Snippet: value: GetStruct = driver.calibration.latest.specific.get(mode = enums.Type.CALibration) \n
		Query date and time of the latest calibration of the specified type. \n
			:param mode: FSCorrection | UCORrection | CALibration | OGCal Type of the calibration for which information is queried. FSCorrection: Correction performed in factory or service UCORrection: Correction performed by a customer CALibration: Verification in the factory OGCal: Verification by the service (outgoing calibration)
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(mode, enums.Type)
		return self._core.io.query_struct(f'CALibration:BASE:LATest:SPECific? {param}', self.__class__.GetStruct())
