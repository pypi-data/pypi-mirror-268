from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class JoinCls:
	"""Join commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("join", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Count: int: No parameter help available
			- Result: enums.SyncResult: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Count'),
			ArgStruct.scalar_enum('Result', enums.SyncResult)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Count: int = None
			self.Result: enums.SyncResult = None

	def get(self, name: str, action: enums.JoinAction = None, polling: enums.SyncPolling = None, poll_interval: float = None) -> GetStruct:
		"""SCPI: CONFigure:SPOint:JOIN \n
		Snippet: value: GetStruct = driver.configure.spoint.join.get(name = 'abc', action = enums.JoinAction.CTASk, polling = enums.SyncPolling.NPOLling, poll_interval = 1.0) \n
		No command help available \n
			:param name: No help available
			:param action: No help available
			:param polling: No help available
			:param poll_interval: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('action', action, DataType.Enum, enums.JoinAction, is_optional=True), ArgSingle('polling', polling, DataType.Enum, enums.SyncPolling, is_optional=True), ArgSingle('poll_interval', poll_interval, DataType.Float, None, is_optional=True))
		return self._core.io.query_struct(f'CONFigure:SPOint:JOIN? {param}'.rstrip(), self.__class__.GetStruct())
