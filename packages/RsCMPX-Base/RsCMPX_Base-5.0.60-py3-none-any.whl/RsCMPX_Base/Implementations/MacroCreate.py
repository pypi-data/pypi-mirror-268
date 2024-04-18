from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from ..Internal.Types import DataType
from ..Internal.Utilities import trim_str_response
from ..Internal.ArgSingleList import ArgSingleList
from ..Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MacroCreateCls:
	"""MacroCreate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("macroCreate", core, parent)

	def set(self, label: str, macro: str) -> None:
		"""SCPI: *DMC \n
		Snippet: driver.macroCreate.set(label = 'abc', macro = 'abc') \n
		Creates a macro. If the label exists already, the macro contents are overwritten. Macros are deleted when a remote
		connection is closed but can be saved to a macro file for later reuse, see method RsCMPX_Base.MassMemory.Store.Macro.set.
		Avoid using labels which are identical with supported remote control commands. In contrast to SCPI stipulations, remote
		commands have priority over macros. \n
			:param label: No help available
			:param macro: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('label', label, DataType.String), ArgSingle('macro', macro, DataType.String))
		self._core.io.write(f'*DMC {param}'.rstrip())

	def get(self, label: str) -> str:
		"""SCPI: *DMC \n
		Snippet: value: str = driver.macroCreate.get(label = 'abc') \n
		Creates a macro. If the label exists already, the macro contents are overwritten. Macros are deleted when a remote
		connection is closed but can be saved to a macro file for later reuse, see method RsCMPX_Base.MassMemory.Store.Macro.set.
		Avoid using labels which are identical with supported remote control commands. In contrast to SCPI stipulations, remote
		commands have priority over macros. \n
			:param label: No help available
			:return: macro: No help available"""
		param = Conversions.value_to_quoted_str(label)
		response = self._core.io.query_str(f'*DMC? {param}')
		return trim_str_response(response)
