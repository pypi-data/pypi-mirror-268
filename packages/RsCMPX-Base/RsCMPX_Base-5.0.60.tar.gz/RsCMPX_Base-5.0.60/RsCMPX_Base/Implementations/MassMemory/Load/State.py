from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, sav_rcl_state_number: float, filename: str, msus: str = None) -> None:
		"""SCPI: MMEMory:LOAD:STATe \n
		Snippet: driver.massMemory.load.state.set(sav_rcl_state_number = 1.0, filename = 'abc', msus = 'abc') \n
		Loads the instrument settings from the specified file to the specified internal memory. After the file has been loaded,
		the settings must be activated using a *RCL command. For more convenience, see method RsCMPX_Base.MassMemory.recall. \n
			:param sav_rcl_state_number: No help available
			:param filename: No help available
			:param msus: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sav_rcl_state_number', sav_rcl_state_number, DataType.Float), ArgSingle('filename', filename, DataType.String), ArgSingle('msus', msus, DataType.String, None, is_optional=True))
		self._core.io.write(f'MMEMory:LOAD:STATe {param}'.rstrip())
