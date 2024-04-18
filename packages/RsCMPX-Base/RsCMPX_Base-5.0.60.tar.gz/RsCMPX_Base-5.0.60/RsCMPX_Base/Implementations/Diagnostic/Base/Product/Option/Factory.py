from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FactoryCls:
	"""Factory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factory", core, parent)

	def clear(self, part_number: str, serial_number: str) -> None:
		"""SCPI: DIAGnostic:BASE:PRODuct:OPTion:FACTory:CLEar \n
		Snippet: driver.diagnostic.base.product.option.factory.clear(part_number = 'abc', serial_number = 'abc') \n
		No command help available \n
			:param part_number: No help available
			:param serial_number: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('part_number', part_number, DataType.String), ArgSingle('serial_number', serial_number, DataType.String))
		self._core.io.write(f'DIAGnostic:BASE:PRODuct:OPTion:FACTory:CLEar {param}'.rstrip())
