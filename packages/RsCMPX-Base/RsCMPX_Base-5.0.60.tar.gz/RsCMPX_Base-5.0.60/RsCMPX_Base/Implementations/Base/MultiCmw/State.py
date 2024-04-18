from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Cmw_1: enums.CmwCurrentStatus: No parameter help available
			- Cmw_2: enums.CmwCurrentStatus: No parameter help available
			- Cmw_3: enums.CmwCurrentStatus: No parameter help available
			- Cmw_4: enums.CmwCurrentStatus: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Cmw_1', enums.CmwCurrentStatus),
			ArgStruct.scalar_enum('Cmw_2', enums.CmwCurrentStatus),
			ArgStruct.scalar_enum('Cmw_3', enums.CmwCurrentStatus),
			ArgStruct.scalar_enum('Cmw_4', enums.CmwCurrentStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cmw_1: enums.CmwCurrentStatus = None
			self.Cmw_2: enums.CmwCurrentStatus = None
			self.Cmw_3: enums.CmwCurrentStatus = None
			self.Cmw_4: enums.CmwCurrentStatus = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BASE:MCMW:STATe \n
		Snippet: value: FetchStruct = driver.base.multiCmw.state.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BASE:MCMW:STATe?', self.__class__.FetchStruct())
