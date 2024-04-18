from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TraceCls:
	"""Trace commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	@property
	def rxDc(self):
		"""rxDc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxDc'):
			from .RxDc import RxDcCls
			self._rxDc = RxDcCls(self._core, self._cmd_group)
		return self._rxDc

	@property
	def txDc(self):
		"""txDc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txDc'):
			from .TxDc import TxDcCls
			self._txDc = TxDcCls(self._core, self._cmd_group)
		return self._txDc

	@property
	def rxImage(self):
		"""rxImage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxImage'):
			from .RxImage import RxImageCls
			self._rxImage = RxImageCls(self._core, self._cmd_group)
		return self._rxImage

	@property
	def txImage(self):
		"""txImage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txImage'):
			from .TxImage import TxImageCls
			self._txImage = TxImageCls(self._core, self._cmd_group)
		return self._txImage

	def clone(self) -> 'TraceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TraceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
