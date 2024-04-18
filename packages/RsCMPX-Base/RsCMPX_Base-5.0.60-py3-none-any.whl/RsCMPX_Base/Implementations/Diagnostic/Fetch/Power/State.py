from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Main_State: enums.TargetStateA: No parameter help available
			- Synch_State: enums.TargetSyncState: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Main_State', enums.TargetStateA),
			ArgStruct.scalar_enum('Synch_State', enums.TargetSyncState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Main_State: enums.TargetStateA = None
			self.Synch_State: enums.TargetSyncState = None

	def get(self, timeout: float = None, target_main_state: enums.TargetStateA = None, target_sync_state: enums.TargetSyncState = None) -> GetStruct:
		"""SCPI: DIAGnostic:FETCh:POWer:STATe \n
		Snippet: value: GetStruct = driver.diagnostic.fetch.power.state.get(timeout = 1.0, target_main_state = enums.TargetStateA.OFF, target_sync_state = enums.TargetSyncState.ADJusted) \n
		No command help available \n
			:param timeout: No help available
			:param target_main_state: No help available
			:param target_sync_state: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('timeout', timeout, DataType.Float, None, is_optional=True), ArgSingle('target_main_state', target_main_state, DataType.Enum, enums.TargetStateA, is_optional=True), ArgSingle('target_sync_state', target_sync_state, DataType.Enum, enums.TargetSyncState, is_optional=True))
		return self._core.io.query_struct(f'DIAGnostic:FETCh:POWer:STATe? {param}'.rstrip(), self.__class__.GetStruct())
