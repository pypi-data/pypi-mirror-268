from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MmiCls:
	"""Mmi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mmi", core, parent)

	def get_version(self) -> List[str]:
		"""SCPI: DIAGnostic:BASE:MMI:VERSion \n
		Snippet: value: List[str] = driver.diagnostic.base.mmi.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:BASE:MMI:VERSion?')
		return Conversions.str_to_str_list(response)
