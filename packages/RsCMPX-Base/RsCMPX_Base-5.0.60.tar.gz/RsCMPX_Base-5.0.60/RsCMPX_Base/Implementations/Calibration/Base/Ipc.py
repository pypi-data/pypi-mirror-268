from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpcCls:
	"""Ipc commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipc", core, parent)

	# noinspection PyTypeChecker
	class ResultStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Result_Number: int: No parameter help available
			- Date: str: No parameter help available
			- Result_Text: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Result_Number'),
			ArgStruct.scalar_str('Date'),
			ArgStruct.scalar_str('Result_Text')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Result_Number: int = None
			self.Date: str = None
			self.Result_Text: str = None

	def get_result(self) -> ResultStruct:
		"""SCPI: CALibration:BASE:IPC:RESult \n
		Snippet: value: ResultStruct = driver.calibration.base.ipc.get_result() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultStruct structure arguments.
		"""
		return self._core.io.query_struct('CALibration:BASE:IPC:RESult?', self.__class__.ResultStruct())

	# noinspection PyTypeChecker
	class ValuesStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Min_Py: List[float]: No parameter help available
			- Fmin: List[int]: No parameter help available
			- Max_Py: List[float]: No parameter help available
			- Fmax: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Min_Py', DataType.FloatList, None, False, True, 1),
			ArgStruct('Fmin', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Max_Py', DataType.FloatList, None, False, True, 1),
			ArgStruct('Fmax', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Min_Py: List[float] = None
			self.Fmin: List[int] = None
			self.Max_Py: List[float] = None
			self.Fmax: List[int] = None

	def get_values(self) -> ValuesStruct:
		"""SCPI: CALibration:BASE:IPC:VALues \n
		Snippet: value: ValuesStruct = driver.calibration.base.ipc.get_values() \n
		No command help available \n
			:return: structure: for return value, see the help for ValuesStruct structure arguments.
		"""
		return self._core.io.query_struct('CALibration:BASE:IPC:VALues?', self.__class__.ValuesStruct())

	def get_log(self) -> List[str]:
		"""SCPI: CALibration:BASE:IPC:LOG \n
		Snippet: value: List[str] = driver.calibration.base.ipc.get_log() \n
		No command help available \n
			:return: file_path: No help available
		"""
		response = self._core.io.query_str('CALibration:BASE:IPC:LOG?')
		return Conversions.str_to_str_list(response)
