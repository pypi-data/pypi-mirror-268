from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self, name: str) -> int:
		"""SCPI: CONFigure:SEMaphore:COUNt \n
		Snippet: value: int = driver.configure.semaphore.count.get(name = 'abc') \n
		No command help available \n
			:param name: No help available
			:return: count: No help available"""
		param = Conversions.value_to_quoted_str(name)
		response = self._core.io.query_str(f'CONFigure:SEMaphore:COUNt? {param}')
		return Conversions.str_to_int(response)
