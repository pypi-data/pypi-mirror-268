from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ParserCls:
	"""Parser commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("parser", core, parent)

	def set(self, benable: bool, fileNr=repcap.FileNr.Default) -> None:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:PARSer \n
		Snippet: driver.trace.remote.mode.file.parser.set(benable = False, fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param benable: No help available
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
		"""
		param = Conversions.bool_to_str(benable)
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		self._core.io.write(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:PARSer {param}')

	def get(self, fileNr=repcap.FileNr.Default) -> bool:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:PARSer \n
		Snippet: value: bool = driver.trace.remote.mode.file.parser.get(fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
			:return: benable: No help available"""
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		response = self._core.io.query_str(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:PARSer?')
		return Conversions.str_to_bool(response)
