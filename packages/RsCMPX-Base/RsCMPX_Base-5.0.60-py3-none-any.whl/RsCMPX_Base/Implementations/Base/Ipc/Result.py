from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Result_Number: int: No parameter help available
			- Date: str: No parameter help available
			- Result_Text: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Result_Number'),
			ArgStruct.scalar_str('Date'),
			ArgStruct.scalar_str('Result_Text')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Result_Number: int = None
			self.Date: str = None
			self.Result_Text: str = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BASE:IPC:RESult \n
		Snippet: value: FetchStruct = driver.base.ipc.result.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BASE:IPC:RESult?', self.__class__.FetchStruct())
