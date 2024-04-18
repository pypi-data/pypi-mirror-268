from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BaseCls:
	"""Base commands group definition. 8 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def mmi(self):
		"""mmi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmi'):
			from .Mmi import MmiCls
			self._mmi = MmiCls(self._core, self._cmd_group)
		return self._mmi

	@property
	def salignment(self):
		"""salignment commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_salignment'):
			from .Salignment import SalignmentCls
			self._salignment = SalignmentCls(self._core, self._cmd_group)
		return self._salignment

	@property
	def product(self):
		"""product commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_product'):
			from .Product import ProductCls
			self._product = ProductCls(self._core, self._cmd_group)
		return self._product

	def clone(self) -> 'BaseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BaseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
