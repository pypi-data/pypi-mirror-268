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

	def set(self, name: str, intervall_start: float, intervall_end: float = None) -> None:
		"""SCPI: REMove:SYSTem:ATTenuation:CTABle[:TENVironment] \n
		Snippet: driver.remove.system.attenuation.correctionTable.tenvironment.set(name = 'abc', intervall_start = 1.0, intervall_end = 1.0) \n
		Removes entries from an existing channel-specific correction table. To remove a single entry, enter the frequency of the
		entry as <IntervallStart> and omit <IntervallEnd>. To remove all entries in a certain frequency range, enter the lower
		frequency as <IntervallStart> and the upper frequency as <IntervallEnd>. \n
			:param name: Name of the existing correction table.
			:param intervall_start: No help available
			:param intervall_end: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('intervall_start', intervall_start, DataType.Float), ArgSingle('intervall_end', intervall_end, DataType.Float, None, is_optional=True))
		self._core.io.write(f'REMove:SYSTem:ATTenuation:CTABle:TENVironment {param}'.rstrip())
