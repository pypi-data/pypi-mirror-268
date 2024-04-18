from typing import List

from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FirmwareUpdateCls:
	"""FirmwareUpdate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("firmwareUpdate", core, parent)

	def get_versions(self) -> List[str]:
		"""SCPI: FETCh:FWUPdate:VERSions \n
		Snippet: value: List[str] = driver.firmwareUpdate.get_versions() \n
		No command help available \n
			:return: versions: No help available
		"""
		response = self._core.io.query_str('FETCh:FWUPdate:VERSions?')
		return Conversions.str_to_str_list(response)
