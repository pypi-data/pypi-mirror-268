from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CompassCls:
	"""Compass commands group definition. 12 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("compass", core, parent)

	@property
	def statistics(self):
		"""statistics commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_statistics'):
			from .Statistics import StatisticsCls
			self._statistics = StatisticsCls(self._core, self._cmd_group)
		return self._statistics

	@property
	def debug(self):
		"""debug commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_debug'):
			from .Debug import DebugCls
			self._debug = DebugCls(self._core, self._cmd_group)
		return self._debug

	@property
	def dbase(self):
		"""dbase commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dbase'):
			from .Dbase import DbaseCls
			self._dbase = DbaseCls(self._core, self._cmd_group)
		return self._dbase

	def get_version(self) -> str:
		"""SCPI: DIAGnostic:COMPass:VERSion \n
		Snippet: value: str = driver.diagnostic.compass.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:COMPass:VERSion?')
		return trim_str_response(response)

	def get_heap_check(self) -> bool:
		"""SCPI: DIAGnostic:COMPass:HEAPcheck \n
		Snippet: value: bool = driver.diagnostic.compass.get_heap_check() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:COMPass:HEAPcheck?')
		return Conversions.str_to_bool(response)

	def set_heap_check(self, enable: bool) -> None:
		"""SCPI: DIAGnostic:COMPass:HEAPcheck \n
		Snippet: driver.diagnostic.compass.set_heap_check(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'DIAGnostic:COMPass:HEAPcheck {param}')

	def clone(self) -> 'CompassCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CompassCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
