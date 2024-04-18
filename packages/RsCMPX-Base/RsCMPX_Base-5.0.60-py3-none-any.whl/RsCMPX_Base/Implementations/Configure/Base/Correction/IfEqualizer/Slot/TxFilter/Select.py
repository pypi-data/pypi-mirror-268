from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, select: List[bool], slot=repcap.Slot.Default) -> None:
		"""SCPI: CONFigure:BASE:CORRection:IFEQualizer:SLOT<Slot>:TXFilter:SELect \n
		Snippet: driver.configure.base.correction.ifEqualizer.slot.txFilter.select.set(select = [True, False, True], slot = repcap.Slot.Default) \n
		No command help available \n
			:param select: No help available
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
		"""
		param = Conversions.list_to_csv_str(select)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		self._core.io.write(f'CONFigure:BASE:CORRection:IFEQualizer:SLOT{slot_cmd_val}:TXFilter:SELect {param}')

	def get(self, slot=repcap.Slot.Default) -> List[bool]:
		"""SCPI: CONFigure:BASE:CORRection:IFEQualizer:SLOT<Slot>:TXFilter:SELect \n
		Snippet: value: List[bool] = driver.configure.base.correction.ifEqualizer.slot.txFilter.select.get(slot = repcap.Slot.Default) \n
		No command help available \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:return: select: No help available"""
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		response = self._core.io.query_str(f'CONFigure:BASE:CORRection:IFEQualizer:SLOT{slot_cmd_val}:TXFilter:SELect?')
		return Conversions.str_to_bool_list(response)
