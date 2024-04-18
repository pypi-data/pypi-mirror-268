from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ActivateCls:
	"""Activate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("activate", core, parent)

	def set(self, connector: str, table: str, direction: enums.RxTxDirection = None, rf_converter: enums.RfConverterInPath = None) -> None:
		"""SCPI: CONFigure:FDCorrection:ACTivate \n
		Snippet: driver.configure.freqCorrection.activate.set(connector = rawAbc, table = 'abc', direction = enums.RxTxDirection.RX, rf_converter = enums.RfConverterInPath.RF1) \n
		No command help available \n
			:param connector: No help available
			:param table: No help available
			:param direction: No help available
			:param rf_converter: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.RawString), ArgSingle('table', table, DataType.String), ArgSingle('direction', direction, DataType.Enum, enums.RxTxDirection, is_optional=True), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.RfConverterInPath, is_optional=True))
		self._core.io.write(f'CONFigure:FDCorrection:ACTivate {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Table_Rx: str: No parameter help available
			- Table_Tx: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Table_Rx'),
			ArgStruct.scalar_str('Table_Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Table_Rx: str = None
			self.Table_Tx: str = None

	def get(self, connector: str) -> GetStruct:
		"""SCPI: CONFigure:FDCorrection:ACTivate \n
		Snippet: value: GetStruct = driver.configure.freqCorrection.activate.get(connector = rawAbc) \n
		No command help available \n
			:param connector: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_str(connector)
		return self._core.io.query_struct(f'CONFigure:FDCorrection:ACTivate? {param}', self.__class__.GetStruct())
