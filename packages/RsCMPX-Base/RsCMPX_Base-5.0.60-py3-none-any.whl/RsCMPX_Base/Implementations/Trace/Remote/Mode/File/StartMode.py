from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StartModeCls:
	"""StartMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("startMode", core, parent)

	def set(self, estart_mode: enums.RemoteTraceStartMode, fileNr=repcap.FileNr.Default) -> None:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:STARtmode \n
		Snippet: driver.trace.remote.mode.file.startMode.set(estart_mode = enums.RemoteTraceStartMode.AUTO, fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param estart_mode: No help available
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
		"""
		param = Conversions.enum_scalar_to_str(estart_mode, enums.RemoteTraceStartMode)
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		self._core.io.write(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:STARtmode {param}')

	# noinspection PyTypeChecker
	def get(self, fileNr=repcap.FileNr.Default) -> enums.RemoteTraceStartMode:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:STARtmode \n
		Snippet: value: enums.RemoteTraceStartMode = driver.trace.remote.mode.file.startMode.get(fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
			:return: estart_mode: No help available"""
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		response = self._core.io.query_str(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:STARtmode?')
		return Conversions.str_to_scalar_enum(response, enums.RemoteTraceStartMode)
