from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BgInfoCls:
	"""BgInfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bgInfo", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: DIAGnostic:BGINfo:CATalog \n
		Snippet: value: List[str] = driver.diagnostic.bgInfo.get_catalog() \n
		No command help available \n
			:return: boards: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:BGINfo:CATalog?')
		return Conversions.str_to_str_list(response)
