from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpathCls:
	"""Spath commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	def set(self, name_signal_path: str, name_antenna: str, name_connector: str, overwrite: bool = None) -> None:
		"""SCPI: CREate:TENVironment:SPATh \n
		Snippet: driver.create.tenvironment.spath.set(name_signal_path = 'abc', name_antenna = 'abc', name_connector = 'abc', overwrite = False) \n
		Creates a connection for a selected connector and assigns a name to the connection. Assign a unique name to each named
		object within the test environment. Assigning an already used name can be rejected with an error message, even if the
		other object has not the same type as the new object. \n
			:param name_signal_path: Name of the connection. Freely configurable and used in other commands to address the connection. If a connection with this name already exists, the behavior depends on Overwrite.
			:param name_antenna: Name of the DUT antenna connector.
			:param name_connector: Name of the instrument connector. Examples: '0.Slot1.Port1.RRH.RF1', '0.Slot1.Port1.RRH.RF2', '0.Slot1.Port2.IFIn', '0.Slot1.Port2.IFOut'
			:param overwrite: Selects the behavior if a connection with the NameSignalPath already exists. OFF | 0: No overwrite, return an error. ON | 1: Overwrite the existing connection.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_signal_path', name_signal_path, DataType.String), ArgSingle('name_antenna', name_antenna, DataType.String), ArgSingle('name_connector', name_connector, DataType.String), ArgSingle('overwrite', overwrite, DataType.Boolean, None, is_optional=True))
		self._core.io.write(f'CREate:TENVironment:SPATh {param}'.rstrip())
