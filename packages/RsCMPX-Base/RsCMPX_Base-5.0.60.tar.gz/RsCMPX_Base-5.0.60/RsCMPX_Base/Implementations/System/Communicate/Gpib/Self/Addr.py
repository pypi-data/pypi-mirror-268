from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AddrCls:
	"""Addr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("addr", core, parent)

	def set(self, adress_no: int, gpibInstance=repcap.GpibInstance.Default) -> None:
		"""SCPI: SYSTem:COMMunicate:GPIB<inst>[:SELF]:ADDR \n
		Snippet: driver.system.communicate.gpib.self.addr.set(adress_no = 1, gpibInstance = repcap.GpibInstance.Default) \n
		No command help available \n
			:param adress_no: No help available
			:param gpibInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Gpib')
		"""
		param = Conversions.decimal_value_to_str(adress_no)
		gpibInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(gpibInstance, repcap.GpibInstance)
		self._core.io.write(f'SYSTem:COMMunicate:GPIB{gpibInstance_cmd_val}:SELF:ADDR {param}')

	def get(self, gpibInstance=repcap.GpibInstance.Default) -> int:
		"""SCPI: SYSTem:COMMunicate:GPIB<inst>[:SELF]:ADDR \n
		Snippet: value: int = driver.system.communicate.gpib.self.addr.get(gpibInstance = repcap.GpibInstance.Default) \n
		No command help available \n
			:param gpibInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Gpib')
			:return: adress_no: No help available"""
		gpibInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(gpibInstance, repcap.GpibInstance)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:GPIB{gpibInstance_cmd_val}:SELF:ADDR?')
		return Conversions.str_to_int(response)
