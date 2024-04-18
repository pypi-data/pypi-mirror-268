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
		"""SCPI: MMEMory:STORe:MACRo \n
		Snippet: driver.massMemory.store.macro.set(label = 'abc', filename = 'abc', msus = 'abc') \n
		Stores the contents of a macro to a file. If the file exists, it is overwritten. If the file does not exist, it is
		created. \n
			:param label: No help available
			:param filename: No help available
			:param msus: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('label', label, DataType.String), ArgSingle('filename', filename, DataType.String), ArgSingle('msus', msus, DataType.String, None, is_optional=True))
		self._core.io.write(f'MMEMory:STORe:MACRo {param}'.rstrip())
