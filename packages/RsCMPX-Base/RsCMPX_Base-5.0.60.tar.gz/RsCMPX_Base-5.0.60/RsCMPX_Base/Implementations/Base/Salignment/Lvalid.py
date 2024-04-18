from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LvalidCls:
	"""Lvalid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lvalid", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Date: List[str]: No parameter help available
			- Time: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Date', DataType.StringList, None, False, True, 1),
			ArgStruct('Time', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Date: List[str] = None
			self.Time: List[str] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BASE:SALignment:LVALid \n
		Snippet: value: FetchStruct = driver.base.salignment.lvalid.fetch() \n
		Queries the date and time of the last successful execution of the self-alignment procedure. The information is returned
		for the measurement modes IQ and Level: <Date>IQ, <Time>IQ, <Date>level, <Time>level \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BASE:SALignment:LVALid?', self.__class__.FetchStruct())
