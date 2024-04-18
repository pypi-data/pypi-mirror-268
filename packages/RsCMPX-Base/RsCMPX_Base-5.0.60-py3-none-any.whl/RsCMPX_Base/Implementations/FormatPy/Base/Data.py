from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data_type: enums.DataFormat, data_length: int = None) -> None:
		"""SCPI: FORMat:BASE[:DATA] \n
		Snippet: driver.formatPy.base.data.set(data_type = enums.DataFormat.ASCii, data_length = 1) \n
		Selects the format for numeric data transferred to and from the CMX500, for example query results. \n
			:param data_type:
				- ASCii: Numeric data is transferred as ASCII bytes. Floating point numbers are transferred in scientific E notation.
				- REAL: Numeric data is transferred in a definite length block as IEEE floating point numbers (block data) .
				- BINary | HEXadecimal | OCTal: Numeric data is transferred in binary, hexadecimal or octal format.
			:param data_length: The meaning depends on the DataType as listed below. A zero returned by a query means that the
			default value is used.
				- For ASCii: Decimal places of floating point numbers. That means, number of 'b' digits in the scientific notation a.bbbbbbE+ccc.Default: six decimal places
				- For REAL: Length of floating point numbers in bits:32 bits = 4 bytes, format #14...64 bits = 8 bytes, format #18...Default: 64 bits
				- For BINary, HEXadecimal, OCTal: Minimum number of digits. If the number is longer, more digits are used. If it is shorter, leading zeros are added.Default: 0, no leading zeros"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('data_type', data_type, DataType.Enum, enums.DataFormat), ArgSingle('data_length', data_length, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'FORMat:BASE:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Data_Type: enums.DataFormat:
				- ASCii: Numeric data is transferred as ASCII bytes. Floating point numbers are transferred in scientific E notation.
				- REAL: Numeric data is transferred in a definite length block as IEEE floating point numbers (block data) .
				- BINary | HEXadecimal | OCTal: Numeric data is transferred in binary, hexadecimal or octal format.
			- Data_Length: int: The meaning depends on the DataType as listed below. A zero returned by a query means that the
			default value is used.
				- For ASCii: Decimal places of floating point numbers. That means, number of 'b' digits in the scientific notation a.bbbbbbE+ccc.Default: six decimal places
				- For REAL: Length of floating point numbers in bits:32 bits = 4 bytes, format #14...64 bits = 8 bytes, format #18...Default: 64 bits
				- For BINary, HEXadecimal, OCTal: Minimum number of digits. If the number is longer, more digits are used. If it is shorter, leading zeros are added.Default: 0, no leading zeros"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Data_Type', enums.DataFormat),
			ArgStruct.scalar_int('Data_Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Data_Type: enums.DataFormat = None
			self.Data_Length: int = None

	def get(self) -> DataStruct:
		"""SCPI: FORMat:BASE[:DATA] \n
		Snippet: value: DataStruct = driver.formatPy.base.data.get() \n
		Selects the format for numeric data transferred to and from the CMX500, for example query results. \n
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		return self._core.io.query_struct(f'FORMat:BASE:DATA?', self.__class__.DataStruct())
