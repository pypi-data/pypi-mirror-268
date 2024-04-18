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

	def set_partial(self, resetable_system_part: List[str]) -> None:
		"""SCPI: [CONFigure]:SYSTem:RESet:PARTial \n
		Snippet: driver.configure.system.reset.set_partial(resetable_system_part = ['abc1', 'abc2', 'abc3']) \n
		Resets selected system components. \n
			:param resetable_system_part: Comma-separated list of strings, one string per component to be reset.
		"""
		param = Conversions.list_to_csv_quoted_str(resetable_system_part)
		self._core.io.write(f'CONFigure:SYSTem:RESet:PARTial {param}')
