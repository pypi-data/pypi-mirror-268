from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QueueCls:
	"""Queue commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("queue", core, parent)

	# noinspection PyTypeChecker
	class NextStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Error_Code: int: No parameter help available
			- Error_Description: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Error_Code'),
			ArgStruct.scalar_str('Error_Description')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Error_Code: int = None
			self.Error_Description: str = None

	def get_next(self) -> NextStruct:
		"""SCPI: STATus:QUEue[:NEXT] \n
		Snippet: value: NextStruct = driver.status.queue.get_next() \n
		No command help available \n
			:return: structure: for return value, see the help for NextStruct structure arguments.
		"""
		return self._core.io.query_struct('STATus:QUEue:NEXT?', self.__class__.NextStruct())
