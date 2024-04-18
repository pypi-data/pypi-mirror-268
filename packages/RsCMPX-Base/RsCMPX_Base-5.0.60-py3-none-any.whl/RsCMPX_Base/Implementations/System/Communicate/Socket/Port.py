from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PortCls:
	"""Port commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("port", core, parent)

	def set(self, port_number: int, socketInstance=repcap.SocketInstance.Default) -> None:
		"""SCPI: SYSTem:COMMunicate:SOCKet<inst>:PORT \n
		Snippet: driver.system.communicate.socket.port.set(port_number = 1, socketInstance = repcap.SocketInstance.Default) \n
		Sets the data port number for direct socket communication. \n
			:param port_number: No help available
			:param socketInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Socket')
		"""
		param = Conversions.decimal_value_to_str(port_number)
		socketInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(socketInstance, repcap.SocketInstance)
		self._core.io.write(f'SYSTem:COMMunicate:SOCKet{socketInstance_cmd_val}:PORT {param}')

	def get(self, socketInstance=repcap.SocketInstance.Default) -> int:
		"""SCPI: SYSTem:COMMunicate:SOCKet<inst>:PORT \n
		Snippet: value: int = driver.system.communicate.socket.port.get(socketInstance = repcap.SocketInstance.Default) \n
		Sets the data port number for direct socket communication. \n
			:param socketInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Socket')
			:return: port_number: No help available"""
		socketInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(socketInstance, repcap.SocketInstance)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:SOCKet{socketInstance_cmd_val}:PORT?')
		return Conversions.str_to_int(response)
