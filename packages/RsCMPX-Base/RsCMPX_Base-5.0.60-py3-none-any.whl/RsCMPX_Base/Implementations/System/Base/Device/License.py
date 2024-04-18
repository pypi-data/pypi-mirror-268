from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LicenseCls:
	"""License commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("license", core, parent)

	def set(self, sw_option: List[str] = None, license_count: List[int] = None, instrument: List[int] = None) -> None:
		"""SCPI: SYSTem:BASE:DEVice:LICense \n
		Snippet: driver.system.base.device.license.set(sw_option = ['abc1', 'abc2', 'abc3'], license_count = [1, 2, 3], instrument = [1, 2, 3]) \n
		No command help available \n
			:param sw_option: No help available
			:param license_count: No help available
			:param instrument: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sw_option', sw_option, DataType.StringList, None, True, True, 1), ArgSingle('license_count', license_count, DataType.IntegerList, None, True, True, 1), ArgSingle('instrument', instrument, DataType.IntegerList, None, True, True, 1))
		self._core.io.write(f'SYSTem:BASE:DEVice:LICense {param}'.rstrip())

	# noinspection PyTypeChecker
	class LicenseStruct(StructBase):
		"""Response structure. Fields: \n
			- Sw_Option: List[str]: No parameter help available
			- License_Count: List[int]: No parameter help available
			- Instrument: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Sw_Option', DataType.StringList, None, False, True, 1),
			ArgStruct('License_Count', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Instrument', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sw_Option: List[str] = None
			self.License_Count: List[int] = None
			self.Instrument: List[int] = None

	def get(self) -> LicenseStruct:
		"""SCPI: SYSTem:BASE:DEVice:LICense \n
		Snippet: value: LicenseStruct = driver.system.base.device.license.get() \n
		No command help available \n
			:return: structure: for return value, see the help for LicenseStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:BASE:DEVice:LICense?', self.__class__.LicenseStruct())
