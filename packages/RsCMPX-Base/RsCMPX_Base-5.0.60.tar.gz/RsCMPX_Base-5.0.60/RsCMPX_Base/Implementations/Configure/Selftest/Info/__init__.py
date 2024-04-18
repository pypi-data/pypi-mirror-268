from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InfoCls:
	"""Info commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	@property
	def message(self):
		"""message commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_message'):
			from .Message import MessageCls
			self._message = MessageCls(self._core, self._cmd_group)
		return self._message

	@property
	def description(self):
		"""description commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_description'):
			from .Description import DescriptionCls
			self._description = DescriptionCls(self._core, self._cmd_group)
		return self._description

	def get_progress(self) -> str:
		"""SCPI: CONFigure:SELFtest:INFO:PROGress \n
		Snippet: value: str = driver.configure.selftest.info.get_progress() \n
		No command help available \n
			:return: progress: No help available
		"""
		response = self._core.io.query_str('CONFigure:SELFtest:INFO:PROGress?')
		return trim_str_response(response)

	def clone(self) -> 'InfoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InfoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
