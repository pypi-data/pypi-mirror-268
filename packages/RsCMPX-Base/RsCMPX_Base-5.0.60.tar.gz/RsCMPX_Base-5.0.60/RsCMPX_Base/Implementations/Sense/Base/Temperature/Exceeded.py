from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExceededCls:
	"""Exceeded commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("exceeded", core, parent)

	# noinspection PyTypeChecker
	class ListPyStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Meas_Point: List[str]: No parameter help available
			- Current_Temp: List[float]: No parameter help available
			- Max_Temp: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Meas_Point', DataType.StringList, None, False, True, 1),
			ArgStruct('Current_Temp', DataType.FloatList, None, False, True, 1),
			ArgStruct('Max_Temp', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Meas_Point: List[str] = None
			self.Current_Temp: List[float] = None
			self.Max_Temp: List[float] = None

	def get_list_py(self) -> ListPyStruct:
		"""SCPI: SENSe:BASE:TEMPerature:EXCeeded:LIST \n
		Snippet: value: ListPyStruct = driver.sense.base.temperature.exceeded.get_list_py() \n
		No command help available \n
			:return: structure: for return value, see the help for ListPyStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:BASE:TEMPerature:EXCeeded:LIST?', self.__class__.ListPyStruct())

	def get_value(self) -> bool:
		"""SCPI: SENSe:BASE:TEMPerature:EXCeeded \n
		Snippet: value: bool = driver.sense.base.temperature.exceeded.get_value() \n
		No command help available \n
			:return: exceed: No help available
		"""
		response = self._core.io.query_str('SENSe:BASE:TEMPerature:EXCeeded?')
		return Conversions.str_to_bool(response)
