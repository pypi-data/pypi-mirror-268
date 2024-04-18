from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, state: bool, filter_py: str = None) -> None:
		"""SCPI: CONFigure:SELFtest:SELect \n
		Snippet: driver.configure.selftest.select.set(state = False, filter_py = 'abc') \n
		No command help available \n
			:param state: No help available
			:param filter_py: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('filter_py', filter_py, DataType.String, None, is_optional=True))
		self._core.io.write(f'CONFigure:SELFtest:SELect {param}'.rstrip())
