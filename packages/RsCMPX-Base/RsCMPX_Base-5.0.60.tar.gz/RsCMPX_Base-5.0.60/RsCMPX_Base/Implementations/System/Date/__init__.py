from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DateCls:
	"""Date commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	@property
	def local(self):
		"""local commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_local'):
			from .Local import LocalCls
			self._local = LocalCls(self._core, self._cmd_group)
		return self._local

	@property
	def utc(self):
		"""utc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_utc'):
			from .Utc import UtcCls
			self._utc = UtcCls(self._core, self._cmd_group)
		return self._utc

	def set(self, year: int, month: int, day: int) -> None:
		"""SCPI: SYSTem:DATE \n
		Snippet: driver.system.date.set(year = 1, month = 1, day = 1) \n
		No command help available \n
			:param year: No help available
			:param month: No help available
			:param day: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('year', year, DataType.Integer), ArgSingle('month', month, DataType.Integer), ArgSingle('day', day, DataType.Integer))
		self._core.io.write(f'SYSTem:DATE {param}'.rstrip())

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Response structure. Fields: \n
			- Year: int: No parameter help available
			- Month: int: No parameter help available
			- Day: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Year'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Day')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: int = None
			self.Month: int = None
			self.Day: int = None

	def get(self) -> DateStruct:
		"""SCPI: SYSTem:DATE \n
		Snippet: value: DateStruct = driver.system.date.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DateStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:DATE?', self.__class__.DateStruct())

	def clone(self) -> 'DateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
