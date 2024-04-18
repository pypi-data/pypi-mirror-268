from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VersionCls:
	"""Version commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("version", core, parent)

	def get(self, applicname: str = None) -> str:
		"""SCPI: SYSTem:BASE:OPTion:VERSion \n
		Snippet: value: str = driver.system.base.option.version.get(applicname = 'abc') \n
		Returns version information for installed software packages.
			INTRO_CMD_HELP: You can either query a list of all installed packages and their versions or you can query the version of a single package specified via <Application>: \n
			- <Application> specified: A string is returned, indicating the version of the <Application>. If the specified <Application> is unknown / not installed, '0' is returned.
			- <Application> omitted: A string is returned, containing a list of all installed software packages and their version in the format '<PackageName1>,<Version1>;<PackageName2>,<Version2>;...'  \n
			:param applicname: Software package for which the version is queried.
			:return: option_list: Single version or list of applications and versions"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('applicname', applicname, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'SYSTem:BASE:OPTion:VERSion? {param}'.rstrip())
		return trim_str_response(response)
