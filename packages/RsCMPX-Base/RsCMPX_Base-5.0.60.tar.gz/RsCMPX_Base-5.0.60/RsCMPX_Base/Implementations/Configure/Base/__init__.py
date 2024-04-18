from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BaseCls:
	"""Base commands group definition. 27 total commands, 8 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def multiCmw(self):
		"""multiCmw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiCmw'):
			from .MultiCmw import MultiCmwCls
			self._multiCmw = MultiCmwCls(self._core, self._cmd_group)
		return self._multiCmw

	@property
	def ipSet(self):
		"""ipSet commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSet'):
			from .IpSet import IpSetCls
			self._ipSet = IpSetCls(self._core, self._cmd_group)
		return self._ipSet

	@property
	def adjustment(self):
		"""adjustment commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_adjustment'):
			from .Adjustment import AdjustmentCls
			self._adjustment = AdjustmentCls(self._core, self._cmd_group)
		return self._adjustment

	@property
	def ipcr(self):
		"""ipcr commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ipcr'):
			from .Ipcr import IpcrCls
			self._ipcr = IpcrCls(self._core, self._cmd_group)
		return self._ipcr

	@property
	def freqCorrection(self):
		"""freqCorrection commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_freqCorrection'):
			from .FreqCorrection import FreqCorrectionCls
			self._freqCorrection = FreqCorrectionCls(self._core, self._cmd_group)
		return self._freqCorrection

	@property
	def correction(self):
		"""correction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import CorrectionCls
			self._correction = CorrectionCls(self._core, self._cmd_group)
		return self._correction

	@property
	def mmonitor(self):
		"""mmonitor commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mmonitor'):
			from .Mmonitor import MmonitorCls
			self._mmonitor = MmonitorCls(self._core, self._cmd_group)
		return self._mmonitor

	@property
	def salignment(self):
		"""salignment commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_salignment'):
			from .Salignment import SalignmentCls
			self._salignment = SalignmentCls(self._core, self._cmd_group)
		return self._salignment

	# noinspection PyTypeChecker
	def get_fcontrol(self) -> enums.FanMode:
		"""SCPI: CONFigure:BASE:FCONtrol \n
		Snippet: value: enums.FanMode = driver.configure.base.get_fcontrol() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BASE:FCONtrol?')
		return Conversions.str_to_scalar_enum(response, enums.FanMode)

	def set_fcontrol(self, mode: enums.FanMode) -> None:
		"""SCPI: CONFigure:BASE:FCONtrol \n
		Snippet: driver.configure.base.set_fcontrol(mode = enums.FanMode.HIGH) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FanMode)
		self._core.io.write(f'CONFigure:BASE:FCONtrol {param}')

	def clone(self) -> 'BaseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BaseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
