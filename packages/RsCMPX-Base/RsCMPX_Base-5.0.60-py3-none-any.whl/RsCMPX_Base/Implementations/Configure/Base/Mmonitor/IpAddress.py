from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddressCls:
	"""IpAddress commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: IpAddress, default value after init: IpAddress.Addr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipAddress", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_ipAddress_get', 'repcap_ipAddress_set', repcap.IpAddress.Addr1)

	def repcap_ipAddress_set(self, ipAddress: repcap.IpAddress) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IpAddress.Default
		Default value after init: IpAddress.Addr1"""
		self._cmd_group.set_repcap_enum_value(ipAddress)

	def repcap_ipAddress_get(self) -> repcap.IpAddress:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, first_segment: int, second_segment: int, system_id: int, local_id: int, ipAddress=repcap.IpAddress.Default) -> None:
		"""SCPI: CONFigure:BASE:MMONitor:IPADdress<n> \n
		Snippet: driver.configure.base.mmonitor.ipAddress.set(first_segment = 1, second_segment = 1, system_id = 1, local_id = 1, ipAddress = repcap.IpAddress.Default) \n
		No command help available \n
			:param first_segment: No help available
			:param second_segment: No help available
			:param system_id: No help available
			:param local_id: No help available
			:param ipAddress: optional repeated capability selector. Default value: Addr1 (settable in the interface 'IpAddress')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('first_segment', first_segment, DataType.Integer), ArgSingle('second_segment', second_segment, DataType.Integer), ArgSingle('system_id', system_id, DataType.Integer), ArgSingle('local_id', local_id, DataType.Integer))
		ipAddress_cmd_val = self._cmd_group.get_repcap_cmd_value(ipAddress, repcap.IpAddress)
		self._core.io.write(f'CONFigure:BASE:MMONitor:IPADdress{ipAddress_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class IpAddressStruct(StructBase):
		"""Response structure. Fields: \n
			- First_Segment: int: No parameter help available
			- Second_Segment: int: No parameter help available
			- System_Id: int: No parameter help available
			- Local_Id: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('First_Segment'),
			ArgStruct.scalar_int('Second_Segment'),
			ArgStruct.scalar_int('System_Id'),
			ArgStruct.scalar_int('Local_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.First_Segment: int = None
			self.Second_Segment: int = None
			self.System_Id: int = None
			self.Local_Id: int = None

	def get(self, ipAddress=repcap.IpAddress.Default) -> IpAddressStruct:
		"""SCPI: CONFigure:BASE:MMONitor:IPADdress<n> \n
		Snippet: value: IpAddressStruct = driver.configure.base.mmonitor.ipAddress.get(ipAddress = repcap.IpAddress.Default) \n
		No command help available \n
			:param ipAddress: optional repeated capability selector. Default value: Addr1 (settable in the interface 'IpAddress')
			:return: structure: for return value, see the help for IpAddressStruct structure arguments."""
		ipAddress_cmd_val = self._cmd_group.get_repcap_cmd_value(ipAddress, repcap.IpAddress)
		return self._core.io.query_struct(f'CONFigure:BASE:MMONitor:IPADdress{ipAddress_cmd_val}?', self.__class__.IpAddressStruct())

	def clone(self) -> 'IpAddressCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpAddressCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
