from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TranslationCls:
	"""Translation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("translation", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Virtual_Connector: str: No parameter help available
			- Absolute_Connector: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Virtual_Connector'),
			ArgStruct.scalar_raw_str('Absolute_Connector')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Virtual_Connector: str = None
			self.Absolute_Connector: str = None

	def get(self, connector: str) -> GetStruct:
		"""SCPI: SYSTem:CONNector:TRANslation \n
		Snippet: value: GetStruct = driver.system.connector.translation.get(connector = rawAbc) \n
		No command help available \n
			:param connector: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_str(connector)
		return self._core.io.query_struct(f'SYSTem:CONNector:TRANslation? {param}', self.__class__.GetStruct())
