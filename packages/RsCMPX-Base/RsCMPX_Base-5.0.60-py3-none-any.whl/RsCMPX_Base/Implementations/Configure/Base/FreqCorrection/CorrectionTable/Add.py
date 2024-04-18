from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AddCls:
	"""Add commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("add", core, parent)

	def set(self, table_name: str, frequency: List[float] = None, correction: List[float] = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:ADD \n
		Snippet: driver.configure.base.freqCorrection.correctionTable.add.set(table_name = 'abc', frequency = [1.1, 2.2, 3.3], correction = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param table_name: No help available
			:param frequency: No help available
			:param correction: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('table_name', table_name, DataType.String), ArgSingle('frequency', frequency, DataType.FloatList, None, True, True, 1), ArgSingle('correction', correction, DataType.FloatList, None, True, True, 1))
		self._core.io.write(f'CONFigure:BASE:FDCorrection:CTABle:ADD {param}'.rstrip())
