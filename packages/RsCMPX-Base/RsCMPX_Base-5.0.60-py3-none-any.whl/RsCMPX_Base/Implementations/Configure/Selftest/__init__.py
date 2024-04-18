from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelftestCls:
	"""Selftest commands group definition. 11 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selftest", core, parent)

	@property
	def info(self):
		"""info commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import InfoCls
			self._info = InfoCls(self._core, self._cmd_group)
		return self._info

	@property
	def uprofile(self):
		"""uprofile commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_uprofile'):
			from .Uprofile import UprofileCls
			self._uprofile = UprofileCls(self._core, self._cmd_group)
		return self._uprofile

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import SelectCls
			self._select = SelectCls(self._core, self._cmd_group)
		return self._select

	def get_as_meas(self) -> bool:
		"""SCPI: CONFigure:SELFtest:ASMeas \n
		Snippet: value: bool = driver.configure.selftest.get_as_meas() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:SELFtest:ASMeas?')
		return Conversions.str_to_bool(response)

	def set_as_meas(self, state: bool) -> None:
		"""SCPI: CONFigure:SELFtest:ASMeas \n
		Snippet: driver.configure.selftest.set_as_meas(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:SELFtest:ASMeas {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.SelftestStopCondition:
		"""SCPI: CONFigure:SELFtest:SCONdition \n
		Snippet: value: enums.SelftestStopCondition = driver.configure.selftest.get_scondition() \n
		No command help available \n
			:return: stop_condition: No help available
		"""
		response = self._core.io.query_str('CONFigure:SELFtest:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.SelftestStopCondition)

	def set_scondition(self, stop_condition: enums.SelftestStopCondition) -> None:
		"""SCPI: CONFigure:SELFtest:SCONdition \n
		Snippet: driver.configure.selftest.set_scondition(stop_condition = enums.SelftestStopCondition.NONE) \n
		No command help available \n
			:param stop_condition: No help available
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.SelftestStopCondition)
		self._core.io.write(f'CONFigure:SELFtest:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:SELFtest:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.selftest.get_repetition() \n
		No command help available \n
			:return: repetition: No help available
		"""
		response = self._core.io.query_str('CONFigure:SELFtest:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:SELFtest:REPetition \n
		Snippet: driver.configure.selftest.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		No command help available \n
			:param repetition: No help available
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:SELFtest:REPetition {param}')

	# noinspection PyTypeChecker
	def get_smode(self) -> enums.SelftestSpecMode:
		"""SCPI: CONFigure:SELFtest:SMODe \n
		Snippet: value: enums.SelftestSpecMode = driver.configure.selftest.get_smode() \n
		No command help available \n
			:return: spec_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:SELFtest:SMODe?')
		return Conversions.str_to_scalar_enum(response, enums.SelftestSpecMode)

	def set_smode(self, spec_mode: enums.SelftestSpecMode) -> None:
		"""SCPI: CONFigure:SELFtest:SMODe \n
		Snippet: driver.configure.selftest.set_smode(spec_mode = enums.SelftestSpecMode.NONE) \n
		No command help available \n
			:param spec_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(spec_mode, enums.SelftestSpecMode)
		self._core.io.write(f'CONFigure:SELFtest:SMODe {param}')

	# noinspection PyTypeChecker
	def get_execution(self) -> enums.Execution:
		"""SCPI: CONFigure:SELFtest:EXECution \n
		Snippet: value: enums.Execution = driver.configure.selftest.get_execution() \n
		No command help available \n
			:return: execution: No help available
		"""
		response = self._core.io.query_str('CONFigure:SELFtest:EXECution?')
		return Conversions.str_to_scalar_enum(response, enums.Execution)

	def set_execution(self, execution: enums.Execution) -> None:
		"""SCPI: CONFigure:SELFtest:EXECution \n
		Snippet: driver.configure.selftest.set_execution(execution = enums.Execution.CONCurrent) \n
		No command help available \n
			:param execution: No help available
		"""
		param = Conversions.enum_scalar_to_str(execution, enums.Execution)
		self._core.io.write(f'CONFigure:SELFtest:EXECution {param}')

	def clone(self) -> 'SelftestCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SelftestCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
