from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsageCls:
	"""Usage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usage", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Not_Avail_Rx: str: No parameter help available
			- Correction_Table_Rx: str: No parameter help available
			- Not_Avail_Tx: str: No parameter help available
			- Correction_Table_Tx: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Not_Avail_Rx'),
			ArgStruct.scalar_str('Correction_Table_Rx'),
			ArgStruct.scalar_str('Not_Avail_Tx'),
			ArgStruct.scalar_str('Correction_Table_Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Not_Avail_Rx: str = None
			self.Correction_Table_Rx: str = None
			self.Not_Avail_Tx: str = None
			self.Correction_Table_Tx: str = None

	def get(self, connector: str, rf_converter: enums.RfConverterInPath = None) -> GetStruct:
		"""SCPI: CONFigure:FDCorrection:USAGe \n
		Snippet: value: GetStruct = driver.configure.freqCorrection.usage.get(connector = rawAbc, rf_converter = enums.RfConverterInPath.RF1) \n
		No command help available \n
			:param connector: No help available
			:param rf_converter: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.RawString), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.RfConverterInPath, is_optional=True))
		return self._core.io.query_struct(f'CONFigure:FDCorrection:USAGe? {param}'.rstrip(), self.__class__.GetStruct())
