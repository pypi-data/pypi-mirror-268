from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RuleCls:
	"""Rule commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rule", core, parent)

	def get_catalog(self) -> str:
		"""SCPI: SYSTem:TIME:DSTime:RULE:CATalog \n
		Snippet: value: str = driver.system.time.daylightSavingTime.rule.get_catalog() \n
		Returns all time-zone values that can be set via method RsCMPX_Base.System.Time.DaylightSavingTime.Rule.value. \n
			:return: cat: Comma-separated list of all supported values, one string per value.
		"""
		response = self._core.io.query_str('SYSTem:TIME:DSTime:RULE:CATalog?')
		return trim_str_response(response)

	def get_value(self) -> str:
		"""SCPI: SYSTem:TIME:DSTime:RULE \n
		Snippet: value: str = driver.system.time.daylightSavingTime.rule.get_value() \n
		Sets the time zone in the date and time settings of the operating system. The used daylight saving time (DST) rules
		depend on the configured time zone. So this setting influences the automatic adjustment of the local time and date for
		DST. See also method RsCMPX_Base.System.Time.DaylightSavingTime.mode. Modifying the time zone modifies also the
		configured time zone offset, see method RsCMPX_Base.System.Tzone.set. \n
			:return: rule: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:DSTime:RULE?')
		return trim_str_response(response)

	def set_value(self, rule: str) -> None:
		"""SCPI: SYSTem:TIME:DSTime:RULE \n
		Snippet: driver.system.time.daylightSavingTime.rule.set_value(rule = 'abc') \n
		Sets the time zone in the date and time settings of the operating system. The used daylight saving time (DST) rules
		depend on the configured time zone. So this setting influences the automatic adjustment of the local time and date for
		DST. See also method RsCMPX_Base.System.Time.DaylightSavingTime.mode. Modifying the time zone modifies also the
		configured time zone offset, see method RsCMPX_Base.System.Tzone.set. \n
			:param rule: To query a list of all supported strings, use method RsCMPX_Base.System.Time.DaylightSavingTime.Rule.catalog.
		"""
		param = Conversions.value_to_quoted_str(rule)
		self._core.io.write(f'SYSTem:TIME:DSTime:RULE {param}')
