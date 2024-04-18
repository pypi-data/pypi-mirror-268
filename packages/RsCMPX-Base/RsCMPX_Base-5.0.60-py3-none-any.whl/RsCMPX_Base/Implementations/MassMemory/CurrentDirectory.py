from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.Utilities import trim_str_response
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentDirectoryCls:
	"""CurrentDirectory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("currentDirectory", core, parent)

	def set(self, directory_name: str = None) -> None:
		"""SCPI: MMEMory:CDIRectory \n
		Snippet: driver.massMemory.currentDirectory.set(directory_name = 'abc') \n
		Changes the current directory for mass memory storage. If <DirectoryName> is omitted, the current directory is set to '/'. \n
			:param directory_name: Wildcards are not allowed.
		"""
		param = ''
		if directory_name:
			param = Conversions.value_to_quoted_str(directory_name)
		self._core.io.write(f'MMEMory:CDIRectory {param}'.strip())

	def get(self, directory_name: str = None) -> str:
		"""SCPI: MMEMory:CDIRectory \n
		Snippet: value: str = driver.massMemory.currentDirectory.get(directory_name = 'abc') \n
		Changes the current directory for mass memory storage. If <DirectoryName> is omitted, the current directory is set to '/'. \n
			:param directory_name: Wildcards are not allowed.
			:return: directory_name: Wildcards are not allowed."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('directory_name', directory_name, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'MMEMory:CDIRectory? {param}'.rstrip())
		return trim_str_response(response)
