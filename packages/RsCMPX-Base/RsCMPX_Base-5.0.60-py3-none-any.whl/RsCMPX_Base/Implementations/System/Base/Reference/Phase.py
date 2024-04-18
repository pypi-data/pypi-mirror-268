from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhaseCls:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def get_offset(self) -> float:
		"""SCPI: SYSTem:BASE:REFerence:PHASe:OFFSet \n
		Snippet: value: float = driver.system.base.reference.phase.get_offset() \n
		No command help available \n
			:return: phase_offset: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:REFerence:PHASe:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, phase_offset: float) -> None:
		"""SCPI: SYSTem:BASE:REFerence:PHASe:OFFSet \n
		Snippet: driver.system.base.reference.phase.set_offset(phase_offset = 1.0) \n
		No command help available \n
			:param phase_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(phase_offset)
		self._core.io.write(f'SYSTem:BASE:REFerence:PHASe:OFFSet {param}')
