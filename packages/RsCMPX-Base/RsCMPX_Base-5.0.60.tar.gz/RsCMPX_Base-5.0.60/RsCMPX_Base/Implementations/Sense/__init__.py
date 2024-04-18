from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SenseCls:
	"""Sense commands group definition. 15 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def base(self):
		"""base commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_base'):
			from .Base import BaseCls
			self._base = BaseCls(self._core, self._cmd_group)
		return self._base

	@property
	def firmwareUpdate(self):
		"""firmwareUpdate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_firmwareUpdate'):
			from .FirmwareUpdate import FirmwareUpdateCls
			self._firmwareUpdate = FirmwareUpdateCls(self._core, self._cmd_group)
		return self._firmwareUpdate

	@property
	def selftest(self):
		"""selftest commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_selftest'):
			from .Selftest import SelftestCls
			self._selftest = SelftestCls(self._core, self._cmd_group)
		return self._selftest

	def clone(self) -> 'SenseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SenseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
