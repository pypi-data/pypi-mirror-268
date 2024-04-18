from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrheadCls:
	"""Rrhead commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrhead", core, parent)

	@property
	def lo(self):
		"""lo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lo'):
			from .Lo import LoCls
			self._lo = LoCls(self._core, self._cmd_group)
		return self._lo

	def clone(self) -> 'RrheadCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RrheadCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
