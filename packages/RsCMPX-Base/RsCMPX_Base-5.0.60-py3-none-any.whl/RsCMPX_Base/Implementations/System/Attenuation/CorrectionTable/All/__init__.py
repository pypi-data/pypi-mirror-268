from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	@property
	def tenvironment(self):
		"""tenvironment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tenvironment'):
			from .Tenvironment import TenvironmentCls
			self._tenvironment = TenvironmentCls(self._core, self._cmd_group)
		return self._tenvironment

	@property
	def globale(self):
		"""globale commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_globale'):
			from .Globale import GlobaleCls
			self._globale = GlobaleCls(self._core, self._cmd_group)
		return self._globale

	def clone(self) -> 'AllCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AllCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
