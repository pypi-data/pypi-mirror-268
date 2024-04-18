from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpcCls:
	"""Ipc commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipc", core, parent)

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	def initiate(self) -> None:
		"""SCPI: INITiate:BASE:IPC \n
		Snippet: driver.base.ipc.initiate() \n
		No command help available \n
		"""
		self._core.io.write(f'INITiate:BASE:IPC')

	def initiate_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:BASE:IPC \n
		Snippet: driver.base.ipc.initiate_with_opc() \n
		No command help available \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:BASE:IPC', opc_timeout_ms)

	def abort(self) -> None:
		"""SCPI: ABORt:BASE:IPC \n
		Snippet: driver.base.ipc.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'ABORt:BASE:IPC')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:BASE:IPC \n
		Snippet: driver.base.ipc.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:BASE:IPC', opc_timeout_ms)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.ResourceState:
		"""SCPI: FETCh:BASE:IPC \n
		Snippet: value: enums.ResourceState = driver.base.ipc.fetch() \n
		No command help available \n
			:return: meas_status: No help available"""
		response = self._core.io.query_str(f'FETCh:BASE:IPC?')
		return Conversions.str_to_scalar_enum(response, enums.ResourceState)

	def clone(self) -> 'IpcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
