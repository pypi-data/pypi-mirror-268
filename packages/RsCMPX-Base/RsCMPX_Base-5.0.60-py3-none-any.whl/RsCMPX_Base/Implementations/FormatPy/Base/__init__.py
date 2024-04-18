from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BaseCls:
	"""Base commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	# noinspection PyTypeChecker
	def get_border(self) -> enums.ByteOrder:
		"""SCPI: FORMat:BASE:BORDer \n
		Snippet: value: enums.ByteOrder = driver.formatPy.base.get_border() \n
		No command help available \n
			:return: byte_order: No help available
		"""
		response = self._core.io.query_str('FORMat:BASE:BORDer?')
		return Conversions.str_to_scalar_enum(response, enums.ByteOrder)

	def set_border(self, byte_order: enums.ByteOrder) -> None:
		"""SCPI: FORMat:BASE:BORDer \n
		Snippet: driver.formatPy.base.set_border(byte_order = enums.ByteOrder.NORMal) \n
		No command help available \n
			:param byte_order: No help available
		"""
		param = Conversions.enum_scalar_to_str(byte_order, enums.ByteOrder)
		self._core.io.write(f'FORMat:BASE:BORDer {param}')

	def get_dinterchange(self) -> bool:
		"""SCPI: FORMat:BASE:DINTerchange \n
		Snippet: value: bool = driver.formatPy.base.get_dinterchange() \n
		No command help available \n
			:return: dif_format: No help available
		"""
		response = self._core.io.query_str('FORMat:BASE:DINTerchange?')
		return Conversions.str_to_bool(response)

	def set_dinterchange(self, dif_format: bool) -> None:
		"""SCPI: FORMat:BASE:DINTerchange \n
		Snippet: driver.formatPy.base.set_dinterchange(dif_format = False) \n
		No command help available \n
			:param dif_format: No help available
		"""
		param = Conversions.bool_to_str(dif_format)
		self._core.io.write(f'FORMat:BASE:DINTerchange {param}')

	# noinspection PyTypeChecker
	def get_sregister(self) -> enums.StatRegFormat:
		"""SCPI: FORMat:BASE:SREGister \n
		Snippet: value: enums.StatRegFormat = driver.formatPy.base.get_sregister() \n
		No command help available \n
			:return: status_register_format: No help available
		"""
		response = self._core.io.query_str('FORMat:BASE:SREGister?')
		return Conversions.str_to_scalar_enum(response, enums.StatRegFormat)

	def set_sregister(self, status_register_format: enums.StatRegFormat) -> None:
		"""SCPI: FORMat:BASE:SREGister \n
		Snippet: driver.formatPy.base.set_sregister(status_register_format = enums.StatRegFormat.ASCii) \n
		No command help available \n
			:param status_register_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(status_register_format, enums.StatRegFormat)
		self._core.io.write(f'FORMat:BASE:SREGister {param}')

	def clone(self) -> 'BaseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BaseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
