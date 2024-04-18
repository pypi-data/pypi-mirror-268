from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StopModeCls:
	"""StopMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stopMode", core, parent)

	def set(self, estop_mode: enums.RemoteTraceStopMode, fileNr=repcap.FileNr.Default) -> None:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:STOPmode \n
		Snippet: driver.trace.remote.mode.file.stopMode.set(estop_mode = enums.RemoteTraceStopMode.AUTO, fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param estop_mode: No help available
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
		"""
		param = Conversions.enum_scalar_to_str(estop_mode, enums.RemoteTraceStopMode)
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		self._core.io.write(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:STOPmode {param}')

	# noinspection PyTypeChecker
	def get(self, fileNr=repcap.FileNr.Default) -> enums.RemoteTraceStopMode:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:STOPmode \n
		Snippet: value: enums.RemoteTraceStopMode = driver.trace.remote.mode.file.stopMode.get(fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
			:return: estop_mode: No help available"""
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		response = self._core.io.query_str(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:STOPmode?')
		return Conversions.str_to_scalar_enum(response, enums.RemoteTraceStopMode)
