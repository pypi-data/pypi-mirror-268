from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectorsCls:
	"""Connectors commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connectors", core, parent)

	def get(self, name_style: enums.NameStyle = None) -> List[str]:
		"""SCPI: DIAGnostic:CATalog:SYSTem:CONNectors \n
		Snippet: value: List[str] = driver.diagnostic.catalog.system.connectors.get(name_style = enums.NameStyle.FQName) \n
		No command help available \n
			:param name_style: No help available
			:return: name_connector: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_style', name_style, DataType.Enum, enums.NameStyle, is_optional=True))
		response = self._core.io.query_str(f'DIAGnostic:CATalog:SYSTem:CONNectors? {param}'.rstrip())
		return Conversions.str_to_str_list(response)
