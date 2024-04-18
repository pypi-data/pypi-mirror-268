from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def get_spath(self) -> List[str]:
		"""SCPI: DIAGnostic:ROUTe:NRMMw:MEASurement<Instance>:SPATh \n
		Snippet: value: List[str] = driver.diagnostic.route.nrMmw.measurement.get_spath() \n
		No command help available \n
			:return: signal_path: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:ROUTe:NRMMw:MEASurement<Instance>:SPATh?')
		return Conversions.str_to_str_list(response)

	def set_spath(self, signal_path: List[str]) -> None:
		"""SCPI: DIAGnostic:ROUTe:NRMMw:MEASurement<Instance>:SPATh \n
		Snippet: driver.diagnostic.route.nrMmw.measurement.set_spath(signal_path = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param signal_path: No help available
		"""
		param = Conversions.list_to_csv_quoted_str(signal_path)
		self._core.io.write(f'DIAGnostic:ROUTe:NRMMw:MEASurement<Instance>:SPATh {param}')
