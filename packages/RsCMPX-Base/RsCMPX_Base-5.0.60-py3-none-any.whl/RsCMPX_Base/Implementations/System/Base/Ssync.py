from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsyncCls:
	"""Ssync commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssync", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.CmwMode:
		"""SCPI: SYSTem:BASE:SSYNc:MODE \n
		Snippet: value: enums.CmwMode = driver.system.base.ssync.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str_with_opc('SYSTem:BASE:SSYNc:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CmwMode)

	def set_mode(self, mode: enums.CmwMode) -> None:
		"""SCPI: SYSTem:BASE:SSYNc:MODE \n
		Snippet: driver.system.base.ssync.set_mode(mode = enums.CmwMode.GENerator) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CmwMode)
		self._core.io.write_with_opc(f'SYSTem:BASE:SSYNc:MODE {param}')

	def get_offset(self) -> int:
		"""SCPI: SYSTem:BASE:SSYNc:OFFSet \n
		Snippet: value: int = driver.system.base.ssync.get_offset() \n
		No command help available \n
			:return: offset: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:SSYNc:OFFSet?')
		return Conversions.str_to_int(response)

	def set_offset(self, offset: int) -> None:
		"""SCPI: SYSTem:BASE:SSYNc:OFFSet \n
		Snippet: driver.system.base.ssync.set_offset(offset = 1) \n
		No command help available \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SYSTem:BASE:SSYNc:OFFSet {param}')
