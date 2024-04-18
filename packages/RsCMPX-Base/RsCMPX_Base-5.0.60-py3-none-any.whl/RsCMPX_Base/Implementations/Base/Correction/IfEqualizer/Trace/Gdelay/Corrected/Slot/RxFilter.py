from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .........Internal.Types import DataType
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxFilterCls:
	"""RxFilter commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: RxFilter, default value after init: RxFilter.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rxFilter", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_rxFilter_get', 'repcap_rxFilter_set', repcap.RxFilter.Nr1)

	def repcap_rxFilter_set(self, rxFilter: repcap.RxFilter) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RxFilter.Default
		Default value after init: RxFilter.Nr1"""
		self._cmd_group.set_repcap_enum_value(rxFilter)

	def repcap_rxFilter_get(self) -> repcap.RxFilter:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def fetch(self, slot=repcap.Slot.Default, rxFilter=repcap.RxFilter.Default) -> List[float]:
		"""SCPI: FETCh:BASE:CORRection:IFEQualizer:TRACe:GDELay:CORRected:SLOT<Slot>:RXFilter<Filter> \n
		Snippet: value: List[float] = driver.base.correction.ifEqualizer.trace.gdelay.corrected.slot.rxFilter.fetch(slot = repcap.Slot.Default, rxFilter = repcap.RxFilter.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param rxFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RxFilter')
			:return: value: No help available"""
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		rxFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(rxFilter, repcap.RxFilter)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BASE:CORRection:IFEQualizer:TRACe:GDELay:CORRected:SLOT{slot_cmd_val}:RXFilter{rxFilter_cmd_val}?', suppressed)
		return response

	def clone(self) -> 'RxFilterCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxFilterCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
