from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, control: bool) -> None:
		"""SCPI: SOURce:BASE:ADJustment:STATe \n
		Snippet: driver.source.base.adjustment.state.set(control = False) \n
		No command help available \n
			:param control: No help available
		"""
		param = Conversions.bool_to_str(control)
		self._core.io.write_with_opc(f'SOURce:BASE:ADJustment:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BaseAdjState:
		"""SCPI: SOURce:BASE:ADJustment:STATe \n
		Snippet: value: enums.BaseAdjState = driver.source.base.adjustment.state.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str_with_opc(f'SOURce:BASE:ADJustment:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.BaseAdjState)
