from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdentifyCls:
	"""Identify commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("identify", core, parent)

	def get_btime(self) -> int:
		"""SCPI: CONFigure:BASE:MCMW:IDENtify:BTIMe \n
		Snippet: value: int = driver.configure.base.multiCmw.identify.get_btime() \n
		No command help available \n
			:return: blinking_time: No help available
		"""
		response = self._core.io.query_str('CONFigure:BASE:MCMW:IDENtify:BTIMe?')
		return Conversions.str_to_int(response)

	def set_btime(self, blinking_time: int) -> None:
		"""SCPI: CONFigure:BASE:MCMW:IDENtify:BTIMe \n
		Snippet: driver.configure.base.multiCmw.identify.set_btime(blinking_time = 1) \n
		No command help available \n
			:param blinking_time: No help available
		"""
		param = Conversions.decimal_value_to_str(blinking_time)
		self._core.io.write(f'CONFigure:BASE:MCMW:IDENtify:BTIMe {param}')
