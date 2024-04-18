from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_source(self) -> List[str]:
		"""SCPI: TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:CATalog:SOURce \n
		Snippet: value: List[str] = driver.trigger.wcdma.measurement.ooSync.catalog.get_source() \n
		No command help available \n
			:return: trigger: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:CATalog:SOURce?')
		return Conversions.str_to_str_list(response)
