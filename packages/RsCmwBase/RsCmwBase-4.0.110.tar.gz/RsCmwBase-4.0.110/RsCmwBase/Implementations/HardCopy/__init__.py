from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HardCopyCls:
	"""HardCopy commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hardCopy", core, parent)

	@property
	def device(self):
		"""device commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_device'):
			from .Device import DeviceCls
			self._device = DeviceCls(self._core, self._cmd_group)
		return self._device

	@property
	def interior(self):
		"""interior commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_interior'):
			from .Interior import InteriorCls
			self._interior = InteriorCls(self._core, self._cmd_group)
		return self._interior

	def get_data(self) -> bytes:
		"""SCPI: HCOPy:DATA \n
		Snippet: value: bytes = driver.hardCopy.get_data() \n
		Captures a screenshot and returns the result in block data format. method RsCmwBase.HardCopy.data captures the entire
		window, method RsCmwBase.HardCopy.Interior.data only the interior of the window. It is recommended to 'switch on' the
		display before sending this command, see method RsCmwBase.System.Display.update. \n
			:return: data: block Screenshot in block data format.
		"""
		response = self._core.io.query_bin_block('HCOPy:DATA?')
		return response

	def set_file(self, filename: str) -> None:
		"""SCPI: HCOPy:FILE \n
		Snippet: driver.hardCopy.set_file(filename = 'abc') \n
		Captures a screenshot and stores it to the specified file. method RsCmwBase.HardCopy.file captures the entire window,
		method RsCmwBase.HardCopy.Interior.file only the interior of the window. If a 'Remote' dialog is displayed instead of the
		normal display contents, this command switches on the display before taking a screenshot, and afterwards off again. \n
			:param filename: string Absolute path and name of the file. The file name extension is added automatically according to the configured format (see method RsCmwBase.HardCopy.Device.formatPy) . Aliases are allowed (see method RsCmwBase.MassMemory.aliases) . Wildcards are not allowed.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'HCOPy:FILE {param}')

	def clone(self) -> 'HardCopyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HardCopyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
