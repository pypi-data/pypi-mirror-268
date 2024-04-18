from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self, fw_app_name: str) -> int:
		"""SCPI: DIAGnostic:INSTrument:APPLication:COUNt \n
		Snippet: value: int = driver.diagnostic.instrument.application.count.get(fw_app_name = 'abc') \n
		No command help available \n
			:param fw_app_name: No help available
			:return: instance_count: No help available"""
		param = Conversions.value_to_quoted_str(fw_app_name)
		response = self._core.io.query_str(f'DIAGnostic:INSTrument:APPLication:COUNt? {param}')
		return Conversions.str_to_int(response)
