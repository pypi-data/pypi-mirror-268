from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LatestCls:
	"""Latest commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("latest", core, parent)

	@property
	def specific(self):
		"""specific commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_specific'):
			from .Specific import SpecificCls
			self._specific = SpecificCls(self._core, self._cmd_group)
		return self._specific

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Date: str: No parameter help available
			- Time: str: No parameter help available
			- Type_Py: enums.Type: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Date'),
			ArgStruct.scalar_str('Time'),
			ArgStruct.scalar_enum('Type_Py', enums.Type)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Date: str = None
			self.Time: str = None
			self.Type_Py: enums.Type = None

	def get(self, type_py: enums.Type = None) -> GetStruct:
		"""SCPI: CALibration:BASE:LATest \n
		Snippet: value: GetStruct = driver.calibration.base.latest.get(type_py = enums.Type.CALibration) \n
		No command help available \n
			:param type_py: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('type_py', type_py, DataType.Enum, enums.Type, is_optional=True))
		return self._core.io.query_struct(f'CALibration:BASE:LATest? {param}'.rstrip(), self.__class__.GetStruct())

	def clone(self) -> 'LatestCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LatestCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
