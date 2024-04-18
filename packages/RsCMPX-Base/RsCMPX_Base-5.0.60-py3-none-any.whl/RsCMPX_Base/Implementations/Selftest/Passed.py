from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PassedCls:
	"""Passed commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("passed", core, parent)

	def fetch(self, filter_py: str = None) -> List[str]:
		"""SCPI: FETCh:SELFtest:PASSed \n
		Snippet: value: List[str] = driver.selftest.passed.fetch(filter_py = 'abc') \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param filter_py: No help available
			:return: value: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:SELFtest:PASSed? {param}'.rstrip(), suppressed)
		return Conversions.str_to_str_list(response)

	def read(self, filter_py: str = None) -> List[str]:
		"""SCPI: READ:SELFtest:PASSed \n
		Snippet: value: List[str] = driver.selftest.passed.read(filter_py = 'abc') \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param filter_py: No help available
			:return: value: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:SELFtest:PASSed? {param}'.rstrip(), suppressed)
		return Conversions.str_to_str_list(response)
