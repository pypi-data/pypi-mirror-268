from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NtransitionCls:
	"""Ntransition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntransition", core, parent)

	def set(self, register_bit: bool, bitNr=repcap.BitNr.Default) -> None:
		"""SCPI: STATus:QUEStionable:BIT<bitno>:NTRansition \n
		Snippet: driver.status.questionable.bit.ntransition.set(register_bit = False, bitNr = repcap.BitNr.Default) \n
		No command help available \n
			:param register_bit: No help available
			:param bitNr: optional repeated capability selector. Default value: Nr8 (settable in the interface 'Bit')
		"""
		param = Conversions.bool_to_str(register_bit)
		bitNr_cmd_val = self._cmd_group.get_repcap_cmd_value(bitNr, repcap.BitNr)
		self._core.io.write(f'STATus:QUEStionable:BIT{bitNr_cmd_val}:NTRansition {param}')

	def get(self, bitNr=repcap.BitNr.Default) -> bool:
		"""SCPI: STATus:QUEStionable:BIT<bitno>:NTRansition \n
		Snippet: value: bool = driver.status.questionable.bit.ntransition.get(bitNr = repcap.BitNr.Default) \n
		No command help available \n
			:param bitNr: optional repeated capability selector. Default value: Nr8 (settable in the interface 'Bit')
			:return: register_bit: No help available"""
		bitNr_cmd_val = self._cmd_group.get_repcap_cmd_value(bitNr, repcap.BitNr)
		response = self._core.io.query_str(f'STATus:QUEStionable:BIT{bitNr_cmd_val}:NTRansition?')
		return Conversions.str_to_bool(response)
