from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatusCls:
	"""Status commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	# noinspection PyTypeChecker
	class OpcStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Opc_Counter: int: No parameter help available
			- Opc_Active_Counter: int: No parameter help available
			- Opc_State: bool: No parameter help available
			- Opc_Command_State: bool: No parameter help available
			- Opc_Query_State: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Opc_Counter'),
			ArgStruct.scalar_int('Opc_Active_Counter'),
			ArgStruct.scalar_bool('Opc_State'),
			ArgStruct.scalar_bool('Opc_Command_State'),
			ArgStruct.scalar_bool('Opc_Query_State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Opc_Counter: int = None
			self.Opc_Active_Counter: int = None
			self.Opc_State: bool = None
			self.Opc_Command_State: bool = None
			self.Opc_Query_State: bool = None

	def get_opc(self) -> OpcStruct:
		"""SCPI: DIAGnostic:STATus:OPC \n
		Snippet: value: OpcStruct = driver.diagnostic.status.get_opc() \n
		No command help available \n
			:return: structure: for return value, see the help for OpcStruct structure arguments.
		"""
		return self._core.io.query_struct('DIAGnostic:STATus:OPC?', self.__class__.OpcStruct())
