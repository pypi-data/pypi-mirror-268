from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrumCls:
	"""Spectrum commands group definition. 24 total commands, 3 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	@property
	def zeroSpan(self):
		"""zeroSpan commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_zeroSpan'):
			from .ZeroSpan import ZeroSpanCls
			self._zeroSpan = ZeroSpanCls(self._core, self._cmd_group)
		return self._zeroSpan

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def freqSweep(self):
		"""freqSweep commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_freqSweep'):
			from .FreqSweep import FreqSweepCls
			self._freqSweep = FreqSweepCls(self._core, self._cmd_group)
		return self._freqSweep

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.AveragingMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:AMODe \n
		Snippet: value: enums.AveragingMode = driver.configure.gprf.measurement.spectrum.get_amode() \n
		No command help available \n
			:return: averaging_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AveragingMode)

	def set_amode(self, averaging_mode: enums.AveragingMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:AMODe \n
		Snippet: driver.configure.gprf.measurement.spectrum.set_amode(averaging_mode = enums.AveragingMode.LINear) \n
		No command help available \n
			:param averaging_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(averaging_mode, enums.AveragingMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:AMODe {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.gprf.measurement.spectrum.get_repetition() \n
		No command help available \n
			:return: repetition: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:REPetition \n
		Snippet: driver.configure.gprf.measurement.spectrum.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		No command help available \n
			:param repetition: No help available
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:REPetition {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:TOUT \n
		Snippet: value: float = driver.configure.gprf.measurement.spectrum.get_timeout() \n
		No command help available \n
			:return: tcd_timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:TOUT \n
		Snippet: driver.configure.gprf.measurement.spectrum.set_timeout(tcd_timeout = 1.0) \n
		No command help available \n
			:param tcd_timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(tcd_timeout)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:TOUT {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:SCOunt \n
		Snippet: value: int = driver.configure.gprf.measurement.spectrum.get_scount() \n
		No command help available \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:SCOunt \n
		Snippet: driver.configure.gprf.measurement.spectrum.set_scount(statistic_count = 1) \n
		No command help available \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:SCOunt {param}')

	def clone(self) -> 'SpectrumCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpectrumCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
