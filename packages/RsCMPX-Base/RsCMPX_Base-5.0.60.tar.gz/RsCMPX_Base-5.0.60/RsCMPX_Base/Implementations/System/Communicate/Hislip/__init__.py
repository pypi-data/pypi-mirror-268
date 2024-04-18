from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HislipCls:
	"""Hislip commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: HislipInstance, default value after init: HislipInstance.Inst1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hislip", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_hislipInstance_get', 'repcap_hislipInstance_set', repcap.HislipInstance.Inst1)

	def repcap_hislipInstance_set(self, hislipInstance: repcap.HislipInstance) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to HislipInstance.Default
		Default value after init: HislipInstance.Inst1"""
		self._cmd_group.set_repcap_enum_value(hislipInstance)

	def repcap_hislipInstance_get(self) -> repcap.HislipInstance:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def vresource(self):
		"""vresource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vresource'):
			from .Vresource import VresourceCls
			self._vresource = VresourceCls(self._core, self._cmd_group)
		return self._vresource

	def clone(self) -> 'HislipCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HislipCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
