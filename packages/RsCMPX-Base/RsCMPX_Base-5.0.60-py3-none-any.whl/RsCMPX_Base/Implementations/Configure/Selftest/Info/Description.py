from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DescriptionCls:
	"""Description commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("description", core, parent)

	def get(self, test_name: str) -> str:
		"""SCPI: CONFigure:SELFtest:INFO:DESCription \n
		Snippet: value: str = driver.configure.selftest.info.description.get(test_name = 'abc') \n
		No command help available \n
			:param test_name: No help available
			:return: detailed_desc: No help available"""
		param = Conversions.value_to_quoted_str(test_name)
		response = self._core.io.query_str(f'CONFigure:SELFtest:INFO:DESCription? {param}')
		return trim_str_response(response)
