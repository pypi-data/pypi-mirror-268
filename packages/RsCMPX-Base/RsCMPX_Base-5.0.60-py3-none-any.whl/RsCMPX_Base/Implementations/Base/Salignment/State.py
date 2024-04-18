from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.Salignment]:
		"""SCPI: FETCh:BASE:SALignment:STATe \n
		Snippet: value: List[enums.Salignment] = driver.base.salignment.state.fetch() \n
		Queries status information for the last self-alignment execution. The information is returned for the measurement modes
		IQ or Verify IQ (whichever was executed last) and Level: <State>IQ or verify IQ, <State>level \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'FETCh:BASE:SALignment:STATe?')
		return Conversions.str_to_list_enum(response, enums.Salignment)
