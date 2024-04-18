from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmwdCls:
	"""Cmwd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmwd", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:CMWD:TIMeout \n
		Snippet: value: float = driver.configure.cmwd.get_timeout() \n
		No command help available \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:CMWD:TIMeout?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:CMWD:TIMeout \n
		Snippet: driver.configure.cmwd.set_timeout(timeout = 1.0) \n
		No command help available \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:CMWD:TIMeout {param}')
