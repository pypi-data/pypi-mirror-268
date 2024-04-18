from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectedCls:
	"""Selected commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selected", core, parent)

	def get(self, filter_py: str = None) -> List[str]:
		"""SCPI: CATalog:SELFtest:SELected \n
		Snippet: value: List[str] = driver.catalog.selftest.selected.get(filter_py = 'abc') \n
		No command help available \n
			:param filter_py: No help available
			:return: result: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'CATalog:SELFtest:SELected? {param}'.rstrip())
		return Conversions.str_to_str_list(response)
