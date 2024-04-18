from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AttributeCls:
	"""Attribute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attribute", core, parent)

	def set(self, path_name: str, attributes: str) -> None:
		"""SCPI: MMEMory:ATTRibute \n
		Snippet: driver.massMemory.attribute.set(path_name = 'abc', attributes = 'abc') \n
		Sets or removes file attributes for files and directories. \n
			:param path_name: No help available
			:param attributes: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('path_name', path_name, DataType.String), ArgSingle('attributes', attributes, DataType.String))
		self._core.io.write(f'MMEMory:ATTRibute {param}'.rstrip())

	def get(self, path_name: str) -> List[str]:
		"""SCPI: MMEMory:ATTRibute \n
		Snippet: value: List[str] = driver.massMemory.attribute.get(path_name = 'abc') \n
		Sets or removes file attributes for files and directories. \n
			:param path_name: No help available
			:return: file_entry: Comma-separated list of strings. Information strings are returned for the directories '.' and '..', for files and for subdirectories. Each string has the format 'ObjectName,Attributes'."""
		param = Conversions.value_to_quoted_str(path_name)
		response = self._core.io.query_str(f'MMEMory:ATTRibute? {param}')
		return Conversions.str_to_str_list(response)
