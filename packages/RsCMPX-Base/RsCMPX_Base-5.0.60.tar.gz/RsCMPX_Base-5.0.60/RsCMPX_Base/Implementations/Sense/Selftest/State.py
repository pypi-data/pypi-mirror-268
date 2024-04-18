from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def get_sum(self) -> enums.SelftestSumState:
		"""SCPI: SENSe:SELFtest:STATe:SUM \n
		Snippet: value: enums.SelftestSumState = driver.sense.selftest.state.get_sum() \n
		No command help available \n
			:return: sum_state: No help available
		"""
		response = self._core.io.query_str('SENSe:SELFtest:STATe:SUM?')
		return Conversions.str_to_scalar_enum(response, enums.SelftestSumState)
