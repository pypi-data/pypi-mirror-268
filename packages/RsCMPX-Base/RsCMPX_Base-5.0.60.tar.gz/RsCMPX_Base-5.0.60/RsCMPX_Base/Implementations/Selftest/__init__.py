from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelftestCls:
	"""Selftest commands group definition. 12 total commands, 4 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selftest", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def passed(self):
		"""passed commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_passed'):
			from .Passed import PassedCls
			self._passed = PassedCls(self._core, self._cmd_group)
		return self._passed

	@property
	def failed(self):
		"""failed commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_failed'):
			from .Failed import FailedCls
			self._failed = FailedCls(self._core, self._cmd_group)
		return self._failed

	@property
	def skipped(self):
		"""skipped commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_skipped'):
			from .Skipped import SkippedCls
			self._skipped = SkippedCls(self._core, self._cmd_group)
		return self._skipped

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:SELFtest \n
		Snippet: driver.selftest.abort() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:SELFtest', opc_timeout_ms)

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:SELFtest \n
		Snippet: driver.selftest.stop() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:SELFtest', opc_timeout_ms)

	def fetch(self, filter_py: str = None) -> List[str]:
		"""SCPI: FETCh:SELFtest \n
		Snippet: value: List[str] = driver.selftest.fetch(filter_py = 'abc') \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param filter_py: No help available
			:return: value: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:SELFtest? {param}'.rstrip(), suppressed)
		return Conversions.str_to_str_list(response)

	def read(self, filter_py: str = None) -> List[str]:
		"""SCPI: READ:SELFtest \n
		Snippet: value: List[str] = driver.selftest.read(filter_py = 'abc') \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param filter_py: No help available
			:return: value: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:SELFtest? {param}'.rstrip(), suppressed)
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'SelftestCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SelftestCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
