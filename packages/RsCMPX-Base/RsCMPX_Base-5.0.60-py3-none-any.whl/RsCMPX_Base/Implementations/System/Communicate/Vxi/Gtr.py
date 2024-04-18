from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GtrCls:
	"""Gtr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gtr", core, parent)

	def set(self, bool_switchremote: bool, vxiInstance=repcap.VxiInstance.Default) -> None:
		"""SCPI: SYSTem:COMMunicate:VXI<inst>:GTR \n
		Snippet: driver.system.communicate.vxi.gtr.set(bool_switchremote = False, vxiInstance = repcap.VxiInstance.Default) \n
		Enables or disables the VXI-11 interface. \n
			:param bool_switchremote: ON | 1: VXI-11 enabled OFF | 0: VXI-11 disabled
			:param vxiInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Vxi')
		"""
		param = Conversions.bool_to_str(bool_switchremote)
		vxiInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(vxiInstance, repcap.VxiInstance)
		self._core.io.write(f'SYSTem:COMMunicate:VXI{vxiInstance_cmd_val}:GTR {param}')

	def get(self, vxiInstance=repcap.VxiInstance.Default) -> bool:
		"""SCPI: SYSTem:COMMunicate:VXI<inst>:GTR \n
		Snippet: value: bool = driver.system.communicate.vxi.gtr.get(vxiInstance = repcap.VxiInstance.Default) \n
		Enables or disables the VXI-11 interface. \n
			:param vxiInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Vxi')
			:return: bool_switchremote: No help available"""
		vxiInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(vxiInstance, repcap.VxiInstance)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:VXI{vxiInstance_cmd_val}:GTR?')
		return Conversions.str_to_bool(response)
