from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NewCls:
	"""New commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("new", core, parent)

	def set(self, current_password: str, new_password: str) -> None:
		"""SCPI: SYSTem:PASSword:NEW \n
		Snippet: driver.system.password.new.set(current_password = 'abc', new_password = 'abc') \n
		No command help available \n
			:param current_password: No help available
			:param new_password: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('current_password', current_password, DataType.String), ArgSingle('new_password', new_password, DataType.String))
		self._core.io.write(f'SYSTem:PASSword:NEW {param}'.rstrip())
