from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ItemCls:
	"""Item commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	def set(self, item_name: str, filename: str) -> None:
		"""SCPI: MMEMory:STORe:ITEM \n
		Snippet: driver.massMemory.store.item.set(item_name = 'abc', filename = 'abc') \n
		Executes a partial save, i.e. stores a part of the instrument settings to the specified file. You can store all settings
		of a specific application instance. Or you can store the list mode settings of a specific measurement application
		instance. \n
			:param item_name: Part to be saved. ItemName = Application[i][:MEV:LIST] For Application, see method RsCMPX_Base.MassMemory.Load.Item.set. i is the instance of the application. Omitting i stores instance 1. Appending :MEV:LIST stores only the list mode settings.
			:param filename: Path and filename of the target file. Wildcards are not allowed.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item_name', item_name, DataType.String), ArgSingle('filename', filename, DataType.String))
		self._core.io.write(f'MMEMory:STORe:ITEM {param}'.rstrip())
