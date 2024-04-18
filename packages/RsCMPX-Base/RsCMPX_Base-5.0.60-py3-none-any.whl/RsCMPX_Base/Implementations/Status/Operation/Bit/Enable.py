from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, register_bit: float, bitNr=repcap.BitNr.Default) -> None:
		"""SCPI: STATus:OPERation:BIT<bitno>:ENABle \n
		Snippet: driver.status.operation.bit.enable.set(register_bit = 1.0, bitNr = repcap.BitNr.Default) \n
		No command help available \n
			:param register_bit: No help available
			:param bitNr: optional repeated capability selector. Default value: Nr8 (settable in the interface 'Bit')
		"""
		param = Conversions.decimal_value_to_str(register_bit)
		bitNr_cmd_val = self._cmd_group.get_repcap_cmd_value(bitNr, repcap.BitNr)
		self._core.io.write(f'STATus:OPERation:BIT{bitNr_cmd_val}:ENABle {param}')

	def get(self, bitNr=repcap.BitNr.Default) -> float:
		"""SCPI: STATus:OPERation:BIT<bitno>:ENABle \n
		Snippet: value: float = driver.status.operation.bit.enable.get(bitNr = repcap.BitNr.Default) \n
		No command help available \n
			:param bitNr: optional repeated capability selector. Default value: Nr8 (settable in the interface 'Bit')
			:return: register_bit: No help available"""
		bitNr_cmd_val = self._cmd_group.get_repcap_cmd_value(bitNr, repcap.BitNr)
		response = self._core.io.query_str(f'STATus:OPERation:BIT{bitNr_cmd_val}:ENABle?')
		return Conversions.str_to_float(response)
