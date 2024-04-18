from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetupCls:
	"""Setup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	def set(self, absolute_item_name: List[str] = None, instrument: List[int] = None) -> None:
		"""SCPI: SYSTem:BASE:DEVice:SETup \n
		Snippet: driver.system.base.device.setup.set(absolute_item_name = ['abc1', 'abc2', 'abc3'], instrument = [1, 2, 3]) \n
		No command help available \n
			:param absolute_item_name: No help available
			:param instrument: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('absolute_item_name', absolute_item_name, DataType.StringList, None, True, True, 1), ArgSingle('instrument', instrument, DataType.IntegerList, None, True, True, 1))
		self._core.io.write(f'SYSTem:BASE:DEVice:SETup {param}'.rstrip())

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Response structure. Fields: \n
			- Absolute_Item_Name: List[str]: No parameter help available
			- Instrument: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Absolute_Item_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Instrument', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Absolute_Item_Name: List[str] = None
			self.Instrument: List[int] = None

	def get(self) -> SetupStruct:
		"""SCPI: SYSTem:BASE:DEVice:SETup \n
		Snippet: value: SetupStruct = driver.system.base.device.setup.get() \n
		No command help available \n
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:BASE:DEVice:SETup?', self.__class__.SetupStruct())
