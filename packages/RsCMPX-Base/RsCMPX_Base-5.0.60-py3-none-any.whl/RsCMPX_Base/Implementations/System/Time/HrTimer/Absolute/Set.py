from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetCls:
	"""Set commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("set", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute:SET \n
		Snippet: driver.system.time.hrTimer.absolute.set.set() \n
		This command sets a timestamp with the current system time. A timer can be started with a timeout relative to this
		timestamp, see method RsCMPX_Base.System.Time.HrTimer.Absolute.value. An existing timestamp is overwritten. \n
		"""
		self._core.io.write(f'SYSTem:TIME:HRTimer:ABSolute:SET')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute:SET \n
		Snippet: driver.system.time.hrTimer.absolute.set.set_with_opc() \n
		This command sets a timestamp with the current system time. A timer can be started with a timeout relative to this
		timestamp, see method RsCMPX_Base.System.Time.HrTimer.Absolute.value. An existing timestamp is overwritten. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:TIME:HRTimer:ABSolute:SET', opc_timeout_ms)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Year: int: No parameter help available
			- Month: int: No parameter help available
			- Day: int: No parameter help available
			- Hour: int: No parameter help available
			- Min_Py: int: No parameter help available
			- Sec: float: No parameter help available
			- Msec: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Year'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Day'),
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Min_Py'),
			ArgStruct.scalar_float('Sec'),
			ArgStruct.scalar_int('Msec')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: int = None
			self.Month: int = None
			self.Day: int = None
			self.Hour: int = None
			self.Min_Py: int = None
			self.Sec: float = None
			self.Msec: int = None

	def get(self) -> GetStruct:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute:SET \n
		Snippet: value: GetStruct = driver.system.time.hrTimer.absolute.set.get() \n
		This command sets a timestamp with the current system time. A timer can be started with a timeout relative to this
		timestamp, see method RsCMPX_Base.System.Time.HrTimer.Absolute.value. An existing timestamp is overwritten. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:TIME:HRTimer:ABSolute:SET?', self.__class__.GetStruct())
