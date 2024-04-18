from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OperatingCls:
	"""Operating commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("operating", core, parent)

	@property
	def ambient(self):
		"""ambient commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ambient'):
			from .Ambient import AmbientCls
			self._ambient = AmbientCls(self._core, self._cmd_group)
		return self._ambient

	def get_internal(self) -> float:
		"""SCPI: SENSe:BASE:TEMPerature:OPERating:INTernal \n
		Snippet: value: float = driver.sense.base.temperature.operating.get_internal() \n
		No command help available \n
			:return: temperature: No help available
		"""
		response = self._core.io.query_str('SENSe:BASE:TEMPerature:OPERating:INTernal?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'OperatingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OperatingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
