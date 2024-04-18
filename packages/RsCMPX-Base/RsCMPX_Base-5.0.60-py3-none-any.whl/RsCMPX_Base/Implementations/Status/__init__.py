from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatusCls:
	"""Status commands group definition. 37 total commands, 7 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	@property
	def condition(self):
		"""condition commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_condition'):
			from .Condition import ConditionCls
			self._condition = ConditionCls(self._core, self._cmd_group)
		return self._condition

	@property
	def event(self):
		"""event commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_event'):
			from .Event import EventCls
			self._event = EventCls(self._core, self._cmd_group)
		return self._event

	@property
	def queue(self):
		"""queue commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_queue'):
			from .Queue import QueueCls
			self._queue = QueueCls(self._core, self._cmd_group)
		return self._queue

	@property
	def operation(self):
		"""operation commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_operation'):
			from .Operation import OperationCls
			self._operation = OperationCls(self._core, self._cmd_group)
		return self._operation

	@property
	def questionable(self):
		"""questionable commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_questionable'):
			from .Questionable import QuestionableCls
			self._questionable = QuestionableCls(self._core, self._cmd_group)
		return self._questionable

	@property
	def measurement(self):
		"""measurement commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import MeasurementCls
			self._measurement = MeasurementCls(self._core, self._cmd_group)
		return self._measurement

	@property
	def generator(self):
		"""generator commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import GeneratorCls
			self._generator = GeneratorCls(self._core, self._cmd_group)
		return self._generator

	def preset(self) -> None:
		"""SCPI: STATus:PRESet \n
		Snippet: driver.status.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'STATus:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STATus:PRESet \n
		Snippet: driver.status.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STATus:PRESet', opc_timeout_ms)

	def clone(self) -> 'StatusCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StatusCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
