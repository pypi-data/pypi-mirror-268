from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SenseCls:
	"""Sense commands group definition. 13 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def ipSet(self):
		"""ipSet commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSet'):
			from .IpSet import IpSetCls
			self._ipSet = IpSetCls(self._core, self._cmd_group)
		return self._ipSet

	@property
	def temperature(self):
		"""temperature commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_temperature'):
			from .Temperature import TemperatureCls
			self._temperature = TemperatureCls(self._core, self._cmd_group)
		return self._temperature

	@property
	def reference(self):
		"""reference commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import ReferenceCls
			self._reference = ReferenceCls(self._core, self._cmd_group)
		return self._reference

	@property
	def firmwareUpdate(self):
		"""firmwareUpdate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_firmwareUpdate'):
			from .FirmwareUpdate import FirmwareUpdateCls
			self._firmwareUpdate = FirmwareUpdateCls(self._core, self._cmd_group)
		return self._firmwareUpdate

	def clone(self) -> 'SenseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SenseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
