from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdentifyCls:
	"""Identify commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("identify", core, parent)

	def start(self, box_nr: enums.BoxNumber, blinking_time: int = None) -> None:
		"""SCPI: STARt:BASE:MCMW:IDENtify \n
		Snippet: driver.base.multiCmw.identify.start(box_nr = enums.BoxNumber.BOX1, blinking_time = 1) \n
		No command help available \n
			:param box_nr: No help available
			:param blinking_time: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('box_nr', box_nr, DataType.Enum, enums.BoxNumber), ArgSingle('blinking_time', blinking_time, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'STARt:BASE:MCMW:IDENtify {param}'.rstrip())
