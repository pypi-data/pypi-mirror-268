from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxCls:
	"""Rx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rx", core, parent)

	def set(self, rrh_name: str, source: enums.SourceInt) -> None:
		"""SCPI: CONFigure:SYSTem:RRHead:LO:SOURce:RX \n
		Snippet: driver.configure.system.rrhead.lo.source.rx.set(rrh_name = 'abc', source = enums.SourceInt.EXTernal) \n
		Selects the source of the LO signal for the RX direction of the RRH with the <RRH_Name>. \n
			:param rrh_name: No help available
			:param source: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rrh_name', rrh_name, DataType.String), ArgSingle('source', source, DataType.Enum, enums.SourceInt))
		self._core.io.write(f'CONFigure:SYSTem:RRHead:LO:SOURce:RX {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, rrh_name: str) -> enums.SourceInt:
		"""SCPI: CONFigure:SYSTem:RRHead:LO:SOURce:RX \n
		Snippet: value: enums.SourceInt = driver.configure.system.rrhead.lo.source.rx.get(rrh_name = 'abc') \n
		Selects the source of the LO signal for the RX direction of the RRH with the <RRH_Name>. \n
			:param rrh_name: No help available
			:return: source: No help available"""
		param = Conversions.value_to_quoted_str(rrh_name)
		response = self._core.io.query_str(f'CONFigure:SYSTem:RRHead:LO:SOURce:RX? {param}')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)
