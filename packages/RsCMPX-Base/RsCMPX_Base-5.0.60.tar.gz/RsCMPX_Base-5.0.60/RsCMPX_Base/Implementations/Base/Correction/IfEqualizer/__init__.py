from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfEqualizerCls:
	"""IfEqualizer commands group definition. 13 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifEqualizer", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def slot(self):
		"""slot commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import SlotCls
			self._slot = SlotCls(self._core, self._cmd_group)
		return self._slot

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	def initiate(self) -> None:
		"""SCPI: INITiate:BASE:CORRection:IFEQualizer \n
		Snippet: driver.base.correction.ifEqualizer.initiate() \n
		No command help available \n
		"""
		self._core.io.write(f'INITiate:BASE:CORRection:IFEQualizer')

	def initiate_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:BASE:CORRection:IFEQualizer \n
		Snippet: driver.base.correction.ifEqualizer.initiate_with_opc() \n
		No command help available \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:BASE:CORRection:IFEQualizer', opc_timeout_ms)

	def abort(self) -> None:
		"""SCPI: ABORt:BASE:CORRection:IFEQualizer \n
		Snippet: driver.base.correction.ifEqualizer.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'ABORt:BASE:CORRection:IFEQualizer')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:BASE:CORRection:IFEQualizer \n
		Snippet: driver.base.correction.ifEqualizer.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:BASE:CORRection:IFEQualizer', opc_timeout_ms)

	def clone(self) -> 'IfEqualizerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IfEqualizerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
