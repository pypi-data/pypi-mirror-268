from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: SYSTem:BASE:REFerence:DC:OFFSet:ENABle \n
		Snippet: value: bool = driver.system.base.reference.dc.offset.get_enable() \n
		No command help available \n
			:return: dc_offset_enable: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:REFerence:DC:OFFSet:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, dc_offset_enable: bool) -> None:
		"""SCPI: SYSTem:BASE:REFerence:DC:OFFSet:ENABle \n
		Snippet: driver.system.base.reference.dc.offset.set_enable(dc_offset_enable = False) \n
		No command help available \n
			:param dc_offset_enable: No help available
		"""
		param = Conversions.bool_to_str(dc_offset_enable)
		self._core.io.write(f'SYSTem:BASE:REFerence:DC:OFFSet:ENABle {param}')
