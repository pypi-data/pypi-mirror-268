from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 201 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def power(self):
		"""power commands group. 13 Sub-classes, 3 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def iqVsSlot(self):
		"""iqVsSlot commands group. 7 Sub-classes, 3 commands."""
		if not hasattr(self, '_iqVsSlot'):
			from .IqVsSlot import IqVsSlotCls
			self._iqVsSlot = IqVsSlotCls(self._core, self._cmd_group)
		return self._iqVsSlot

	@property
	def extPwrSensor(self):
		"""extPwrSensor commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_extPwrSensor'):
			from .ExtPwrSensor import ExtPwrSensorCls
			self._extPwrSensor = ExtPwrSensorCls(self._core, self._cmd_group)
		return self._extPwrSensor

	@property
	def nrpm(self):
		"""nrpm commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_nrpm'):
			from .Nrpm import NrpmCls
			self._nrpm = NrpmCls(self._core, self._cmd_group)
		return self._nrpm

	@property
	def iqRecorder(self):
		"""iqRecorder commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_iqRecorder'):
			from .IqRecorder import IqRecorderCls
			self._iqRecorder = IqRecorderCls(self._core, self._cmd_group)
		return self._iqRecorder

	@property
	def spectrum(self):
		"""spectrum commands group. 8 Sub-classes, 3 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def fftSpecAn(self):
		"""fftSpecAn commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_fftSpecAn'):
			from .FftSpecAn import FftSpecAnCls
			self._fftSpecAn = FftSpecAnCls(self._core, self._cmd_group)
		return self._fftSpecAn

	@property
	def canalyzer(self):
		"""canalyzer commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_canalyzer'):
			from .Canalyzer import CanalyzerCls
			self._canalyzer = CanalyzerCls(self._core, self._cmd_group)
		return self._canalyzer

	@property
	def ploss(self):
		"""ploss commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_ploss'):
			from .Ploss import PlossCls
			self._ploss = PlossCls(self._core, self._cmd_group)
		return self._ploss

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
