from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubMonitorCls:
	"""SubMonitor commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subMonitor", core, parent)

	def get_name(self) -> List[str]:
		"""SCPI: SENSe:BASE:IPSet:SMONitor:NAME \n
		Snippet: value: List[str] = driver.sense.base.ipSet.subMonitor.get_name() \n
		No command help available \n
			:return: names: No help available
		"""
		response = self._core.io.query_str('SENSe:BASE:IPSet:SMONitor:NAME?')
		return Conversions.str_to_str_list(response)

	def get_type_py(self) -> List[str]:
		"""SCPI: SENSe:BASE:IPSet:SMONitor:TYPE \n
		Snippet: value: List[str] = driver.sense.base.ipSet.subMonitor.get_type_py() \n
		No command help available \n
			:return: types: No help available
		"""
		response = self._core.io.query_str('SENSe:BASE:IPSet:SMONitor:TYPE?')
		return Conversions.str_to_str_list(response)

	def get_id(self) -> List[int]:
		"""SCPI: SENSe:BASE:IPSet:SMONitor:ID \n
		Snippet: value: List[int] = driver.sense.base.ipSet.subMonitor.get_id() \n
		No command help available \n
			:return: ids: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SENSe:BASE:IPSet:SMONitor:ID?')
		return response

	def get_description(self) -> List[str]:
		"""SCPI: SENSe:BASE:IPSet:SMONitor:DESCription \n
		Snippet: value: List[str] = driver.sense.base.ipSet.subMonitor.get_description() \n
		No command help available \n
			:return: descriptions: No help available
		"""
		response = self._core.io.query_str('SENSe:BASE:IPSet:SMONitor:DESCription?')
		return Conversions.str_to_str_list(response)
