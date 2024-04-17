from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Cmw_1: enums.CmwCurrentStatus: STBY | SALone | MCMW | ERRor | MCCNconnected | PCINconnected STBY: standalone mode, standby state SALone: standalone mode, ready state MCMW: multi-CMW mode, ready state ERRor: an error occurred, a state change failed MCCNconnected: there is no MCC connection to the instrument, so the current state cannot be queried or changed PCINconnected: there is no PCIe connection to the instrument
			- Cmw_2: enums.CmwCurrentStatus: STBY | SALone | MCMW | ERRor | MCCNconnected | PCINconnected
			- Cmw_3: enums.CmwCurrentStatus: STBY | SALone | MCMW | ERRor | MCCNconnected | PCINconnected
			- Cmw_4: enums.CmwCurrentStatus: STBY | SALone | MCMW | ERRor | MCCNconnected | PCINconnected"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Cmw_1', enums.CmwCurrentStatus),
			ArgStruct.scalar_enum('Cmw_2', enums.CmwCurrentStatus),
			ArgStruct.scalar_enum('Cmw_3', enums.CmwCurrentStatus),
			ArgStruct.scalar_enum('Cmw_4', enums.CmwCurrentStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cmw_1: enums.CmwCurrentStatus = None
			self.Cmw_2: enums.CmwCurrentStatus = None
			self.Cmw_3: enums.CmwCurrentStatus = None
			self.Cmw_4: enums.CmwCurrentStatus = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BASE:MCMW:STATe \n
		Snippet: value: FetchStruct = driver.multiCmw.state.fetch() \n
		Queries the current state of CMW 1 to CMW 4. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BASE:MCMW:STATe?', self.__class__.FetchStruct())
