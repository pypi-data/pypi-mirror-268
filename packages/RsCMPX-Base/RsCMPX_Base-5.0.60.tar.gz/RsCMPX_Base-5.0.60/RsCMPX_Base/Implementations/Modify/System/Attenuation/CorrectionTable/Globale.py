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

	def set(self, name: str, frequency: List[float], attenuation: List[float]) -> None:
		"""SCPI: MODify:SYSTem:ATTenuation:CTABle:GLOBal \n
		Snippet: driver.modify.system.attenuation.correctionTable.globale.set(name = 'abc', frequency = [1.1, 2.2, 3.3], attenuation = [1.1, 2.2, 3.3]) \n
		Modifies existing entries of a global correction table. Specify at least one parameter pair <Frequency>, <Attenuation>.
		Entries with the specified frequencies must already exist. The attenuation values of these entries are overwritten. \n
			:param name: Name of the correction table
			:param frequency: No help available
			:param attenuation: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle.as_open_list('frequency', frequency, DataType.FloatList, None), ArgSingle.as_open_list('attenuation', attenuation, DataType.FloatList, None))
		self._core.io.write(f'MODify:SYSTem:ATTenuation:CTABle:GLOBal {param}'.rstrip())
