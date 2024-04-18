from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsageCls:
	"""Usage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usage", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Correction_Table_Rx: str: No parameter help available
			- Correction_Table_Tx: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Correction_Table_Rx'),
			ArgStruct.scalar_str('Correction_Table_Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Correction_Table_Rx: str = None
			self.Correction_Table_Tx: str = None

	def get(self, connector: str) -> GetStruct:
		"""SCPI: CONFigure:CMWS:FDCorrection:USAGe \n
		Snippet: value: GetStruct = driver.configure.singleCmw.freqCorrection.usage.get(connector = rawAbc) \n
		No command help available \n
			:param connector: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_str(connector)
		return self._core.io.query_struct(f'CONFigure:CMWS:FDCorrection:USAGe? {param}', self.__class__.GetStruct())
