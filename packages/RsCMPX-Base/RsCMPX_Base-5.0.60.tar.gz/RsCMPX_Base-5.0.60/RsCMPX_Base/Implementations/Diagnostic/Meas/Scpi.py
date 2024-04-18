from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScpiCls:
	"""Scpi commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scpi", core, parent)

	def get_version(self) -> float:
		"""SCPI: DIAGnostic:MEAS:SCPI:VERSion \n
		Snippet: value: float = driver.diagnostic.meas.scpi.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:MEAS:SCPI:VERSion?')
		return Conversions.str_to_float(response)

	def get_host(self) -> str:
		"""SCPI: DIAGnostic:MEAS:SCPI:HOST \n
		Snippet: value: str = driver.diagnostic.meas.scpi.get_host() \n
		No command help available \n
			:return: name: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:MEAS:SCPI:HOST?')
		return trim_str_response(response)
