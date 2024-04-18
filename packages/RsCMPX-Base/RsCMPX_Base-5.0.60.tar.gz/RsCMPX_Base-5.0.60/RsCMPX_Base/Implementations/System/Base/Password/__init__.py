from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PasswordCls:
	"""Password commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("password", core, parent)

	@property
	def cenable(self):
		"""cenable commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cenable'):
			from .Cenable import CenableCls
			self._cenable = CenableCls(self._core, self._cmd_group)
		return self._cenable

	def set_cdisable(self, user_mode: enums.UserRole) -> None:
		"""SCPI: SYSTem:BASE:PASSword:CDISable \n
		Snippet: driver.system.base.password.set_cdisable(user_mode = enums.UserRole.ADMin) \n
		No command help available \n
			:param user_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(user_mode, enums.UserRole)
		self._core.io.write(f'SYSTem:BASE:PASSword:CDISable {param}')

	def clone(self) -> 'PasswordCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PasswordCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
