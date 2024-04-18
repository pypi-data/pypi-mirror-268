from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResetCls:
	"""Reset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reset", core, parent)

	def get_partial(self) -> List[str]:
		"""SCPI: CATalog:SYSTem:RESet:PARTial \n
		Snippet: value: List[str] = driver.catalog.system.reset.get_partial() \n
		Queries a list of the components available for a partial reset. \n
			:return: resetable_system_part: Comma-separated list of strings, one string per component.
		"""
		response = self._core.io.query_str('CATalog:SYSTem:RESet:PARTial?')
		return Conversions.str_to_str_list(response)
