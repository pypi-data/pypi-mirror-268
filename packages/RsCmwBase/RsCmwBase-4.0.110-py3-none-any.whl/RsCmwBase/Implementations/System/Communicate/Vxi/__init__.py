from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VxiCls:
	"""Vxi commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: VxiInstance, default value after init: VxiInstance.Inst1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vxi", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_vxiInstance_get', 'repcap_vxiInstance_set', repcap.VxiInstance.Inst1)

	def repcap_vxiInstance_set(self, vxiInstance: repcap.VxiInstance) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to VxiInstance.Default
		Default value after init: VxiInstance.Inst1"""
		self._cmd_group.set_repcap_enum_value(vxiInstance)

	def repcap_vxiInstance_get(self) -> repcap.VxiInstance:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def vresource(self):
		"""vresource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vresource'):
			from .Vresource import VresourceCls
			self._vresource = VresourceCls(self._core, self._cmd_group)
		return self._vresource

	@property
	def gtr(self):
		"""gtr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gtr'):
			from .Gtr import GtrCls
			self._gtr = GtrCls(self._core, self._cmd_group)
		return self._gtr

	def clone(self) -> 'VxiCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VxiCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
