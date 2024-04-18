from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrepareCls:
	"""Prepare commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prepare", core, parent)

	def get_fdefault(self) -> bool:
		"""SCPI: SYSTem:STARtup:PREPare:FDEFault \n
		Snippet: value: bool = driver.system.startup.prepare.get_fdefault() \n
		No command help available \n
			:return: on_off: No help available
		"""
		response = self._core.io.query_str('SYSTem:STARtup:PREPare:FDEFault?')
		return Conversions.str_to_bool(response)

	def set_fdefault(self, on_off: bool) -> None:
		"""SCPI: SYSTem:STARtup:PREPare:FDEFault \n
		Snippet: driver.system.startup.prepare.set_fdefault(on_off = False) \n
		No command help available \n
			:param on_off: No help available
		"""
		param = Conversions.bool_to_str(on_off)
		self._core.io.write(f'SYSTem:STARtup:PREPare:FDEFault {param}')
