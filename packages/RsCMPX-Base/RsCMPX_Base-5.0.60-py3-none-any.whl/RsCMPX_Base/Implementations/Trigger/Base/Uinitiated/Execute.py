from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExecuteCls:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self, trigger=repcap.Trigger.Default) -> None:
		"""SCPI: TRIGger:BASE:UINitiated<n>:EXECute \n
		Snippet: driver.trigger.base.uinitiated.execute.set(trigger = repcap.Trigger.Default) \n
		Initiates the generation of a User Initiated Trigger signal. \n
			:param trigger: optional repeated capability selector. Default value: Trg1 (settable in the interface 'Uinitiated')
		"""
		trigger_cmd_val = self._cmd_group.get_repcap_cmd_value(trigger, repcap.Trigger)
		self._core.io.write(f'TRIGger:BASE:UINitiated{trigger_cmd_val}:EXECute')

	def set_with_opc(self, trigger=repcap.Trigger.Default, opc_timeout_ms: int = -1) -> None:
		trigger_cmd_val = self._cmd_group.get_repcap_cmd_value(trigger, repcap.Trigger)
		"""SCPI: TRIGger:BASE:UINitiated<n>:EXECute \n
		Snippet: driver.trigger.base.uinitiated.execute.set_with_opc(trigger = repcap.Trigger.Default) \n
		Initiates the generation of a User Initiated Trigger signal. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param trigger: optional repeated capability selector. Default value: Trg1 (settable in the interface 'Uinitiated')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TRIGger:BASE:UINitiated{trigger_cmd_val}:EXECute', opc_timeout_ms)
