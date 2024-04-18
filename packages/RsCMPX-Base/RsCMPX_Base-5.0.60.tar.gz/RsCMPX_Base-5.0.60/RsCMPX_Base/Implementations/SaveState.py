from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SaveStateCls:
	"""SaveState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("saveState", core, parent)

	def set(self, num: float) -> None:
		"""SCPI: *SAV \n
		Snippet: driver.saveState.set(num = 1.0) \n
		Stores the current instrument settings under the specified number in an intermediate memory. The settings can be restored,
		using the command *RCL with the associated number. To save the stored instrument settings to a file, see method
		RsCMPX_Base.MassMemory.Store.State.set. See also method RsCMPX_Base.MassMemory.save. \n
			:param num: No help available
		"""
		param = Conversions.decimal_value_to_str(num)
		self._core.io.write(f'*SAV {param}')
