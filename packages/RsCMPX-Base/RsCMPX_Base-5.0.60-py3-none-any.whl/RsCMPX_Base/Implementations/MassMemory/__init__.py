from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MassMemoryCls:
	"""MassMemory commands group definition. 22 total commands, 6 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("massMemory", core, parent)

	@property
	def load(self):
		"""load commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_load'):
			from .Load import LoadCls
			self._load = LoadCls(self._core, self._cmd_group)
		return self._load

	@property
	def store(self):
		"""store commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_store'):
			from .Store import StoreCls
			self._store = StoreCls(self._core, self._cmd_group)
		return self._store

	@property
	def attribute(self):
		"""attribute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attribute'):
			from .Attribute import AttributeCls
			self._attribute = AttributeCls(self._core, self._cmd_group)
		return self._attribute

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def currentDirectory(self):
		"""currentDirectory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_currentDirectory'):
			from .CurrentDirectory import CurrentDirectoryCls
			self._currentDirectory = CurrentDirectoryCls(self._core, self._cmd_group)
		return self._currentDirectory

	@property
	def dcatalog(self):
		"""dcatalog commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcatalog'):
			from .Dcatalog import DcatalogCls
			self._dcatalog = DcatalogCls(self._core, self._cmd_group)
		return self._dcatalog

	def copy(self, file_source: str, file_destination: str = None) -> None:
		"""SCPI: MMEMory:COPY \n
		Snippet: driver.massMemory.copy(file_source = 'abc', file_destination = 'abc') \n
		Copies an existing file. The target directory must exist. \n
			:param file_source: Name of the file to be copied. Wildcards ? and * are allowed if FileDestination contains a path without a filename.
			:param file_destination: Path and/or name of the new file If no file destination is specified, the source file is written to the current directory (see method RsCMPX_Base.MassMemory.CurrentDirectory.set) . Wildcards are not allowed.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('file_source', file_source, DataType.String), ArgSingle('file_destination', file_destination, DataType.String, None, is_optional=True))
		self._core.io.write(f'MMEMory:COPY {param}'.rstrip())

	def delete(self, filename: str) -> None:
		"""SCPI: MMEMory:DELete \n
		Snippet: driver.massMemory.delete(filename = 'abc') \n
		Deletes the specified files. \n
			:param filename: File to be deleted. The wildcards * and ? are allowed. Specifying a directory instead of a file is not allowed.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'MMEMory:DELete {param}')

	def get_drives(self) -> List[str]:
		"""SCPI: MMEMory:DRIVes \n
		Snippet: value: List[str] = driver.massMemory.get_drives() \n
		No command help available \n
			:return: drive: No help available
		"""
		response = self._core.io.query_str('MMEMory:DRIVes?')
		return Conversions.str_to_str_list(response)

	def make_directory(self, directory_name: str) -> None:
		"""SCPI: MMEMory:MDIRectory \n
		Snippet: driver.massMemory.make_directory(directory_name = 'abc') \n
		Creates a directory. If necessary, an entire path consisting of several subdirectories is created. \n
			:param directory_name: Wildcards are not allowed.
		"""
		param = Conversions.value_to_quoted_str(directory_name)
		self._core.io.write(f'MMEMory:MDIRectory {param}')

	def move(self, file_source: str, file_destination: str) -> None:
		"""SCPI: MMEMory:MOVE \n
		Snippet: driver.massMemory.move(file_source = 'abc', file_destination = 'abc') \n
		Moves or renames an existing object (file or directory) to a new location. \n
			:param file_source: Name of the object to be moved or renamed. Wildcards ? and * are only allowed for moving files without renaming.
			:param file_destination: New name and/or path of the object. Wildcards are not allowed. If a new object name without a path is specified, the object is renamed. If a new path without an object name is specified, the object is moved to this path. If a new path and a new object name are specified, the object is moved to this path and renamed.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('file_source', file_source, DataType.String), ArgSingle('file_destination', file_destination, DataType.String))
		self._core.io.write(f'MMEMory:MOVE {param}'.rstrip())

	def get_msis(self) -> str:
		"""SCPI: MMEMory:MSIS \n
		Snippet: value: str = driver.massMemory.get_msis() \n
		No command help available \n
			:return: msus: No help available
		"""
		response = self._core.io.query_str('MMEMory:MSIS?')
		return trim_str_response(response)

	def set_msis(self, msus: str) -> None:
		"""SCPI: MMEMory:MSIS \n
		Snippet: driver.massMemory.set_msis(msus = 'abc') \n
		No command help available \n
			:param msus: No help available
		"""
		param = Conversions.value_to_quoted_str(msus)
		self._core.io.write(f'MMEMory:MSIS {param}')

	def delete_directory(self, directory_name: str) -> None:
		"""SCPI: MMEMory:RDIRectory \n
		Snippet: driver.massMemory.delete_directory(directory_name = 'abc') \n
		Removes an existing empty directory from the mass memory storage system. \n
			:param directory_name: Wildcards are not allowed.
		"""
		param = Conversions.value_to_quoted_str(directory_name)
		self._core.io.write(f'MMEMory:RDIRectory {param}')

	def save(self, filename: str, msus: str = None) -> None:
		"""SCPI: MMEMory:SAV \n
		Snippet: driver.massMemory.save(filename = 'abc', msus = 'abc') \n
		Stores the current instrument settings to the specified file. This command has the same effect as the combination of *SAV
		and method RsCMPX_Base.MassMemory.Store.State.set. \n
			:param filename: No help available
			:param msus: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('msus', msus, DataType.String, None, is_optional=True))
		self._core.io.write(f'MMEMory:SAV {param}'.rstrip())

	def recall(self, filename: str, msus: str = None) -> None:
		"""SCPI: MMEMory:RCL \n
		Snippet: driver.massMemory.recall(filename = 'abc', msus = 'abc') \n
		Restores the instrument settings from the specified file. This command has the same effect as the combination of method
		RsCMPX_Base.MassMemory.Load.State.set and *RCL. \n
			:param filename: No help available
			:param msus: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('msus', msus, DataType.String, None, is_optional=True))
		self._core.io.write(f'MMEMory:RCL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AliasesStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Alias: List[str]: No parameter help available
			- Path: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Alias', DataType.StringList, None, False, True, 1),
			ArgStruct('Path', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Alias: List[str] = None
			self.Path: List[str] = None

	def get_aliases(self) -> AliasesStruct:
		"""SCPI: MMEMory:ALIases \n
		Snippet: value: AliasesStruct = driver.massMemory.get_aliases() \n
		Returns the defined alias entries and the assigned directories. These settings are predefined and cannot be configured. \n
			:return: structure: for return value, see the help for AliasesStruct structure arguments.
		"""
		return self._core.io.query_struct('MMEMory:ALIases?', self.__class__.AliasesStruct())

	def clone(self) -> 'MassMemoryCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MassMemoryCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
