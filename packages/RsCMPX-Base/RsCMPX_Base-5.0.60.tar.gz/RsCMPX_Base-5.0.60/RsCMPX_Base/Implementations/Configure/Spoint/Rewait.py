from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RewaitCls:
	"""Rewait commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rewait", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Count: int: No parameter help available
			- Result: enums.SyncResult: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Count'),
			ArgStruct.scalar_enum('Result', enums.SyncResult)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Count: int = None
			self.Result: enums.SyncResult = None

	def get(self, name: str) -> GetStruct:
		"""SCPI: CONFigure:SPOint:REWait \n
		Snippet: value: GetStruct = driver.configure.spoint.rewait.get(name = 'abc') \n
		No command help available \n
			:param name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(name)
		return self._core.io.query_struct(f'CONFigure:SPOint:REWait? {param}', self.__class__.GetStruct())
