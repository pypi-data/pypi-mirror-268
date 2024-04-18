from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 8 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def hdr(self):
		"""hdr commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_hdr'):
			from .Hdr import HdrCls
			self._hdr = HdrCls(self._core, self._cmd_group)
		return self._hdr

	@property
	def hdrp(self):
		"""hdrp commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_hdrp'):
			from .Hdrp import HdrpCls
			self._hdrp = HdrpCls(self._core, self._cmd_group)
		return self._hdrp

	@property
	def bhRate(self):
		"""bhRate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_bhRate'):
			from .BhRate import BhRateCls
			self._bhRate = BhRateCls(self._core, self._cmd_group)
		return self._bhRate

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
