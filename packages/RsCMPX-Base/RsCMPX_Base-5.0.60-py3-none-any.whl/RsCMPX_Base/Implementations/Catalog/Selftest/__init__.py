from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelftestCls:
	"""Selftest commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selftest", core, parent)

	@property
	def selected(self):
		"""selected commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_selected'):
			from .Selected import SelectedCls
			self._selected = SelectedCls(self._core, self._cmd_group)
		return self._selected

	def get(self, filter_py: str = None) -> List[str]:
		"""SCPI: CATalog:SELFtest \n
		Snippet: value: List[str] = driver.catalog.selftest.get(filter_py = 'abc') \n
		No command help available \n
			:param filter_py: No help available
			:return: results: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'CATalog:SELFtest? {param}'.rstrip())
		return Conversions.str_to_str_list(response)

	def get_uprofile(self) -> List[str]:
		"""SCPI: CATalog:SELFtest:UPRofile \n
		Snippet: value: List[str] = driver.catalog.selftest.get_uprofile() \n
		No command help available \n
			:return: user_prof_names: No help available
		"""
		response = self._core.io.query_str('CATalog:SELFtest:UPRofile?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'SelftestCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SelftestCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
