from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Sname: str: No parameter help available
			- Efunctionality: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Sname'),
			ArgStruct.scalar_int('Efunctionality')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sname: str = None
			self.Efunctionality: int = None

	def get(self, iuse_case_id: int) -> GetStruct:
		"""SCPI: DIAGnostic:FOOTprint:USECase:DATA \n
		Snippet: value: GetStruct = driver.diagnostic.footPrint.useCase.data.get(iuse_case_id = 1) \n
		No command help available \n
			:param iuse_case_id: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(iuse_case_id)
		return self._core.io.query_struct(f'DIAGnostic:FOOTprint:USECase:DATA? {param}', self.__class__.GetStruct())
