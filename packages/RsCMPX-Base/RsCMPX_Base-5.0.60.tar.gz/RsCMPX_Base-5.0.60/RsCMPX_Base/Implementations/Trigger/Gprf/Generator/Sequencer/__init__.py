from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SequencerCls:
	"""Sequencer commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequencer", core, parent)

	@property
	def isMeas(self):
		"""isMeas commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_isMeas'):
			from .IsMeas import IsMeasCls
			self._isMeas = IsMeasCls(self._core, self._cmd_group)
		return self._isMeas

	@property
	def isTrigger(self):
		"""isTrigger commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_isTrigger'):
			from .IsTrigger import IsTriggerCls
			self._isTrigger = IsTriggerCls(self._core, self._cmd_group)
		return self._isTrigger

	def clone(self) -> 'SequencerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SequencerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
