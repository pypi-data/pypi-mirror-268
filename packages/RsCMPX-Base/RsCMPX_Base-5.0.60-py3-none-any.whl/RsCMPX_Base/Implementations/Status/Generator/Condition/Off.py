from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffCls:
	"""Off commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("off", core, parent)

	def get(self, filter_py: str = None, mode: enums.ExpressionMode = None) -> str:
		"""SCPI: STATus:GENerator:CONDition:OFF \n
		Snippet: value: str = driver.status.generator.condition.off.get(filter_py = 'abc', mode = enums.ExpressionMode.REGex) \n
		No command help available \n
			:param filter_py: No help available
			:param mode: No help available
			:return: bitname: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True), ArgSingle('mode', mode, DataType.Enum, enums.ExpressionMode, is_optional=True))
		response = self._core.io.query_str(f'STATus:GENerator:CONDition:OFF? {param}'.rstrip())
		return trim_str_response(response)
