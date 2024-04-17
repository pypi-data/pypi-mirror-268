from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CommunicateCls:
	"""Communicate commands group definition. 19 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("communicate", core, parent)

	@property
	def net(self):
		"""net commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_net'):
			from .Net import NetCls
			self._net = NetCls(self._core, self._cmd_group)
		return self._net

	@property
	def gpib(self):
		"""gpib commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gpib'):
			from .Gpib import GpibCls
			self._gpib = GpibCls(self._core, self._cmd_group)
		return self._gpib

	@property
	def usb(self):
		"""usb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usb'):
			from .Usb import UsbCls
			self._usb = UsbCls(self._core, self._cmd_group)
		return self._usb

	@property
	def rsib(self):
		"""rsib commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsib'):
			from .Rsib import RsibCls
			self._rsib = RsibCls(self._core, self._cmd_group)
		return self._rsib

	@property
	def socket(self):
		"""socket commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_socket'):
			from .Socket import SocketCls
			self._socket = SocketCls(self._core, self._cmd_group)
		return self._socket

	@property
	def vxi(self):
		"""vxi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_vxi'):
			from .Vxi import VxiCls
			self._vxi = VxiCls(self._core, self._cmd_group)
		return self._vxi

	@property
	def hislip(self):
		"""hislip commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hislip'):
			from .Hislip import HislipCls
			self._hislip = HislipCls(self._core, self._cmd_group)
		return self._hislip

	def clone(self) -> 'CommunicateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CommunicateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
