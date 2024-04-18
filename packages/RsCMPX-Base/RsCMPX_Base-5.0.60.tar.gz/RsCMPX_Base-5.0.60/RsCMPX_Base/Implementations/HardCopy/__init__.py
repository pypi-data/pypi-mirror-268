from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HardCopyCls:
	"""HardCopy commands group definition. 6 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hardCopy", core, parent)

	@property
	def device(self):
		"""device commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_device'):
			from .Device import DeviceCls
			self._device = DeviceCls(self._core, self._cmd_group)
		return self._device

	@property
	def interior(self):
		"""interior commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_interior'):
			from .Interior import InteriorCls
			self._interior = InteriorCls(self._core, self._cmd_group)
		return self._interior

	# noinspection PyTypeChecker
	def get_area(self) -> enums.HardcopyArea:
		"""SCPI: HCOPy:AREA \n
		Snippet: value: enums.HardcopyArea = driver.hardCopy.get_area() \n
		No command help available \n
			:return: area: No help available
		"""
		response = self._core.io.query_str('HCOPy:AREA?')
		return Conversions.str_to_scalar_enum(response, enums.HardcopyArea)

	def set_area(self, area: enums.HardcopyArea) -> None:
		"""SCPI: HCOPy:AREA \n
		Snippet: driver.hardCopy.set_area(area = enums.HardcopyArea.AWINdow) \n
		No command help available \n
			:param area: No help available
		"""
		param = Conversions.enum_scalar_to_str(area, enums.HardcopyArea)
		self._core.io.write(f'HCOPy:AREA {param}')

	def get_data(self) -> bytes:
		"""SCPI: HCOPy:DATA \n
		Snippet: value: bytes = driver.hardCopy.get_data() \n
		No command help available \n
			:return: data: No help available
		"""
		response = self._core.io.query_bin_block('HCOPy:DATA?')
		return response

	def set_file(self, filename: str) -> None:
		"""SCPI: HCOPy:FILE \n
		Snippet: driver.hardCopy.set_file(filename = 'abc') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'HCOPy:FILE {param}')

	def clone(self) -> 'HardCopyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HardCopyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
