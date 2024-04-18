from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EntryCls:
	"""Entry commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("entry", core, parent)

	def get(self, index: int) -> bytes:
		"""SCPI: SYSTem:DFPRint:HISTory:ENTRy \n
		Snippet: value: bytes = driver.system.deviceFootprint.history.entry.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: xml_device_footprint: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_bin_block_ERROR(f'SYSTem:DFPRint:HISTory:ENTRy? {param}')
		return response
