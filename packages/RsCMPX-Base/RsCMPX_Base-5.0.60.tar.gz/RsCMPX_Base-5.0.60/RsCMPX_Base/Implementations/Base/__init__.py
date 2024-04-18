from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BaseCls:
	"""Base commands group definition. 51 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def multiCmw(self):
		"""multiCmw commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiCmw'):
			from .MultiCmw import MultiCmwCls
			self._multiCmw = MultiCmwCls(self._core, self._cmd_group)
		return self._multiCmw

	@property
	def ipc(self):
		"""ipc commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipc'):
			from .Ipc import IpcCls
			self._ipc = IpcCls(self._core, self._cmd_group)
		return self._ipc

	@property
	def correction(self):
		"""correction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import CorrectionCls
			self._correction = CorrectionCls(self._core, self._cmd_group)
		return self._correction

	@property
	def salignment(self):
		"""salignment commands group. 7 Sub-classes, 4 commands."""
		if not hasattr(self, '_salignment'):
			from .Salignment import SalignmentCls
			self._salignment = SalignmentCls(self._core, self._cmd_group)
		return self._salignment

	@property
	def buffer(self):
		"""buffer commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_buffer'):
			from .Buffer import BufferCls
			self._buffer = BufferCls(self._core, self._cmd_group)
		return self._buffer

	def clone(self) -> 'BaseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BaseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
