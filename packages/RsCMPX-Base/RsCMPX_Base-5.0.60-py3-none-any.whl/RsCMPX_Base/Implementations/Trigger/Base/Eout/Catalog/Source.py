from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def get(self, eout=repcap.Eout.Default) -> List[str]:
		"""SCPI: TRIGger:BASE:EOUT<n>:CATalog:SOURce \n
		Snippet: value: List[str] = driver.trigger.base.eout.catalog.source.get(eout = repcap.Eout.Default) \n
		No command help available \n
			:param eout: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eout')
			:return: source_list: No help available"""
		eout_cmd_val = self._cmd_group.get_repcap_cmd_value(eout, repcap.Eout)
		response = self._core.io.query_str(f'TRIGger:BASE:EOUT{eout_cmd_val}:CATalog:SOURce?')
		return Conversions.str_to_str_list(response)
