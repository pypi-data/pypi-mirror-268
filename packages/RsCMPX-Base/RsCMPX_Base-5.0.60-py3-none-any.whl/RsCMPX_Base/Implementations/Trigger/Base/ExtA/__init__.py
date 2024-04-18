from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtACls:
	"""ExtA commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extA", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_source(self) -> str:
		"""SCPI: TRIGger:BASE:EXTA:SOURce \n
		Snippet: value: str = driver.trigger.base.extA.get_source() \n
		Selects the output trigger signals to be routed to the trigger connectors. A list of all supported values can be
		retrieved using TRIGger:BASE:EXTA|EXTB:CATalog:SOURce?. \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('TRIGger:BASE:EXTA:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:BASE:EXTA:SOURce \n
		Snippet: driver.trigger.base.extA.set_source(source = 'abc') \n
		Selects the output trigger signals to be routed to the trigger connectors. A list of all supported values can be
		retrieved using TRIGger:BASE:EXTA|EXTB:CATalog:SOURce?. \n
			:param source: No help available
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:BASE:EXTA:SOURce {param}')

	# noinspection PyTypeChecker
	def get_direction(self) -> enums.DirectionIo:
		"""SCPI: TRIGger:BASE:EXTA:DIRection \n
		Snippet: value: enums.DirectionIo = driver.trigger.base.extA.get_direction() \n
		Configures the trigger connectors as input or output connectors. \n
			:return: direction: IN: Input connector OUT: Output connector
		"""
		response = self._core.io.query_str('TRIGger:BASE:EXTA:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.DirectionIo)

	def set_direction(self, direction: enums.DirectionIo) -> None:
		"""SCPI: TRIGger:BASE:EXTA:DIRection \n
		Snippet: driver.trigger.base.extA.set_direction(direction = enums.DirectionIo.IN) \n
		Configures the trigger connectors as input or output connectors. \n
			:param direction: IN: Input connector OUT: Output connector
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.DirectionIo)
		self._core.io.write(f'TRIGger:BASE:EXTA:DIRection {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlope:
		"""SCPI: TRIGger:BASE:EXTA:SLOPe \n
		Snippet: value: enums.SignalSlope = driver.trigger.base.extA.get_slope() \n
		Specifies whether the rising edge or the falling edge of the trigger pulse is generated at the trigger event. The setting
		applies to output trigger signals provided at the trigger connectors. \n
			:return: slope: REDGe: Rising edge FEDGe: Falling edge
		"""
		response = self._core.io.query_str('TRIGger:BASE:EXTA:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlope)

	def set_slope(self, slope: enums.SignalSlope) -> None:
		"""SCPI: TRIGger:BASE:EXTA:SLOPe \n
		Snippet: driver.trigger.base.extA.set_slope(slope = enums.SignalSlope.FEDGe) \n
		Specifies whether the rising edge or the falling edge of the trigger pulse is generated at the trigger event. The setting
		applies to output trigger signals provided at the trigger connectors. \n
			:param slope: REDGe: Rising edge FEDGe: Falling edge
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlope)
		self._core.io.write(f'TRIGger:BASE:EXTA:SLOPe {param}')

	def clone(self) -> 'ExtACls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ExtACls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
