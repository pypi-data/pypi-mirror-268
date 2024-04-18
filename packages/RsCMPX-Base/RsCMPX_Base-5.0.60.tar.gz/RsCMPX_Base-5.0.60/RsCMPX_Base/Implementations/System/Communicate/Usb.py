from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsbCls:
	"""Usb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usb", core, parent)

	def get_vresource(self) -> str:
		"""SCPI: SYSTem:COMMunicate:USB:VRESource \n
		Snippet: value: str = driver.system.communicate.usb.get_vresource() \n
		Queries the VISA resource string of the USB interface. \n
			:return: visa_resource: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:USB:VRESource?')
		return trim_str_response(response)
