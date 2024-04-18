from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TenvironmentCls:
	"""Tenvironment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tenvironment", core, parent)

	def delete(self, name: str) -> None:
		"""SCPI: DELete:SYSTem:ATTenuation:CTABle[:TENVironment] \n
		Snippet: driver.system.attenuation.correctionTable.tenvironment.delete(name = 'abc') \n
		Deletes a channel-specific correction table. \n
			:param name: The name of the correction table to be deleted.
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'DELete:SYSTem:ATTenuation:CTABle:TENVironment {param}')
