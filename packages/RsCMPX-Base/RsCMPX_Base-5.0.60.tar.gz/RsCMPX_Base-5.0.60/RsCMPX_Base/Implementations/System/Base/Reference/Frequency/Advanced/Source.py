from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.SourceIntExt, frequency=repcap.Frequency.Default) -> None:
		"""SCPI: SYSTem:BASE:REFerence:FREQuency<n>:ADVanced:SOURce \n
		Snippet: driver.system.base.reference.frequency.advanced.source.set(source = enums.SourceIntExt.EINTernal, frequency = repcap.Frequency.Default) \n
		No command help available \n
			:param source: No help available
			:param frequency: optional repeated capability selector. Default value: Freq1 (settable in the interface 'Frequency')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceIntExt)
		frequency_cmd_val = self._cmd_group.get_repcap_cmd_value(frequency, repcap.Frequency)
		self._core.io.write(f'SYSTem:BASE:REFerence:FREQuency{frequency_cmd_val}:ADVanced:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, frequency=repcap.Frequency.Default) -> enums.SourceIntExt:
		"""SCPI: SYSTem:BASE:REFerence:FREQuency<n>:ADVanced:SOURce \n
		Snippet: value: enums.SourceIntExt = driver.system.base.reference.frequency.advanced.source.get(frequency = repcap.Frequency.Default) \n
		No command help available \n
			:param frequency: optional repeated capability selector. Default value: Freq1 (settable in the interface 'Frequency')
			:return: source: No help available"""
		frequency_cmd_val = self._cmd_group.get_repcap_cmd_value(frequency, repcap.Frequency)
		response = self._core.io.query_str(f'SYSTem:BASE:REFerence:FREQuency{frequency_cmd_val}:ADVanced:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceIntExt)
