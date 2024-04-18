from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MacroCls:
	"""Macro commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("macro", core, parent)

	def set(self, label: str, filename: str, msus: str = None) -> None:
		"""SCPI: MMEMory:LOAD:MACRo \n
		Snippet: driver.massMemory.load.macro.set(label = 'abc', filename = 'abc', msus = 'abc') \n
		Creates a macro, reading the macro contents from a file. If the label exists already, the macro contents are overwritten.
		Avoid using labels which are identical with supported remote control commands. In contrast to SCPI stipulations, remote
		commands have priority over macros. \n
			:param label: No help available
			:param filename: No help available
			:param msus: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('label', label, DataType.String), ArgSingle('filename', filename, DataType.String), ArgSingle('msus', msus, DataType.String, None, is_optional=True))
		self._core.io.write(f'MMEMory:LOAD:MACRo {param}'.rstrip())
