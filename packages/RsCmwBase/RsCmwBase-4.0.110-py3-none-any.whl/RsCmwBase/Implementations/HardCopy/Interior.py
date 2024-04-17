from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InteriorCls:
	"""Interior commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interior", core, parent)

	def get_data(self) -> bytes:
		"""SCPI: HCOPy:INTerior:DATA \n
		Snippet: value: bytes = driver.hardCopy.interior.get_data() \n
		Captures a screenshot and returns the result in block data format. method RsCmwBase.HardCopy.data captures the entire
		window, method RsCmwBase.HardCopy.Interior.data only the interior of the window. It is recommended to 'switch on' the
		display before sending this command, see method RsCmwBase.System.Display.update. \n
			:return: data: block Screenshot in block data format.
		"""
		response = self._core.io.query_bin_block('HCOPy:INTerior:DATA?')
		return response

	def set_file(self, filename: str) -> None:
		"""SCPI: HCOPy:INTerior:FILE \n
		Snippet: driver.hardCopy.interior.set_file(filename = 'abc') \n
		Captures a screenshot and stores it to the specified file. method RsCmwBase.HardCopy.file captures the entire window,
		method RsCmwBase.HardCopy.Interior.file only the interior of the window. If a 'Remote' dialog is displayed instead of the
		normal display contents, this command switches on the display before taking a screenshot, and afterwards off again. \n
			:param filename: string Absolute path and name of the file. The file name extension is added automatically according to the configured format (see method RsCmwBase.HardCopy.Device.formatPy) . Aliases are allowed (see method RsCmwBase.MassMemory.aliases) . Wildcards are not allowed.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'HCOPy:INTerior:FILE {param}')
