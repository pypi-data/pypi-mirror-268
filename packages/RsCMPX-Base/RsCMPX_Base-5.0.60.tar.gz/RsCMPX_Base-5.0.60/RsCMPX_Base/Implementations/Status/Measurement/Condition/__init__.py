from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConditionCls:
	"""Condition commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

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
	def qued(self):
		"""qued commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qued'):
			from .Qued import QuedCls
			self._qued = QuedCls(self._core, self._cmd_group)
		return self._qued

	@property
	def run(self):
		"""run commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_run'):
			from .Run import RunCls
			self._run = RunCls(self._core, self._cmd_group)
		return self._run

	@property
	def rdy(self):
		"""rdy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rdy'):
			from .Rdy import RdyCls
			self._rdy = RdyCls(self._core, self._cmd_group)
		return self._rdy

	@property
	def sdReached(self):
		"""sdReached commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdReached'):
			from .SdReached import SdReachedCls
			self._sdReached = SdReachedCls(self._core, self._cmd_group)
		return self._sdReached

	def clone(self) -> 'ConditionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConditionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
