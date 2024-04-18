from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdeviceCls:
	"""Edevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edevice", core, parent)

	def set(self, device_type: enums.DeviceType, device_mode: enums.DeviceMode) -> None:
		"""SCPI: [CONFigure]:SYSTem:EDEVice \n
		Snippet: driver.configure.system.edevice.set(device_type = enums.DeviceType.NONE, device_mode = enums.DeviceMode.M2X2) \n
		No command help available \n
			:param device_type: No help available
			:param device_mode: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('device_type', device_type, DataType.Enum, enums.DeviceType), ArgSingle('device_mode', device_mode, DataType.Enum, enums.DeviceMode))
		self._core.io.write(f'CONFigure:SYSTem:EDEVice {param}'.rstrip())

	# noinspection PyTypeChecker
	class EdeviceStruct(StructBase):
		"""Response structure. Fields: \n
			- Device_Type: enums.DeviceType: No parameter help available
			- Device_Mode: enums.DeviceMode: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Device_Type', enums.DeviceType),
			ArgStruct.scalar_enum('Device_Mode', enums.DeviceMode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Device_Type: enums.DeviceType = None
			self.Device_Mode: enums.DeviceMode = None

	def get(self) -> EdeviceStruct:
		"""SCPI: [CONFigure]:SYSTem:EDEVice \n
		Snippet: value: EdeviceStruct = driver.configure.system.edevice.get() \n
		No command help available \n
			:return: structure: for return value, see the help for EdeviceStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SYSTem:EDEVice?', self.__class__.EdeviceStruct())
