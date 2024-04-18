from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RestartCls:
	"""Restart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("restart", core, parent)

	def set(self) -> None:
		"""SCPI: [CONFigure]:SYSTem:CONTrol:RESTart \n
		Snippet: driver.configure.system.control.restart.set() \n
		Restarts the test software on the instrument. \n
		"""
		self._core.io.write(f'CONFigure:SYSTem:CONTrol:RESTart')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [CONFigure]:SYSTem:CONTrol:RESTart \n
		Snippet: driver.configure.system.control.restart.set_with_opc() \n
		Restarts the test software on the instrument. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:SYSTem:CONTrol:RESTart', opc_timeout_ms)
