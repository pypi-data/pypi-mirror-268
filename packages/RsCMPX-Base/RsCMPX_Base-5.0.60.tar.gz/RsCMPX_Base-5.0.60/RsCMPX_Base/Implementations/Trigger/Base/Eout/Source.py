from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: str, eout=repcap.Eout.Default) -> None:
		"""SCPI: TRIGger:BASE:EOUT<n>:SOURce \n
		Snippet: driver.trigger.base.eout.source.set(source = 'abc', eout = repcap.Eout.Default) \n
		No command help available \n
			:param source: No help available
			:param eout: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eout')
		"""
		param = Conversions.value_to_quoted_str(source)
		eout_cmd_val = self._cmd_group.get_repcap_cmd_value(eout, repcap.Eout)
		self._core.io.write(f'TRIGger:BASE:EOUT{eout_cmd_val}:SOURce {param}')

	def get(self, eout=repcap.Eout.Default) -> str:
		"""SCPI: TRIGger:BASE:EOUT<n>:SOURce \n
		Snippet: value: str = driver.trigger.base.eout.source.get(eout = repcap.Eout.Default) \n
		No command help available \n
			:param eout: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eout')
			:return: source: No help available"""
		eout_cmd_val = self._cmd_group.get_repcap_cmd_value(eout, repcap.Eout)
		response = self._core.io.query_str(f'TRIGger:BASE:EOUT{eout_cmd_val}:SOURce?')
		return trim_str_response(response)
