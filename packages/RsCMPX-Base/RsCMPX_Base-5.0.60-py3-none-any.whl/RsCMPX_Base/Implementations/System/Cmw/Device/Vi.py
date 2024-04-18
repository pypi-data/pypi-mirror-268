from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ViCls:
	"""Vi commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vi", core, parent)

	def get_mode(self) -> bool:
		"""SCPI: SYSTem:CMW:DEVice:VI:MODE \n
		Snippet: value: bool = driver.system.cmw.device.vi.get_mode() \n
		No command help available \n
			:return: vi_mode: No help available
		"""
		response = self._core.io.query_str('SYSTem:CMW:DEVice:VI:MODE?')
		return Conversions.str_to_bool(response)

	def get_count(self) -> int:
		"""SCPI: SYSTem:CMW:DEVice:VI:COUNt \n
		Snippet: value: int = driver.system.cmw.device.vi.get_count() \n
		No command help available \n
			:return: vi_count: No help available
		"""
		response = self._core.io.query_str('SYSTem:CMW:DEVice:VI:COUNt?')
		return Conversions.str_to_int(response)
