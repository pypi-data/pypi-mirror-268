from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HistoryCls:
	"""History commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("history", core, parent)

	@property
	def entry(self):
		"""entry commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_entry'):
			from .Entry import EntryCls
			self._entry = EntryCls(self._core, self._cmd_group)
		return self._entry

	def get_count(self) -> int:
		"""SCPI: SYSTem:DFPRint:HISTory:COUNt \n
		Snippet: value: int = driver.system.deviceFootprint.history.get_count() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('SYSTem:DFPRint:HISTory:COUNt?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'HistoryCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HistoryCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
