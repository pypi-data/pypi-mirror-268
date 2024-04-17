from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnodeCls:
	"""Snode commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snode", core, parent)

	def get_nname(self) -> str:
		"""SCPI: SENSe:BASE:IPSet:SNODe:NNAMe \n
		Snippet: value: str = driver.sense.ipSet.snode.get_nname() \n
		Queries the subnet node name of the R&S CMW. \n
			:return: name: string
		"""
		response = self._core.io.query_str('SENSe:BASE:IPSet:SNODe:NNAMe?')
		return trim_str_response(response)

	def get_ntype(self) -> str:
		"""SCPI: SENSe:BASE:IPSet:SNODe:NTYPe \n
		Snippet: value: str = driver.sense.ipSet.snode.get_ntype() \n
		Queries the subnet node type of the R&S CMW. \n
			:return: type_py: string 'CMW'
		"""
		response = self._core.io.query_str('SENSe:BASE:IPSet:SNODe:NTYPe?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	class NsegmentStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Selected_Segment: enums.Segment: A | B | C Selected network segment
			- Ip_Address: str: string First two IP address octets of the subnet
			- Subnet_Mask: str: string Used subnet mask (fixed value)"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Selected_Segment', enums.Segment),
			ArgStruct.scalar_str('Ip_Address'),
			ArgStruct.scalar_str('Subnet_Mask')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Selected_Segment: enums.Segment = None
			self.Ip_Address: str = None
			self.Subnet_Mask: str = None

	def get_nsegment(self) -> NsegmentStruct:
		"""SCPI: SENSe:BASE:IPSet:SNODe:NSEGment \n
		Snippet: value: NsegmentStruct = driver.sense.ipSet.snode.get_nsegment() \n
		Queries information about the selected network segment and the resulting subnet properties. \n
			:return: structure: for return value, see the help for NsegmentStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:BASE:IPSet:SNODe:NSEGment?', self.__class__.NsegmentStruct())
