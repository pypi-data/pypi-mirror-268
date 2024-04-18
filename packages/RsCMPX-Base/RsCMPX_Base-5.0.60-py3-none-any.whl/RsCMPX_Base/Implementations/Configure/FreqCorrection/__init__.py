from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqCorrectionCls:
	"""FreqCorrection commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("freqCorrection", core, parent)

	@property
	def activate(self):
		"""activate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_activate'):
			from .Activate import ActivateCls
			self._activate = ActivateCls(self._core, self._cmd_group)
		return self._activate

	@property
	def usage(self):
		"""usage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .Usage import UsageCls
			self._usage = UsageCls(self._core, self._cmd_group)
		return self._usage

	def deactivate(self, connector: str, direction: enums.RxTxDirection = None, rf_converter: enums.RfConverterInPath = None) -> None:
		"""SCPI: CONFigure:FDCorrection:DEACtivate \n
		Snippet: driver.configure.freqCorrection.deactivate(connector = rawAbc, direction = enums.RxTxDirection.RX, rf_converter = enums.RfConverterInPath.RF1) \n
		No command help available \n
			:param connector: No help available
			:param direction: No help available
			:param rf_converter: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.RawString), ArgSingle('direction', direction, DataType.Enum, enums.RxTxDirection, is_optional=True), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.RfConverterInPath, is_optional=True))
		self._core.io.write(f'CONFigure:FDCorrection:DEACtivate {param}'.rstrip())

	def deactivate_all(self, direction: enums.RxTxDirection = None, table_path: str = None) -> None:
		"""SCPI: CONFigure:FDCorrection:DEACtivate:ALL \n
		Snippet: driver.configure.freqCorrection.deactivate_all(direction = enums.RxTxDirection.RX, table_path = rawAbc) \n
		No command help available \n
			:param direction: No help available
			:param table_path: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('direction', direction, DataType.Enum, enums.RxTxDirection, is_optional=True), ArgSingle('table_path', table_path, DataType.RawString, None, is_optional=True))
		self._core.io.write(f'CONFigure:FDCorrection:DEACtivate:ALL {param}'.rstrip())

	def clone(self) -> 'FreqCorrectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FreqCorrectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
