from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlotCls:
	"""Slot commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: Slot, default value after init: Slot.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slot", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_slot_get', 'repcap_slot_set', repcap.Slot.Nr1)

	def repcap_slot_set(self, slot: repcap.Slot) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Slot.Default
		Default value after init: Slot.Nr1"""
		self._cmd_group.set_repcap_enum_value(slot)

	def repcap_slot_get(self) -> repcap.Slot:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def txFilter(self):
		"""txFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txFilter'):
			from .TxFilter import TxFilterCls
			self._txFilter = TxFilterCls(self._core, self._cmd_group)
		return self._txFilter

	@property
	def rxFilter(self):
		"""rxFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxFilter'):
			from .RxFilter import RxFilterCls
			self._rxFilter = RxFilterCls(self._core, self._cmd_group)
		return self._rxFilter

	def clone(self) -> 'SlotCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SlotCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
