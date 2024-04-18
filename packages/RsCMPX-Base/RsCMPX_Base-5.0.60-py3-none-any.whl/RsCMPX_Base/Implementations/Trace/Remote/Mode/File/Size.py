from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SizeCls:
	"""Size commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("size", core, parent)

	def set(self, ifile_size: int, fileNr=repcap.FileNr.Default) -> None:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:SIZE \n
		Snippet: driver.trace.remote.mode.file.size.set(ifile_size = 1, fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param ifile_size: No help available
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
		"""
		param = Conversions.decimal_value_to_str(ifile_size)
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		self._core.io.write(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:SIZE {param}')

	def get(self, fileNr=repcap.FileNr.Default) -> int:
		"""SCPI: TRACe:REMote:MODE:FILE<instrument>:SIZE \n
		Snippet: value: int = driver.trace.remote.mode.file.size.get(fileNr = repcap.FileNr.Default) \n
		No command help available \n
			:param fileNr: optional repeated capability selector. Default value: Nr1 (settable in the interface 'File')
			:return: ifile_size: No help available"""
		fileNr_cmd_val = self._cmd_group.get_repcap_cmd_value(fileNr, repcap.FileNr)
		response = self._core.io.query_str(f'TRACe:REMote:MODE:FILE{fileNr_cmd_val}:SIZE?')
		return Conversions.str_to_int(response)
