from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, gpibInstance=repcap.GpibInstance.Default) -> None:
		"""SCPI: SYSTem:COMMunicate:GPIB<inst>[:SELF]:ENABle \n
		Snippet: driver.system.communicate.gpib.self.enable.set(enable = False, gpibInstance = repcap.GpibInstance.Default) \n
		No command help available \n
			:param enable: No help available
			:param gpibInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Gpib')
		"""
		param = Conversions.bool_to_str(enable)
		gpibInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(gpibInstance, repcap.GpibInstance)
		self._core.io.write(f'SYSTem:COMMunicate:GPIB{gpibInstance_cmd_val}:SELF:ENABle {param}')

	def get(self, gpibInstance=repcap.GpibInstance.Default) -> bool:
		"""SCPI: SYSTem:COMMunicate:GPIB<inst>[:SELF]:ENABle \n
		Snippet: value: bool = driver.system.communicate.gpib.self.enable.get(gpibInstance = repcap.GpibInstance.Default) \n
		No command help available \n
			:param gpibInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Gpib')
			:return: enable: No help available"""
		gpibInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(gpibInstance, repcap.GpibInstance)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:GPIB{gpibInstance_cmd_val}:SELF:ENABle?')
		return Conversions.str_to_bool(response)
