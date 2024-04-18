from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LengthCls:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def get(self, table_name: str) -> int:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:LENGth \n
		Snippet: value: int = driver.configure.base.freqCorrection.correctionTable.length.get(table_name = 'abc') \n
		No command help available \n
			:param table_name: No help available
			:return: table_length: No help available"""
		param = Conversions.value_to_quoted_str(table_name)
		response = self._core.io.query_str(f'CONFigure:BASE:FDCorrection:CTABle:LENGth? {param}')
		return Conversions.str_to_int(response)
