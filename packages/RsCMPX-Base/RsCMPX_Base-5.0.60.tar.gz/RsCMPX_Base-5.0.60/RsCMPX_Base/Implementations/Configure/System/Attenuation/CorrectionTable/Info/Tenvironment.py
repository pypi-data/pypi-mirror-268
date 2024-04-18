from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TenvironmentCls:
	"""Tenvironment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tenvironment", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency: List[float]: No parameter help available
			- Attenuation: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Attenuation', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: List[float] = None
			self.Attenuation: List[float] = None

	def get(self, name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SYSTem:ATTenuation:CTABle:INFO[:TENVironment] \n
		Snippet: value: GetStruct = driver.configure.system.attenuation.correctionTable.info.tenvironment.get(name = 'abc') \n
		Returns the entries of a channel-specific correction table as pairs of values: {<Frequency>, <Attenuation>}1,
		{<Frequency>, <Attenuation>}2, ... \n
			:param name: Name of the correction table.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(name)
		return self._core.io.query_struct(f'CONFigure:SYSTem:ATTenuation:CTABle:INFO:TENVironment? {param}', self.__class__.GetStruct())
