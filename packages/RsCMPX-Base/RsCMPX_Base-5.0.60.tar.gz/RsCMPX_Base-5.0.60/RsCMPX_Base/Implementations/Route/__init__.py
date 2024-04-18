from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RouteCls:
	"""Route commands group definition. 29 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("route", core, parent)

	@property
	def gprf(self):
		"""gprf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gprf'):
			from .Gprf import GprfCls
			self._gprf = GprfCls(self._core, self._cmd_group)
		return self._gprf

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def nrMmw(self):
		"""nrMmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrMmw'):
			from .NrMmw import NrMmwCls
			self._nrMmw = NrMmwCls(self._core, self._cmd_group)
		return self._nrMmw

	@property
	def nrDl(self):
		"""nrDl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrDl'):
			from .NrDl import NrDlCls
			self._nrDl = NrDlCls(self._core, self._cmd_group)
		return self._nrDl

	@property
	def lteDl(self):
		"""lteDl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lteDl'):
			from .LteDl import LteDlCls
			self._lteDl = LteDlCls(self._core, self._cmd_group)
		return self._lteDl

	@property
	def nrSub(self):
		"""nrSub commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrSub'):
			from .NrSub import NrSubCls
			self._nrSub = NrSubCls(self._core, self._cmd_group)
		return self._nrSub

	@property
	def cdma(self):
		"""cdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdma'):
			from .Cdma import CdmaCls
			self._cdma = CdmaCls(self._core, self._cmd_group)
		return self._cdma

	@property
	def niot(self):
		"""niot commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_niot'):
			from .Niot import NiotCls
			self._niot = NiotCls(self._core, self._cmd_group)
		return self._niot

	@property
	def uwb(self):
		"""uwb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uwb'):
			from .Uwb import UwbCls
			self._uwb = UwbCls(self._core, self._cmd_group)
		return self._uwb

	@property
	def wlan(self):
		"""wlan commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wlan'):
			from .Wlan import WlanCls
			self._wlan = WlanCls(self._core, self._cmd_group)
		return self._wlan

	@property
	def wpan(self):
		"""wpan commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wpan'):
			from .Wpan import WpanCls
			self._wpan = WpanCls(self._core, self._cmd_group)
		return self._wpan

	@property
	def bluetooth(self):
		"""bluetooth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bluetooth'):
			from .Bluetooth import BluetoothCls
			self._bluetooth = BluetoothCls(self._core, self._cmd_group)
		return self._bluetooth

	@property
	def gsm(self):
		"""gsm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gsm'):
			from .Gsm import GsmCls
			self._gsm = GsmCls(self._core, self._cmd_group)
		return self._gsm

	@property
	def wcdma(self):
		"""wcdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wcdma'):
			from .Wcdma import WcdmaCls
			self._wcdma = WcdmaCls(self._core, self._cmd_group)
		return self._wcdma

	def clone(self) -> 'RouteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RouteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
