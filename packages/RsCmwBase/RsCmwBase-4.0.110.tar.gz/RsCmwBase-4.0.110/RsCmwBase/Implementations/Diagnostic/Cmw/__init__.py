from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmwCls:
	"""Cmw commands group definition. 2 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: CmwVariant, default value after init: CmwVariant.Cmw1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmw", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cmwVariant_get', 'repcap_cmwVariant_set', repcap.CmwVariant.Cmw1)

	def repcap_cmwVariant_set(self, cmwVariant: repcap.CmwVariant) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CmwVariant.Default
		Default value after init: CmwVariant.Cmw1"""
		self._cmd_group.set_repcap_enum_value(cmwVariant)

	def repcap_cmwVariant_get(self) -> repcap.CmwVariant:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def ledTest(self):
		"""ledTest commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ledTest'):
			from .LedTest import LedTestCls
			self._ledTest = LedTestCls(self._core, self._cmd_group)
		return self._ledTest

	def clone(self) -> 'CmwCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CmwCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
