from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UprofileCls:
	"""Uprofile commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uprofile", core, parent)

	def save(self, save_user_profile: str) -> None:
		"""SCPI: CONFigure:SELFtest:UPRofile:SAVE \n
		Snippet: driver.configure.selftest.uprofile.save(save_user_profile = 'abc') \n
		No command help available \n
			:param save_user_profile: No help available
		"""
		param = Conversions.value_to_quoted_str(save_user_profile)
		self._core.io.write(f'CONFigure:SELFtest:UPRofile:SAVE {param}')

	def get_load(self) -> str:
		"""SCPI: CONFigure:SELFtest:UPRofile:LOAD \n
		Snippet: value: str = driver.configure.selftest.uprofile.get_load() \n
		No command help available \n
			:return: user_profile: No help available
		"""
		response = self._core.io.query_str('CONFigure:SELFtest:UPRofile:LOAD?')
		return trim_str_response(response)

	def set_load(self, user_profile: str) -> None:
		"""SCPI: CONFigure:SELFtest:UPRofile:LOAD \n
		Snippet: driver.configure.selftest.uprofile.set_load(user_profile = 'abc') \n
		No command help available \n
			:param user_profile: No help available
		"""
		param = Conversions.value_to_quoted_str(user_profile)
		self._core.io.write(f'CONFigure:SELFtest:UPRofile:LOAD {param}')
