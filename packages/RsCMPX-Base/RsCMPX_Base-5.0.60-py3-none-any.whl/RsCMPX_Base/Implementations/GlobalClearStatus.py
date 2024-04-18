from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GlobalClearStatusCls:
	"""GlobalClearStatus commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("globalClearStatus", core, parent)

	def set(self) -> None:
		"""SCPI: *GCLS \n
		Snippet: driver.globalClearStatus.set() \n
		No command help available \n
		"""
		self._core.io.write(f'*GCLS')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: *GCLS \n
		Snippet: driver.globalClearStatus.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'*GCLS', opc_timeout_ms)
