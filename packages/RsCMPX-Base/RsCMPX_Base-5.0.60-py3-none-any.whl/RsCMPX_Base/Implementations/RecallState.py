from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RecallStateCls:
	"""RecallState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("recallState", core, parent)

	def set(self, num: float) -> None:
		"""SCPI: *RCL \n
		Snippet: driver.recallState.set(num = 1.0) \n
		Loads the instrument settings from an intermediate memory identified by the specified number. The instrument settings can
		be stored to this memory using the command *SAV with the associated number. To load instrument settings from a file to
		the memory, see method RsCMPX_Base.MassMemory.Load.State.set. See also method RsCMPX_Base.MassMemory.recall. \n
			:param num: No help available
		"""
		param = Conversions.decimal_value_to_str(num)
		self._core.io.write(f'*RCL {param}')
