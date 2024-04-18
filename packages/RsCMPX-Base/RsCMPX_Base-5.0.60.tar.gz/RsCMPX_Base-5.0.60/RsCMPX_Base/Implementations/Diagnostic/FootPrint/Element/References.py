from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReferencesCls:
	"""References commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("references", core, parent)

	def get(self, ielement_id: float, sreference_type: str) -> List[int]:
		"""SCPI: DIAGnostic:FOOTprint:ELEMent:REFerences \n
		Snippet: value: List[int] = driver.diagnostic.footPrint.element.references.get(ielement_id = 1.0, sreference_type = 'abc') \n
		No command help available \n
			:param ielement_id: No help available
			:param sreference_type: No help available
			:return: ielement_ids: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ielement_id', ielement_id, DataType.Float), ArgSingle('sreference_type', sreference_type, DataType.String))
		response = self._core.io.query_bin_or_ascii_int_list(f'DIAGnostic:FOOTprint:ELEMent:REFerences? {param}'.rstrip())
		return response
