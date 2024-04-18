from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GlobaleCls:
	"""Globale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("globale", core, parent)

	def delete(self) -> None:
		"""SCPI: DELete:SYSTem:ATTenuation:CTABle:ALL:GLOBal \n
		Snippet: driver.system.attenuation.correctionTable.all.globale.delete() \n
		Deletes all global correction tables. \n
		"""
		self._core.io.write(f'DELete:SYSTem:ATTenuation:CTABle:ALL:GLOBal')

	def delete_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DELete:SYSTem:ATTenuation:CTABle:ALL:GLOBal \n
		Snippet: driver.system.attenuation.correctionTable.all.globale.delete_with_opc() \n
		Deletes all global correction tables. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DELete:SYSTem:ATTenuation:CTABle:ALL:GLOBal', opc_timeout_ms)
