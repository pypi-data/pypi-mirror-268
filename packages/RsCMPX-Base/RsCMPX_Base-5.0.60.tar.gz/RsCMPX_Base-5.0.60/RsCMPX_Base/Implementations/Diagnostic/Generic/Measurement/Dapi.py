from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DapiCls:
	"""Dapi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dapi", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: DIAGnostic:GENeric:MEASurement:DAPI:TOUT \n
		Snippet: value: float = driver.diagnostic.generic.measurement.dapi.get_timeout() \n
		No command help available \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GENeric:MEASurement:DAPI:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: DIAGnostic:GENeric:MEASurement:DAPI:TOUT \n
		Snippet: driver.diagnostic.generic.measurement.dapi.set_timeout(timeout = 1.0) \n
		No command help available \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'DIAGnostic:GENeric:MEASurement:DAPI:TOUT {param}')
