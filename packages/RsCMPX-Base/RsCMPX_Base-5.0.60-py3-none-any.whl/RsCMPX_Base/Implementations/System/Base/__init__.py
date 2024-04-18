from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BaseCls:
	"""Base commands group definition. 31 total commands, 8 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def ipSet(self):
		"""ipSet commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSet'):
			from .IpSet import IpSetCls
			self._ipSet = IpSetCls(self._core, self._cmd_group)
		return self._ipSet

	@property
	def device(self):
		"""device commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_device'):
			from .Device import DeviceCls
			self._device = DeviceCls(self._core, self._cmd_group)
		return self._device

	@property
	def reference(self):
		"""reference commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import ReferenceCls
			self._reference = ReferenceCls(self._core, self._cmd_group)
		return self._reference

	@property
	def ssync(self):
		"""ssync commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ssync'):
			from .Ssync import SsyncCls
			self._ssync = SsyncCls(self._core, self._cmd_group)
		return self._ssync

	@property
	def option(self):
		"""option commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_option'):
			from .Option import OptionCls
			self._option = OptionCls(self._core, self._cmd_group)
		return self._option

	@property
	def password(self):
		"""password commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_password'):
			from .Password import PasswordCls
			self._password = PasswordCls(self._core, self._cmd_group)
		return self._password

	@property
	def display(self):
		"""display commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_display'):
			from .Display import DisplayCls
			self._display = DisplayCls(self._core, self._cmd_group)
		return self._display

	@property
	def stIcon(self):
		"""stIcon commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_stIcon'):
			from .StIcon import StIconCls
			self._stIcon = StIconCls(self._core, self._cmd_group)
		return self._stIcon

	def get_reliability(self) -> int:
		"""SCPI: SYSTem:BASE:RELiability \n
		Snippet: value: int = driver.system.base.get_reliability() \n
		Returns a reliability value indicating errors detected by the base software. \n
			:return: value: For reliability indicator values, see 'Checking the reliability indicator'.
		"""
		response = self._core.io.query_str('SYSTem:BASE:RELiability?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'BaseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BaseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
