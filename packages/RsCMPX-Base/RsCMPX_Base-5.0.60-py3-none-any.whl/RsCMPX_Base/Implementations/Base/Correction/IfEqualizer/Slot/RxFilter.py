from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxFilterCls:
	"""RxFilter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rxFilter", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, slot=repcap.Slot.Default) -> List[enums.CorrResult]:
		"""SCPI: FETCh:BASE:CORRection:IFEQualizer:SLOT<Slot>:RXFilter \n
		Snippet: value: List[enums.CorrResult] = driver.base.correction.ifEqualizer.slot.rxFilter.fetch(slot = repcap.Slot.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:return: value: No help available"""
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BASE:CORRection:IFEQualizer:SLOT{slot_cmd_val}:RXFilter?', suppressed)
		return Conversions.str_to_list_enum(response, enums.CorrResult)
