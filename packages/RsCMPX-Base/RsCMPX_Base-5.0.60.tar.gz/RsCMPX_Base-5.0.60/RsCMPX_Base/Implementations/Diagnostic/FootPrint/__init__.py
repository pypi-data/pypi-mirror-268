from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FootPrintCls:
	"""FootPrint commands group definition. 8 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("footPrint", core, parent)

	@property
	def element(self):
		"""element commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_element'):
			from .Element import ElementCls
			self._element = ElementCls(self._core, self._cmd_group)
		return self._element

	@property
	def useCase(self):
		"""useCase commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_useCase'):
			from .UseCase import UseCaseCls
			self._useCase = UseCaseCls(self._core, self._cmd_group)
		return self._useCase

	@property
	def li(self):
		"""li commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_li'):
			from .Li import LiCls
			self._li = LiCls(self._core, self._cmd_group)
		return self._li

	def clone(self) -> 'FootPrintCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FootPrintCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
