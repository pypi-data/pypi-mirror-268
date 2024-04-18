from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:CMWS:FDCorrection:DEACtivate:RX:ALL \n
		Snippet: driver.configure.singleCmw.freqCorrection.deactivate.rx.all.set(table_path = rawAbc) \n
		No command help available \n
			:param table_path: No help available
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_str(table_path)
		self._core.io.write(f'CONFigure:CMWS:FDCorrection:DEACtivate:RX:ALL {param}'.strip())
