from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SalignmentCls:
	"""Salignment commands group definition. 23 total commands, 7 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("salignment", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def lvalid(self):
		"""lvalid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lvalid'):
			from .Lvalid import LvalidCls
			self._lvalid = LvalidCls(self._core, self._cmd_group)
		return self._lvalid

	@property
	def reliability(self):
		"""reliability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reliability'):
			from .Reliability import ReliabilityCls
			self._reliability = ReliabilityCls(self._core, self._cmd_group)
		return self._reliability

	@property
	def trace(self):
		"""trace commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	@property
	def ulimit(self):
		"""ulimit commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulimit'):
			from .Ulimit import UlimitCls
			self._ulimit = UlimitCls(self._core, self._cmd_group)
		return self._ulimit

	@property
	def llimit(self):
		"""llimit commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_llimit'):
			from .Llimit import LlimitCls
			self._llimit = LlimitCls(self._core, self._cmd_group)
		return self._llimit

	@property
	def xvalues(self):
		"""xvalues commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_xvalues'):
			from .Xvalues import XvaluesCls
			self._xvalues = XvaluesCls(self._core, self._cmd_group)
		return self._xvalues

	def initiate(self) -> None:
		"""SCPI: INITiate:BASE:SALignment \n
		Snippet: driver.base.salignment.initiate() \n
		Starts the measurement procedure. \n
		"""
		self._core.io.write(f'INITiate:BASE:SALignment')

	def initiate_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:BASE:SALignment \n
		Snippet: driver.base.salignment.initiate_with_opc() \n
		Starts the measurement procedure. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:BASE:SALignment', opc_timeout_ms)

	def abort(self) -> None:
		"""SCPI: ABORt:BASE:SALignment \n
		Snippet: driver.base.salignment.abort() \n
		Aborts the measurement procedure. \n
		"""
		self._core.io.write(f'ABORt:BASE:SALignment')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:BASE:SALignment \n
		Snippet: driver.base.salignment.abort_with_opc() \n
		Aborts the measurement procedure. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:BASE:SALignment', opc_timeout_ms)

	def stop(self) -> None:
		"""SCPI: STOP:BASE:SALignment \n
		Snippet: driver.base.salignment.stop() \n
		Pauses the measurement procedure. \n
		"""
		self._core.io.write(f'STOP:BASE:SALignment')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:BASE:SALignment \n
		Snippet: driver.base.salignment.stop_with_opc() \n
		Pauses the measurement procedure. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:BASE:SALignment', opc_timeout_ms)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.ResourceState:
		"""SCPI: FETCh:BASE:SALignment \n
		Snippet: value: enums.ResourceState = driver.base.salignment.fetch() \n
		Queries the state of the measurement procedure. \n
			:return: meas_status: OFF: measurement off RUN: measurement running RDY: measurement finished"""
		response = self._core.io.query_str(f'FETCh:BASE:SALignment?')
		return Conversions.str_to_scalar_enum(response, enums.ResourceState)

	def clone(self) -> 'SalignmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SalignmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
