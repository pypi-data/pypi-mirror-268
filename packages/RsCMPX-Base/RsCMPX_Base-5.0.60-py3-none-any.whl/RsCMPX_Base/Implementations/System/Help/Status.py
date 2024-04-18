from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatusCls:
	"""Status commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	def get_bits(self) -> List[str]:
		"""SCPI: SYSTem:HELP:STATus:BITS \n
		Snippet: value: List[str] = driver.system.help.status.get_bits() \n
		No command help available \n
			:return: bits: No help available
		"""
		response = self._core.io.query_str('SYSTem:HELP:STATus:BITS?')
		return Conversions.str_to_str_list(response)

	def get_register(self) -> List[str]:
		"""SCPI: SYSTem:HELP:STATus[:REGister] \n
		Snippet: value: List[str] = driver.system.help.status.get_register() \n
		No command help available \n
			:return: register: No help available
		"""
		response = self._core.io.query_str('SYSTem:HELP:STATus:REGister?')
		return Conversions.str_to_str_list(response)
