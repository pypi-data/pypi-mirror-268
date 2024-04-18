from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TaLoggingCls:
	"""TaLogging commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("taLogging", core, parent)

	@property
	def protocol(self):
		"""protocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protocol'):
			from .Protocol import ProtocolCls
			self._protocol = ProtocolCls(self._core, self._cmd_group)
		return self._protocol

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	def clear(self) -> None:
		"""SCPI: DIAGnostic:COMPass:DBASe:TALogging:CLEar \n
		Snippet: driver.diagnostic.compass.dbase.taLogging.clear() \n
		No command help available \n
		"""
		self._core.io.write(f'DIAGnostic:COMPass:DBASe:TALogging:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DIAGnostic:COMPass:DBASe:TALogging:CLEar \n
		Snippet: driver.diagnostic.compass.dbase.taLogging.clear_with_opc() \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DIAGnostic:COMPass:DBASe:TALogging:CLEar', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_device(self) -> enums.DiagLoggingDevice:
		"""SCPI: DIAGnostic:COMPass:DBASe:TALogging:DEVice \n
		Snippet: value: enums.DiagLoggingDevice = driver.diagnostic.compass.dbase.taLogging.get_device() \n
		No command help available \n
			:return: device: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:COMPass:DBASe:TALogging:DEVice?')
		return Conversions.str_to_scalar_enum(response, enums.DiagLoggingDevice)

	def set_device(self, device: enums.DiagLoggingDevice) -> None:
		"""SCPI: DIAGnostic:COMPass:DBASe:TALogging:DEVice \n
		Snippet: driver.diagnostic.compass.dbase.taLogging.set_device(device = enums.DiagLoggingDevice.ALL) \n
		No command help available \n
			:param device: No help available
		"""
		param = Conversions.enum_scalar_to_str(device, enums.DiagLoggingDevice)
		self._core.io.write(f'DIAGnostic:COMPass:DBASe:TALogging:DEVice {param}')

	def clone(self) -> 'TaLoggingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TaLoggingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
