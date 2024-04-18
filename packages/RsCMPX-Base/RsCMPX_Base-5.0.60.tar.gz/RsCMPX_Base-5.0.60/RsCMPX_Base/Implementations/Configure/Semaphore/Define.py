from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DefineCls:
	"""Define commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("define", core, parent)

	def set(self, name: str, def_timeout: float, def_count: int, scope: enums.ValidityScopeA = None) -> None:
		"""SCPI: CONFigure:SEMaphore:DEFine \n
		Snippet: driver.configure.semaphore.define.set(name = 'abc', def_timeout = 1.0, def_count = 1, scope = enums.ValidityScopeA.GLOBal) \n
		No command help available \n
			:param name: No help available
			:param def_timeout: No help available
			:param def_count: No help available
			:param scope: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('def_timeout', def_timeout, DataType.Float), ArgSingle('def_count', def_count, DataType.Integer), ArgSingle('scope', scope, DataType.Enum, enums.ValidityScopeA, is_optional=True))
		self._core.io.write(f'CONFigure:SEMaphore:DEFine {param}'.rstrip())
