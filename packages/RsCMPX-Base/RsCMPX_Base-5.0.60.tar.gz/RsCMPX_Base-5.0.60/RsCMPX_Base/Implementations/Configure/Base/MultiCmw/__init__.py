from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiCmwCls:
	"""MultiCmw commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiCmw", core, parent)

	@property
	def identify(self):
		"""identify commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_identify'):
			from .Identify import IdentifyCls
			self._identify = IdentifyCls(self._core, self._cmd_group)
		return self._identify

	def set_rearrange(self, box_nr: List[enums.BoxNumber]) -> None:
		"""SCPI: CONFigure:BASE:MCMW:REARrange \n
		Snippet: driver.configure.base.multiCmw.set_rearrange(box_nr = [BoxNumber.BOX1, BoxNumber.NAV]) \n
		No command help available \n
			:param box_nr: No help available
		"""
		param = Conversions.enum_list_to_str(box_nr, enums.BoxNumber)
		self._core.io.write(f'CONFigure:BASE:MCMW:REARrange {param}')

	def clone(self) -> 'MultiCmwCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiCmwCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
