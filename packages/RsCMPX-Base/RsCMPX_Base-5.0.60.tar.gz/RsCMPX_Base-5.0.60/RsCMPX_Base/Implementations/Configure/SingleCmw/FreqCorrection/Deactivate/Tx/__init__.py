from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxCls:
	"""Tx commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def set_value(self, connector_bench: str) -> None:
		"""SCPI: CONFigure:CMWS:FDCorrection:DEACtivate:TX \n
		Snippet: driver.configure.singleCmw.freqCorrection.deactivate.tx.set_value(connector_bench = rawAbc) \n
		No command help available \n
			:param connector_bench: No help available
		"""
		param = Conversions.value_to_str(connector_bench)
		self._core.io.write(f'CONFigure:CMWS:FDCorrection:DEACtivate:TX {param}')

	def clone(self) -> 'TxCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TxCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
