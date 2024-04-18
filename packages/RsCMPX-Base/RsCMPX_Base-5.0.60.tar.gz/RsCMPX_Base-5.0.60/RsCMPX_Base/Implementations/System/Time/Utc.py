from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UtcCls:
	"""Utc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utc", core, parent)

	def set(self, hour: int, minute: int, second: int) -> None:
		"""SCPI: SYSTem:TIME:UTC \n
		Snippet: driver.system.time.utc.set(hour = 1, minute = 1, second = 1) \n
		Sets the UTC time of the operating system clock. Configuration is only possible for the time source MANual, see method
		RsCMPX_Base.System.Time.source. \n
			:param hour: No help available
			:param minute: No help available
			:param second: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hour', hour, DataType.Integer), ArgSingle('minute', minute, DataType.Integer), ArgSingle('second', second, DataType.Integer))
		self._core.io.write(f'SYSTem:TIME:UTC {param}'.rstrip())

	# noinspection PyTypeChecker
	class UtcStruct(StructBase):
		"""Response structure. Fields: \n
			- Hour: int: No parameter help available
			- Minute: int: No parameter help available
			- Second: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_int('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None
			self.Second: int = None

	def get(self) -> UtcStruct:
		"""SCPI: SYSTem:TIME:UTC \n
		Snippet: value: UtcStruct = driver.system.time.utc.get() \n
		Sets the UTC time of the operating system clock. Configuration is only possible for the time source MANual, see method
		RsCMPX_Base.System.Time.source. \n
			:return: structure: for return value, see the help for UtcStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:TIME:UTC?', self.__class__.UtcStruct())
