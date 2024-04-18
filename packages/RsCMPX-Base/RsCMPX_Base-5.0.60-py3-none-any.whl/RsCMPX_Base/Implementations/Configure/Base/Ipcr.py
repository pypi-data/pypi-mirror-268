from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpcrCls:
	"""Ipcr commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipcr", core, parent)

	def get_enable(self) -> List[bool]:
		"""SCPI: CONFigure:BASE:IPCR:ENABle \n
		Snippet: value: List[bool] = driver.configure.base.ipcr.get_enable() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:BASE:IPCR:ENABle?')
		return Conversions.str_to_bool_list(response)

	def set_enable(self, enable: List[bool]) -> None:
		"""SCPI: CONFigure:BASE:IPCR:ENABle \n
		Snippet: driver.configure.base.ipcr.set_enable(enable = [True, False, True]) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.list_to_csv_str(enable)
		self._core.io.write(f'CONFigure:BASE:IPCR:ENABle {param}')

	def get_ident(self) -> List[str]:
		"""SCPI: CONFigure:BASE:IPCR:IDENt \n
		Snippet: value: List[str] = driver.configure.base.ipcr.get_ident() \n
		No command help available \n
			:return: ident: No help available
		"""
		response = self._core.io.query_str('CONFigure:BASE:IPCR:IDENt?')
		return Conversions.str_to_str_list(response)
