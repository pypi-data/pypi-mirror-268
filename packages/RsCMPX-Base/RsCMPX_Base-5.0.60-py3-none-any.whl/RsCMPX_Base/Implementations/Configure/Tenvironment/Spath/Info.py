from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InfoCls:
	"""Info commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Name_Antenna: str: Name of the DUT antenna connector.
			- Name_Connector: str: Name of the instrument connector.
			- Signal_Direction: enums.RxTxDirection: Signal direction, from the point of view of the instrument.
			- No_Corr_Table_Rx: float: Number of correction tables assigned to the RX direction of the connection.
			- Corr_Table_Rx: str: Comma-separated list of NoCorrTableRX strings. Each string indicates the name of a correction table assigned to the RX direction.
			- No_Corr_Table_Tx: float: Number of correction tables assigned to the TX direction of the connection.
			- Corr_Table_Tx: List[str]: Comma-separated list of NoCorrTableTX strings. Each string indicates the name of a correction table assigned to the TX direction."""
		__meta_args_list = [
			ArgStruct.scalar_str('Name_Antenna'),
			ArgStruct.scalar_str('Name_Connector'),
			ArgStruct.scalar_enum('Signal_Direction', enums.RxTxDirection),
			ArgStruct.scalar_float('No_Corr_Table_Rx'),
			ArgStruct.scalar_str('Corr_Table_Rx'),
			ArgStruct.scalar_float('No_Corr_Table_Tx'),
			ArgStruct('Corr_Table_Tx', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name_Antenna: str = None
			self.Name_Connector: str = None
			self.Signal_Direction: enums.RxTxDirection = None
			self.No_Corr_Table_Rx: float = None
			self.Corr_Table_Rx: str = None
			self.No_Corr_Table_Tx: float = None
			self.Corr_Table_Tx: List[str] = None

	def get(self, name_spath: str) -> GetStruct:
		"""SCPI: [CONFigure]:TENVironment:SPATh:INFO \n
		Snippet: value: GetStruct = driver.configure.tenvironment.spath.info.get(name_spath = 'abc') \n
		Returns information about the connection <NameSpath>. \n
			:param name_spath: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(name_spath)
		return self._core.io.query_struct(f'CONFigure:TENVironment:SPATh:INFO? {param}', self.__class__.GetStruct())
