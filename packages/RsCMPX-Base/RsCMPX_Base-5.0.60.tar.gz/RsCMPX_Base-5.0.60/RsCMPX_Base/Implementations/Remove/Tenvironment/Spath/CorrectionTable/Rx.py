from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxCls:
	"""Rx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rx", core, parent)

	def set(self, name_signal_path: str, correction_table: List[str] = None) -> None:
		"""SCPI: REMove:TENVironment:SPATh:CTABle:RX \n
		Snippet: driver.remove.tenvironment.spath.correctionTable.rx.set(name_signal_path = 'abc', correction_table = ['abc1', 'abc2', 'abc3']) \n
		Removes assigned correction tables from the TX direction or RX direction of a connection. \n
			:param name_signal_path: Name of the connection
			:param correction_table: The name of the correction table to be removed. If you omit the parameter, all correction tables are removed. You can specify several table names as comma-separated list of strings.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_signal_path', name_signal_path, DataType.String), ArgSingle('correction_table', correction_table, DataType.StringList, None, True, True, 1))
		self._core.io.write(f'REMove:TENVironment:SPATh:CTABle:RX {param}'.rstrip())
