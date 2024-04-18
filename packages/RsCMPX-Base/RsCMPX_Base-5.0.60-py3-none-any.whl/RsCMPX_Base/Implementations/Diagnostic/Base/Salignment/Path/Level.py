from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def get_start(self) -> str:
		"""SCPI: DIAGnostic:BASE:SALignment:PATH:LEVel:STARt \n
		Snippet: value: str = driver.diagnostic.base.salignment.path.level.get_start() \n
		No command help available \n
			:return: path: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:BASE:SALignment:PATH:LEVel:STARt?')
		return trim_str_response(response)

	def set_start(self, path: str) -> None:
		"""SCPI: DIAGnostic:BASE:SALignment:PATH:LEVel:STARt \n
		Snippet: driver.diagnostic.base.salignment.path.level.set_start(path = 'abc') \n
		No command help available \n
			:param path: No help available
		"""
		param = Conversions.value_to_quoted_str(path)
		self._core.io.write(f'DIAGnostic:BASE:SALignment:PATH:LEVel:STARt {param}')

	def get_state(self) -> List[str]:
		"""SCPI: DIAGnostic:BASE:SALignment:PATH:LEVel:STATe \n
		Snippet: value: List[str] = driver.diagnostic.base.salignment.path.level.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:BASE:SALignment:PATH:LEVel:STATe?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> List[str]:
		"""SCPI: DIAGnostic:BASE:SALignment:PATH:LEVel \n
		Snippet: value: List[str] = driver.diagnostic.base.salignment.path.level.get_value() \n
		No command help available \n
			:return: path_list: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:BASE:SALignment:PATH:LEVel?')
		return Conversions.str_to_str_list(response)
