from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VresourceCls:
	"""Vresource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vresource", core, parent)

	def get(self, socketInstance=repcap.SocketInstance.Default) -> str:
		"""SCPI: SYSTem:COMMunicate:SOCKet<inst>:VRESource \n
		Snippet: value: str = driver.system.communicate.socket.vresource.get(socketInstance = repcap.SocketInstance.Default) \n
		Queries the VISA resource string for direct socket communication. \n
			:param socketInstance: optional repeated capability selector. Default value: Inst1 (settable in the interface 'Socket')
			:return: visa_resource: No help available"""
		socketInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(socketInstance, repcap.SocketInstance)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:SOCKet{socketInstance_cmd_val}:VRESource?')
		return trim_str_response(response)
