from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TenvironmentCls:
	"""Tenvironment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tenvironment", core, parent)

	def set(self, name: str, frequency: List[float] = None, attenuation: List[float] = None) -> None:
		"""SCPI: CREate:SYSTem:ATTenuation:CTABle[:TENVironment] \n
		Snippet: driver.create.system.attenuation.correctionTable.tenvironment.set(name = 'abc', frequency = [1.1, 2.2, 3.3], attenuation = [1.1, 2.2, 3.3]) \n
		Creates a channel-specific correction table. You can specify one or more parameter pairs <Frequency>, <Attenuation> to
		add entries to the table. \n
			:param name: Name of the table. Freely configurable and used in other commands to address the table. If a table with the given name exists already for the addressed smart channel, this table is overwritten.
			:param frequency: No help available
			:param attenuation: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('frequency', frequency, DataType.FloatList, None, True, True, 1), ArgSingle('attenuation', attenuation, DataType.FloatList, None, True, True, 1))
		self._core.io.write(f'CREate:SYSTem:ATTenuation:CTABle:TENVironment {param}'.rstrip())
