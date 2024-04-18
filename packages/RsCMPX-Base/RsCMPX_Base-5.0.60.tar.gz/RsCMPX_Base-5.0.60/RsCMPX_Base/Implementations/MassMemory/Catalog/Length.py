from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LengthCls:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def get(self, path_name: str = None) -> int:
		"""SCPI: MMEMory:CATalog:LENGth \n
		Snippet: value: int = driver.massMemory.catalog.length.get(path_name = 'abc') \n
		Returns the number of files and subdirectories of the current or of a specified directory. The number also considers the
		strings '.' and '..' so that it corresponds to the number of strings returned by the method RsCMPX_Base.MassMemory.
		Catalog.get_ command after the initial numeric parameters. \n
			:param path_name: If the directory name is omitted, the command queries the contents of the current directory (see method RsCMPX_Base.MassMemory.CurrentDirectory.set) . If the wildcards ? or * are used, the number of files and subdirectories matching this pattern are returned.
			:return: count: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('path_name', path_name, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'MMEMory:CATalog:LENGth? {param}'.rstrip())
		return Conversions.str_to_int(response)
