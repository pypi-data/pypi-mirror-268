from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GroupCls:
	"""Group commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("group", core, parent)

	def set(self, connector_name: str, signal_path: str) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SPATh:GROup \n
		Snippet: driver.route.gprf.generator.spath.group.set(connector_name = 'abc', signal_path = 'abc') \n
		No command help available \n
			:param connector_name: No help available
			:param signal_path: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector_name', connector_name, DataType.String), ArgSingle('signal_path', signal_path, DataType.String))
		self._core.io.write(f'ROUTe:GPRF:GENerator<Instance>:SPATh:GROup {param}'.rstrip())

	def get(self, connector_name: str) -> str:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SPATh:GROup \n
		Snippet: value: str = driver.route.gprf.generator.spath.group.get(connector_name = 'abc') \n
		No command help available \n
			:param connector_name: No help available
			:return: signal_path: No help available"""
		param = Conversions.value_to_quoted_str(connector_name)
		response = self._core.io.query_str(f'ROUTe:GPRF:GENerator<Instance>:SPATh:GROup? {param}')
		return trim_str_response(response)
