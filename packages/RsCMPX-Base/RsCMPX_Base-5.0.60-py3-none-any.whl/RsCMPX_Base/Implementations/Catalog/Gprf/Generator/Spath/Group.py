from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GroupCls:
	"""Group commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("group", core, parent)

	def get_connector(self) -> str:
		"""SCPI: CATalog:GPRF:GENerator<Instance>:SPATh:GROup:CONNector \n
		Snippet: value: str = driver.catalog.gprf.generator.spath.group.get_connector() \n
		No command help available \n
			:return: connector_name: No help available
		"""
		response = self._core.io.query_str('CATalog:GPRF:GENerator<Instance>:SPATh:GROup:CONNector?')
		return trim_str_response(response)

	def get(self, connector_name: str) -> List[str]:
		"""SCPI: CATalog:GPRF:GENerator<Instance>:SPATh:GROup \n
		Snippet: value: List[str] = driver.catalog.gprf.generator.spath.group.get(connector_name = 'abc') \n
		No command help available \n
			:param connector_name: No help available
			:return: signal_path: No help available"""
		param = Conversions.value_to_quoted_str(connector_name)
		response = self._core.io.query_str(f'CATalog:GPRF:GENerator<Instance>:SPATh:GROup? {param}')
		return Conversions.str_to_str_list(response)
