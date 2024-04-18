from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnumberCls:
	"""Snumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snumber", core, parent)

	def fetch(self, box_nr: enums.BoxNumber) -> str:
		"""SCPI: FETCh:BASE:MCMW:SNUMber \n
		Snippet: value: str = driver.base.multiCmw.snumber.fetch(box_nr = enums.BoxNumber.BOX1) \n
		No command help available \n
			:param box_nr: No help available
			:return: serial_number: No help available"""
		param = Conversions.enum_scalar_to_str(box_nr, enums.BoxNumber)
		response = self._core.io.query_str(f'FETCh:BASE:MCMW:SNUMber? {param}')
		return trim_str_response(response)
