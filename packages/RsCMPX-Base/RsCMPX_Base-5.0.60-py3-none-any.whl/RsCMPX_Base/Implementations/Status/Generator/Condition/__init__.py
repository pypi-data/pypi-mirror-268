from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConditionCls:
	"""Condition commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("condition", core, parent)

	@property
	def off(self):
		"""off commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_off'):
			from .Off import OffCls
			self._off = OffCls(self._core, self._cmd_group)
		return self._off

	@property
	def pending(self):
		"""pending commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pending'):
			from .Pending import PendingCls
			self._pending = PendingCls(self._core, self._cmd_group)
		return self._pending

	@property
	def on(self):
		"""on commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_on'):
			from .On import OnCls
			self._on = OnCls(self._core, self._cmd_group)
		return self._on

	def clone(self) -> 'ConditionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConditionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
