from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsoluteCls:
	"""Absolute commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	@property
	def set(self):
		"""set commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_set'):
			from .Set import SetCls
			self._set = SetCls(self._core, self._cmd_group)
		return self._set

	def clear(self) -> None:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute:CLEar \n
		Snippet: driver.system.time.hrTimer.absolute.clear() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:TIME:HRTimer:ABSolute:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute:CLEar \n
		Snippet: driver.system.time.hrTimer.absolute.clear_with_opc() \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:TIME:HRTimer:ABSolute:CLEar', opc_timeout_ms)

	def set_value(self, duration: float) -> None:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute \n
		Snippet: driver.system.time.hrTimer.absolute.set_value(duration = 1.0) \n
		This command starts a timer. The timeout is specified relative to an already set timestamp, see method RsCMPX_Base.System.
		Time.HrTimer.Absolute.Set.set. When the timer expires, 'Operation Complete' is indicated. This event can be evaluated by
		polling, via a *OPC? or via *WAI. \n
			:param duration: No help available
		"""
		param = Conversions.decimal_value_to_str(duration)
		self._core.io.write_with_opc(f'SYSTem:TIME:HRTimer:ABSolute {param}')

	def clone(self) -> 'AbsoluteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AbsoluteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
