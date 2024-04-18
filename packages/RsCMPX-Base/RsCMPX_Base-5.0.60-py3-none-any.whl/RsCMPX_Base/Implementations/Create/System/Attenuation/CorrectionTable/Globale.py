from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GlobaleCls:
	"""Globale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("globale", core, parent)

	def set(self, name: str, arg_1: List[float] = None, attenuation: List[float] = None) -> None:
		"""SCPI: CREate:SYSTem:ATTenuation:CTABle:GLOBal \n
		Snippet: driver.create.system.attenuation.correctionTable.globale.set(name = 'abc', arg_1 = [1.1, 2.2, 3.3], attenuation = [1.1, 2.2, 3.3]) \n
		Creates a global correction table. You can specify one or more parameter pairs <Frequency>, <Attenuation> to add entries
		to the table. \n
			:param name: Name of the table. Freely configurable and used in other commands to address the table. If a global table with the given name exists already, this table is overwritten.
			:param arg_1: No help available
			:param attenuation: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('arg_1', arg_1, DataType.FloatList, None, True, True, 1), ArgSingle('attenuation', attenuation, DataType.FloatList, None, True, True, 1))
		self._core.io.write(f'CREate:SYSTem:ATTenuation:CTABle:GLOBal {param}'.rstrip())
