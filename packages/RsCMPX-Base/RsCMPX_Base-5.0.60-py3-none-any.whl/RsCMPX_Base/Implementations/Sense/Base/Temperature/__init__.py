from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TemperatureCls:
	"""Temperature commands group definition. 5 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("temperature", core, parent)

	@property
	def operating(self):
		"""operating commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_operating'):
			from .Operating import OperatingCls
			self._operating = OperatingCls(self._core, self._cmd_group)
		return self._operating

	@property
	def exceeded(self):
		"""exceeded commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_exceeded'):
			from .Exceeded import ExceededCls
			self._exceeded = ExceededCls(self._core, self._cmd_group)
		return self._exceeded

	def get_environment(self) -> float:
		"""SCPI: SENSe:BASE:TEMPerature:ENVironment \n
		Snippet: value: float = driver.sense.base.temperature.get_environment() \n
		No command help available \n
			:return: temperature: No help available
		"""
		response = self._core.io.query_str('SENSe:BASE:TEMPerature:ENVironment?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'TemperatureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TemperatureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
