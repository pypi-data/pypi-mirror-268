from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCmwCls:
	"""SingleCmw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("singleCmw", core, parent)

	def set_led_test(self, test: bool) -> None:
		"""SCPI: DIAGnostic:CMWS:LEDTest \n
		Snippet: driver.diagnostic.singleCmw.set_led_test(test = False) \n
		No command help available \n
			:param test: No help available
		"""
		param = Conversions.bool_to_str(test)
		self._core.io.write(f'DIAGnostic:CMWS:LEDTest {param}')
