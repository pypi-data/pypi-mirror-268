from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TriggerCls:
	"""Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TriggerSource:
		"""SCPI: [CONFigure]:GPRF:MEASurement<Instance>:IQVSlot:TRIGger:SOURce \n
		Snippet: value: enums.TriggerSource = driver.configure.gprf.measurement.iqVsSlot.trigger.get_source() \n
		No command help available \n
			:return: trigger: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TRIGger:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSource)

	def set_source(self, trigger: enums.TriggerSource) -> None:
		"""SCPI: [CONFigure]:GPRF:MEASurement<Instance>:IQVSlot:TRIGger:SOURce \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.trigger.set_source(trigger = enums.TriggerSource.EXTernal) \n
		No command help available \n
			:param trigger: No help available
		"""
		param = Conversions.enum_scalar_to_str(trigger, enums.TriggerSource)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TRIGger:SOURce {param}')
