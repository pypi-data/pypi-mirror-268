from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeviceCls:
	"""Device commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("device", core, parent)

	def get_id(self) -> str:
		"""SCPI: SYSTem:DEVice:ID \n
		Snippet: value: str = driver.system.device.get_id() \n
		Queries the device identification of the instrument. This ID is important for ordering licenses. \n
			:return: device_id: No help available
		"""
		response = self._core.io.query_str('SYSTem:DEVice:ID?')
		return trim_str_response(response)
