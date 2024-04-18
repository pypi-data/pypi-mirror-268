from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SystemCls:
	"""System commands group definition. 17 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	@property
	def reset(self):
		"""reset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reset'):
			from .Reset import ResetCls
			self._reset = ResetCls(self._core, self._cmd_group)
		return self._reset

	@property
	def save(self):
		"""save commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_save'):
			from .Save import SaveCls
			self._save = SaveCls(self._core, self._cmd_group)
		return self._save

	@property
	def recall(self):
		"""recall commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_recall'):
			from .Recall import RecallCls
			self._recall = RecallCls(self._core, self._cmd_group)
		return self._recall

	@property
	def control(self):
		"""control commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import ControlCls
			self._control = ControlCls(self._core, self._cmd_group)
		return self._control

	@property
	def rrhead(self):
		"""rrhead commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rrhead'):
			from .Rrhead import RrheadCls
			self._rrhead = RrheadCls(self._core, self._cmd_group)
		return self._rrhead

	@property
	def attenuation(self):
		"""attenuation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_attenuation'):
			from .Attenuation import AttenuationCls
			self._attenuation = AttenuationCls(self._core, self._cmd_group)
		return self._attenuation

	@property
	def edevice(self):
		"""edevice commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edevice'):
			from .Edevice import EdeviceCls
			self._edevice = EdeviceCls(self._core, self._cmd_group)
		return self._edevice

	@property
	def vse(self):
		"""vse commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_vse'):
			from .Vse import VseCls
			self._vse = VseCls(self._core, self._cmd_group)
		return self._vse

	@property
	def z310(self):
		"""z310 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_z310'):
			from .Z310 import Z310Cls
			self._z310 = Z310Cls(self._core, self._cmd_group)
		return self._z310

	@property
	def z320(self):
		"""z320 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_z320'):
			from .Z320 import Z320Cls
			self._z320 = Z320Cls(self._core, self._cmd_group)
		return self._z320

	@property
	def rf42(self):
		"""rf42 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rf42'):
			from .Rf42 import Rf42Cls
			self._rf42 = Rf42Cls(self._core, self._cmd_group)
		return self._rf42

	def clone(self) -> 'SystemCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SystemCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
