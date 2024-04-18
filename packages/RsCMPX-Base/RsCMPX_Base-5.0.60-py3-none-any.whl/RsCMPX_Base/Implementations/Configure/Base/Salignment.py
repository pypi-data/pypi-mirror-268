from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SalignmentCls:
	"""Salignment commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("salignment", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SalignmentMode:
		"""SCPI: CONFigure:BASE:SALignment:MODE \n
		Snippet: value: enums.SalignmentMode = driver.configure.base.salignment.get_mode() \n
		Selects the measurement mode for self-alignment. \n
			:return: mode: Mode IQ, Level, Verify IQ
		"""
		response = self._core.io.query_str('CONFigure:BASE:SALignment:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SalignmentMode)

	def set_mode(self, mode: enums.SalignmentMode) -> None:
		"""SCPI: CONFigure:BASE:SALignment:MODE \n
		Snippet: driver.configure.base.salignment.set_mode(mode = enums.SalignmentMode.FLEVel) \n
		Selects the measurement mode for self-alignment. \n
			:param mode: Mode IQ, Level, Verify IQ
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SalignmentMode)
		self._core.io.write(f'CONFigure:BASE:SALignment:MODE {param}')

	def get_slot(self) -> str:
		"""SCPI: CONFigure:BASE:SALignment:SLOT \n
		Snippet: value: str = driver.configure.base.salignment.get_slot() \n
		No command help available \n
			:return: slot: No help available
		"""
		response = self._core.io.query_str('CONFigure:BASE:SALignment:SLOT?')
		return trim_str_response(response)

	def set_slot(self, slot: str) -> None:
		"""SCPI: CONFigure:BASE:SALignment:SLOT \n
		Snippet: driver.configure.base.salignment.set_slot(slot = 'abc') \n
		No command help available \n
			:param slot: No help available
		"""
		param = Conversions.value_to_quoted_str(slot)
		self._core.io.write(f'CONFigure:BASE:SALignment:SLOT {param}')
