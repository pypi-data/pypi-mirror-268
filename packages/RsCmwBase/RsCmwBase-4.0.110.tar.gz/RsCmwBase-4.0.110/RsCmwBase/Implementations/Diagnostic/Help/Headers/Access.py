from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AccessCls:
	"""Access commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("access", core, parent)

	# noinspection PyTypeChecker
	class EnabledStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Count: int: No parameter help available
			- Header: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Count'),
			ArgStruct('Header', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Count: int = None
			self.Header: List[str] = None

	def get_enabled(self) -> EnabledStruct:
		"""SCPI: DIAGnostic:HELP:HEADers:ACCess:ENABled \n
		Snippet: value: EnabledStruct = driver.diagnostic.help.headers.access.get_enabled() \n
		No command help available \n
			:return: structure: for return value, see the help for EnabledStruct structure arguments.
		"""
		return self._core.io.query_struct('DIAGnostic:HELP:HEADers:ACCess:ENABled?', self.__class__.EnabledStruct())

	# noinspection PyTypeChecker
	class DeniedStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Count: int: No parameter help available
			- Header: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Count'),
			ArgStruct('Header', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Count: int = None
			self.Header: List[str] = None

	def get_denied(self) -> DeniedStruct:
		"""SCPI: DIAGnostic:HELP:HEADers:ACCess:DENied \n
		Snippet: value: DeniedStruct = driver.diagnostic.help.headers.access.get_denied() \n
		No command help available \n
			:return: structure: for return value, see the help for DeniedStruct structure arguments.
		"""
		return self._core.io.query_struct('DIAGnostic:HELP:HEADers:ACCess:DENied?', self.__class__.DeniedStruct())
