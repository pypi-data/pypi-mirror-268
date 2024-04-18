from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrachCls:
	"""Prach commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_source(self) -> str:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:PRACh:SOURce \n
		Snippet: value: str = driver.trigger.nrSub.measurement.prach.get_source() \n
		No command help available \n
			:return: trigger: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRSub:MEASurement<Instance>:PRACh:SOURce?')
		return trim_str_response(response)

	def set_source(self, trigger: str) -> None:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:PRACh:SOURce \n
		Snippet: driver.trigger.nrSub.measurement.prach.set_source(trigger = 'abc') \n
		No command help available \n
			:param trigger: No help available
		"""
		param = Conversions.value_to_quoted_str(trigger)
		self._core.io.write(f'TRIGger:NRSub:MEASurement<Instance>:PRACh:SOURce {param}')

	def clone(self) -> 'PrachCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrachCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
