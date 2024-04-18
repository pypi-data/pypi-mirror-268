from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdsCls:
	"""Ids commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ids", core, parent)

	def get(self, ielement_id: float) -> str:
		"""SCPI: DIAGnostic:FOOTprint:ELEMent:CONNection:TARGet:IDS \n
		Snippet: value: str = driver.diagnostic.footPrint.element.connection.target.ids.get(ielement_id = 1.0) \n
		No command help available \n
			:param ielement_id: No help available
			:return: starget_ids: No help available"""
		param = Conversions.decimal_value_to_str(ielement_id)
		response = self._core.io.query_str(f'DIAGnostic:FOOTprint:ELEMent:CONNection:TARGet:IDS? {param}')
		return trim_str_response(response)
