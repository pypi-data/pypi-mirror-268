from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LiCls:
	"""Li commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("li", core, parent)

	@property
	def usecases(self):
		"""usecases commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usecases'):
			from .Usecases import UsecasesCls
			self._usecases = UsecasesCls(self._core, self._cmd_group)
		return self._usecases

	def clone(self) -> 'LiCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LiCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
