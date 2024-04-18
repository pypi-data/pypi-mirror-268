from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SplitCls:
	"""Split commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("split", core, parent)

	def set(self, count: int, direction: enums.DirectionHv) -> None:
		"""SCPI: SYSTem:BASE:DEVice:SPLit \n
		Snippet: driver.system.base.device.split.set(count = 1, direction = enums.DirectionHv.HORizontal) \n
		Splits the instrument into channels or assigns all hardware resources to a single channel. Send this command to the
		channel with the lowest number (device 0 / channel 1 / assigned instrument 1) . To assign/distribute the available
		hardware resources to the channels, a reboot is performed automatically after you have changed the number of channels. \n
			:param count: Number of channels
			:param direction: Direction of the split
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('count', count, DataType.Integer), ArgSingle('direction', direction, DataType.Enum, enums.DirectionHv))
		self._core.io.write(f'SYSTem:BASE:DEVice:SPLit {param}'.rstrip())

	# noinspection PyTypeChecker
	class SplitStruct(StructBase):
		"""Response structure. Fields: \n
			- Count: int: Number of channels
			- Direction: enums.DirectionHv: Direction of the split"""
		__meta_args_list = [
			ArgStruct.scalar_int('Count'),
			ArgStruct.scalar_enum('Direction', enums.DirectionHv)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Count: int = None
			self.Direction: enums.DirectionHv = None

	def get(self) -> SplitStruct:
		"""SCPI: SYSTem:BASE:DEVice:SPLit \n
		Snippet: value: SplitStruct = driver.system.base.device.split.get() \n
		Splits the instrument into channels or assigns all hardware resources to a single channel. Send this command to the
		channel with the lowest number (device 0 / channel 1 / assigned instrument 1) . To assign/distribute the available
		hardware resources to the channels, a reboot is performed automatically after you have changed the number of channels. \n
			:return: structure: for return value, see the help for SplitStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:BASE:DEVice:SPLit?', self.__class__.SplitStruct())
