from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxCls:
	"""Tx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

	def set(self, name_signal_path: str, correction_table: List[str]) -> None:
		"""SCPI: [CONFigure]:TENVironment:SPATh:CTABle:TX \n
		Snippet: driver.configure.tenvironment.spath.correctionTable.tx.set(name_signal_path = 'abc', correction_table = ['abc1', 'abc2', 'abc3']) \n
		Assigns one or more correction tables to the TX direction or RX direction of a connection. If there is an existing
		assignment, it is overwritten. The directions refer to the instrument (TX/RX of the instrument) . \n
			:param name_signal_path: Name of the connection
			:param correction_table: The name of the correction table to be assigned. At least one name of a correction table. To assign several tables, use a comma-separated list of strings.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_signal_path', name_signal_path, DataType.String), ArgSingle.as_open_list('correction_table', correction_table, DataType.StringList, None))
		self._core.io.write(f'CONFigure:TENVironment:SPATh:CTABle:TX {param}'.rstrip())

	def get(self, name_signal_path: str) -> List[str]:
		"""SCPI: [CONFigure]:TENVironment:SPATh:CTABle:TX \n
		Snippet: value: List[str] = driver.configure.tenvironment.spath.correctionTable.tx.get(name_signal_path = 'abc') \n
		Assigns one or more correction tables to the TX direction or RX direction of a connection. If there is an existing
		assignment, it is overwritten. The directions refer to the instrument (TX/RX of the instrument) . \n
			:param name_signal_path: Name of the connection
			:return: correction_table: The name of the correction table to be assigned. At least one name of a correction table. To assign several tables, use a comma-separated list of strings."""
		param = Conversions.value_to_quoted_str(name_signal_path)
		response = self._core.io.query_str(f'CONFigure:TENVironment:SPATh:CTABle:TX? {param}')
		return Conversions.str_to_str_list(response)
