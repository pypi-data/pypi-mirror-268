from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 94 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def spoint(self):
		"""spoint commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_spoint'):
			from .Spoint import SpointCls
			self._spoint = SpointCls(self._core, self._cmd_group)
		return self._spoint

	@property
	def semaphore(self):
		"""semaphore commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_semaphore'):
			from .Semaphore import SemaphoreCls
			self._semaphore = SemaphoreCls(self._core, self._cmd_group)
		return self._semaphore

	@property
	def mutex(self):
		"""mutex commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_mutex'):
			from .Mutex import MutexCls
			self._mutex = MutexCls(self._core, self._cmd_group)
		return self._mutex

	@property
	def base(self):
		"""base commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_base'):
			from .Base import BaseCls
			self._base = BaseCls(self._core, self._cmd_group)
		return self._base

	@property
	def freqCorrection(self):
		"""freqCorrection commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_freqCorrection'):
			from .FreqCorrection import FreqCorrectionCls
			self._freqCorrection = FreqCorrectionCls(self._core, self._cmd_group)
		return self._freqCorrection

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmwCls
			self._singleCmw = SingleCmwCls(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def cmwd(self):
		"""cmwd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmwd'):
			from .Cmwd import CmwdCls
			self._cmwd = CmwdCls(self._core, self._cmd_group)
		return self._cmwd

	@property
	def system(self):
		"""system commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_system'):
			from .System import SystemCls
			self._system = SystemCls(self._core, self._cmd_group)
		return self._system

	@property
	def gprf(self):
		"""gprf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gprf'):
			from .Gprf import GprfCls
			self._gprf = GprfCls(self._core, self._cmd_group)
		return self._gprf

	@property
	def tenvironment(self):
		"""tenvironment commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tenvironment'):
			from .Tenvironment import TenvironmentCls
			self._tenvironment = TenvironmentCls(self._core, self._cmd_group)
		return self._tenvironment

	@property
	def selftest(self):
		"""selftest commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_selftest'):
			from .Selftest import SelftestCls
			self._selftest = SelftestCls(self._core, self._cmd_group)
		return self._selftest

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
