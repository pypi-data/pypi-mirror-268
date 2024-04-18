from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HeadersCls:
	"""Headers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("headers", core, parent)

	def get(self, parser: str = None) -> bytes:
		"""SCPI: SYSTem:HELP:HEADers \n
		Snippet: value: bytes = driver.system.help.headers.get(parser = 'abc') \n
		No command help available \n
			:param parser: No help available
			:return: headers: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('parser', parser, DataType.String, None, is_optional=True))
		response = self._core.io.query_bin_block_ERROR(f'SYSTem:HELP:HEADers? {param}'.rstrip())
		return response
