from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FileCls:
	"""File commands group definition. 11 total commands, 11 Subgroups, 0 group commands
	Repeated Capability: FileNr, default value after init: FileNr.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_fileNr_get', 'repcap_fileNr_set', repcap.FileNr.Nr1)

	def repcap_fileNr_set(self, fileNr: repcap.FileNr) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FileNr.Default
		Default value after init: FileNr.Nr1"""
		self._cmd_group.set_repcap_enum_value(fileNr)

	def repcap_fileNr_get(self) -> repcap.FileNr:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def dexecution(self):
		"""dexecution commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dexecution'):
			from .Dexecution import DexecutionCls
			self._dexecution = DexecutionCls(self._core, self._cmd_group)
		return self._dexecution

	@property
	def stopMode(self):
		"""stopMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stopMode'):
			from .StopMode import StopModeCls
			self._stopMode = StopModeCls(self._core, self._cmd_group)
		return self._stopMode

	@property
	def startMode(self):
		"""startMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_startMode'):
			from .StartMode import StartModeCls
			self._startMode = StartModeCls(self._core, self._cmd_group)
		return self._startMode

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import NameCls
			self._name = NameCls(self._core, self._cmd_group)
		return self._name

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPyCls
			self._formatPy = FormatPyCls(self._core, self._cmd_group)
		return self._formatPy

	@property
	def size(self):
		"""size commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_size'):
			from .Size import SizeCls
			self._size = SizeCls(self._core, self._cmd_group)
		return self._size

	@property
	def rpc(self):
		"""rpc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpc'):
			from .Rpc import RpcCls
			self._rpc = RpcCls(self._core, self._cmd_group)
		return self._rpc

	@property
	def functions(self):
		"""functions commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_functions'):
			from .Functions import FunctionsCls
			self._functions = FunctionsCls(self._core, self._cmd_group)
		return self._functions

	@property
	def parser(self):
		"""parser commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_parser'):
			from .Parser import ParserCls
			self._parser = ParserCls(self._core, self._cmd_group)
		return self._parser

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	def clone(self) -> 'FileCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FileCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
