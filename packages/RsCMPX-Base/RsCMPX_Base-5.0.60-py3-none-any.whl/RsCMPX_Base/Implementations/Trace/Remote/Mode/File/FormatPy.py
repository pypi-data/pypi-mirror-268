from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPyCls:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, eformat: enums.RemoteTraceFileFormat, fileNr=repcap.FileNr.Default) -> None:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:FORMat \n
		Snippet: driver.trace.remote.mode.file.formatPy.set(eformat = enums.RemoteTraceFileFormat.ASCii, fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param eformat: No help available
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
		"""
		param = Conversions.enum_scalar_to_str(eformat, enums.RemoteTraceFileFormat)
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		self._core.io.write(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, fileNr=repcap.FileNr.Default) -> enums.RemoteTraceFileFormat:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:FORMat \n
		Snippet: value: enums.RemoteTraceFileFormat = driver.trace.remote.mode.file.formatPy.get(fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
			:return: eformat: No help available"""
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		response = self._core.io.query_str(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.RemoteTraceFileFormat)
