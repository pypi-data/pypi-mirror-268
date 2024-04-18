from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpcrCls:
	"""Ipcr commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipcr", core, parent)

	def get_date(self) -> str:
		"""SCPI: CALibration:BASE:IPCR:DATE \n
		Snippet: value: str = driver.calibration.base.ipcr.get_date() \n
		No command help available \n
			:return: date: No help available
		"""
		response = self._core.io.query_str('CALibration:BASE:IPCR:DATE?')
		return trim_str_response(response)

	def get_state(self) -> List[int]:
		"""SCPI: CALibration:BASE:IPCR:STATe \n
		Snippet: value: List[int] = driver.calibration.base.ipcr.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CALibration:BASE:IPCR:STATe?')
		return response

	def get_result(self) -> List[str]:
		"""SCPI: CALibration:BASE:IPCR:RESult \n
		Snippet: value: List[str] = driver.calibration.base.ipcr.get_result() \n
		No command help available \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('CALibration:BASE:IPCR:RESult?')
		return Conversions.str_to_str_list(response)
