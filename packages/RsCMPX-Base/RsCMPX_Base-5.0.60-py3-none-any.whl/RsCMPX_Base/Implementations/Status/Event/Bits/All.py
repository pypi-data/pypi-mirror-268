from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self, filter_py: str = None, mode: enums.ExpressionMode = None) -> List[str]:
		"""SCPI: STATus:EVENt:BITS:ALL \n
		Snippet: value: List[str] = driver.status.event.bits.all.get(filter_py = 'abc', mode = enums.ExpressionMode.REGex) \n
		No command help available \n
			:param filter_py: No help available
			:param mode: No help available
			:return: bit: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True), ArgSingle('mode', mode, DataType.Enum, enums.ExpressionMode, is_optional=True))
		response = self._core.io.query_str(f'STATus:EVENt:BITS:ALL? {param}'.rstrip())
		return Conversions.str_to_str_list(response)
