from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RloggingCls:
	"""Rlogging commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlogging", core, parent)

	@property
	def protocol(self):
		"""protocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protocol'):
			from .Protocol import ProtocolCls
			self._protocol = ProtocolCls(self._core, self._cmd_group)
		return self._protocol

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DiagLoggigMode:
		"""SCPI: DIAGnostic:COMPass:DBASe:RLOGging:MODE \n
		Snippet: value: enums.DiagLoggigMode = driver.diagnostic.compass.dbase.rlogging.get_mode() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:COMPass:DBASe:RLOGging:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DiagLoggigMode)

	def set_mode(self, arg_0: enums.DiagLoggigMode) -> None:
		"""SCPI: DIAGnostic:COMPass:DBASe:RLOGging:MODE \n
		Snippet: driver.diagnostic.compass.dbase.rlogging.set_mode(arg_0 = enums.DiagLoggigMode.DETailed) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.DiagLoggigMode)
		self._core.io.write(f'DIAGnostic:COMPass:DBASe:RLOGging:MODE {param}')

	# noinspection PyTypeChecker
	def get_device(self) -> enums.DiagLoggingDevice:
		"""SCPI: DIAGnostic:COMPass:DBASe:RLOGging:DEVice \n
		Snippet: value: enums.DiagLoggingDevice = driver.diagnostic.compass.dbase.rlogging.get_device() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:COMPass:DBASe:RLOGging:DEVice?')
		return Conversions.str_to_scalar_enum(response, enums.DiagLoggingDevice)

	def set_device(self, arg_0: enums.DiagLoggingDevice) -> None:
		"""SCPI: DIAGnostic:COMPass:DBASe:RLOGging:DEVice \n
		Snippet: driver.diagnostic.compass.dbase.rlogging.set_device(arg_0 = enums.DiagLoggingDevice.ALL) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.DiagLoggingDevice)
		self._core.io.write(f'DIAGnostic:COMPass:DBASe:RLOGging:DEVice {param}')

	def clear(self) -> None:
		"""SCPI: DIAGnostic:COMPass:DBASe:RLOGging:CLEar \n
		Snippet: driver.diagnostic.compass.dbase.rlogging.clear() \n
		No command help available \n
		"""
		self._core.io.write(f'DIAGnostic:COMPass:DBASe:RLOGging:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DIAGnostic:COMPass:DBASe:RLOGging:CLEar \n
		Snippet: driver.diagnostic.compass.dbase.rlogging.clear_with_opc() \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DIAGnostic:COMPass:DBASe:RLOGging:CLEar', opc_timeout_ms)

	def clone(self) -> 'RloggingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RloggingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
