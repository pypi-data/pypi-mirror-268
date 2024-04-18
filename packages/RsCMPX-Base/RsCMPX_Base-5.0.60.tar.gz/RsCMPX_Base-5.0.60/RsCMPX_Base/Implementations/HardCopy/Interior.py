from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InteriorCls:
	"""Interior commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interior", core, parent)

	def get_data(self) -> bytes:
		"""SCPI: HCOPy:INTerior:DATA \n
		Snippet: value: bytes = driver.hardCopy.interior.get_data() \n
		No command help available \n
			:return: data: No help available
		"""
		response = self._core.io.query_bin_block('HCOPy:INTerior:DATA?')
		return response

	def set_file(self, filename: str) -> None:
		"""SCPI: HCOPy:INTerior:FILE \n
		Snippet: driver.hardCopy.interior.set_file(filename = 'abc') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'HCOPy:INTerior:FILE {param}')
