from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BoxCls:
	"""Box commands group definition. 2 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: Box, default value after init: Box.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("box", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_box_get', 'repcap_box_set', repcap.Box.Nr1)

	def repcap_box_set(self, box: repcap.Box) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Box.Default
		Default value after init: Box.Nr1"""
		self._cmd_group.set_repcap_enum_value(box)

	def repcap_box_get(self) -> repcap.Box:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def apreset(self):
		"""apreset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_apreset'):
			from .Apreset import ApresetCls
			self._apreset = ApresetCls(self._core, self._cmd_group)
		return self._apreset

	def clone(self) -> 'BoxCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BoxCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
