from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HelpCls:
	"""Help commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("help", core, parent)

	@property
	def syntax(self):
		"""syntax commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_syntax'):
			from .Syntax import SyntaxCls
			self._syntax = SyntaxCls(self._core, self._cmd_group)
		return self._syntax

	def get_headers(self) -> bytes:
		"""SCPI: DIAGnostic:HELP:HEADers \n
		Snippet: value: bytes = driver.diagnostic.help.get_headers() \n
		No command help available \n
			:return: header: No help available
		"""
		response = self._core.io.query_bin_block('DIAGnostic:HELP:HEADers?')
		return response

	def clone(self) -> 'HelpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HelpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
