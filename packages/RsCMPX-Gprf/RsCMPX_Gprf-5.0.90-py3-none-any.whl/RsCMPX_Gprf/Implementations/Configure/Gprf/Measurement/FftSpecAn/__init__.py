from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftSpecAnCls:
	"""FftSpecAn commands group definition. 10 total commands, 1 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fftSpecAn", core, parent)

	@property
	def peakSearch(self):
		"""peakSearch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_peakSearch'):
			from .PeakSearch import PeakSearchCls
			self._peakSearch = PeakSearchCls(self._core, self._cmd_group)
		return self._peakSearch

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT \n
		Snippet: value: float = driver.configure.gprf.measurement.fftSpecAn.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: tcd_timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.set_timeout(tcd_timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:param tcd_timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(tcd_timeout)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT {param}')

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.AveragingMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:AMODe \n
		Snippet: value: enums.AveragingMode = driver.configure.gprf.measurement.fftSpecAn.get_amode() \n
		Selects the averaging mode for the average spectrum trace. \n
			:return: averaging_mode: LINear: averaging of linear power values LOGarithmic: averaging of logarithmic power values
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AveragingMode)

	def set_amode(self, averaging_mode: enums.AveragingMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:AMODe \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.set_amode(averaging_mode = enums.AveragingMode.LINear) \n
		Selects the averaging mode for the average spectrum trace. \n
			:param averaging_mode: LINear: averaging of linear power values LOGarithmic: averaging of logarithmic power values
		"""
		param = Conversions.enum_scalar_to_str(averaging_mode, enums.AveragingMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:AMODe {param}')

	# noinspection PyTypeChecker
	def get_detector(self) -> enums.DetectorBasic:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:DETector \n
		Snippet: value: enums.DetectorBasic = driver.configure.gprf.measurement.fftSpecAn.get_detector() \n
		Defines how the spectrum diagram is calculated from the frequency domain samples. \n
			:return: detector: PEAK: The peak value of adjacent samples is used. RMS: The RMS value of adjacent samples is used.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:DETector?')
		return Conversions.str_to_scalar_enum(response, enums.DetectorBasic)

	def set_detector(self, detector: enums.DetectorBasic) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:DETector \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.set_detector(detector = enums.DetectorBasic.PEAK) \n
		Defines how the spectrum diagram is calculated from the frequency domain samples. \n
			:param detector: PEAK: The peak value of adjacent samples is used. RMS: The RMS value of adjacent samples is used.
		"""
		param = Conversions.enum_scalar_to_str(detector, enums.DetectorBasic)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:DETector {param}')

	def get_fft_length(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FFTLength \n
		Snippet: value: int = driver.configure.gprf.measurement.fftSpecAn.get_fft_length() \n
		Selects the number of samples recorded per measurement interval. \n
			:return: length: Only the following values can be configured: 1024, 2048, 4096, 8192, 16384 Other values are rounded to the next allowed value.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FFTLength?')
		return Conversions.str_to_int(response)

	def set_fft_length(self, length: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FFTLength \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.set_fft_length(length = 1) \n
		Selects the number of samples recorded per measurement interval. \n
			:param length: Only the following values can be configured: 1024, 2048, 4096, 8192, 16384 Other values are rounded to the next allowed value.
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FFTLength {param}')

	def get_fspan(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FSPan \n
		Snippet: value: float = driver.configure.gprf.measurement.fftSpecAn.get_fspan() \n
		Configures the frequency span of the FFT spectrum analyzer. \n
			:return: frequency_span: Only the following values can be configured, all values in MHz: IF unit: 10, 20, 40, 80, 160, 250, 500, 1000 RF unit: 10, 20, 40, 80, 160, 250 R&S CMW: 1.25, 2.5, 5, 10, 20, 40, 80, 160 Other values are rounded to the next allowed value.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FSPan?')
		return Conversions.str_to_float(response)

	def set_fspan(self, frequency_span: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FSPan \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.set_fspan(frequency_span = 1.0) \n
		Configures the frequency span of the FFT spectrum analyzer. \n
			:param frequency_span: Only the following values can be configured, all values in MHz: IF unit: 10, 20, 40, 80, 160, 250, 500, 1000 RF unit: 10, 20, 40, 80, 160, 250 R&S CMW: 1.25, 2.5, 5, 10, 20, 40, 80, 160 Other values are rounded to the next allowed value.
		"""
		param = Conversions.decimal_value_to_str(frequency_span)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FSPan {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:MOEXception \n
		Snippet: value: bool = driver.configure.gprf.measurement.fftSpecAn.get_mo_exception() \n
		Specifies whether measurement results that the CMX500 identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:MOEXception \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the CMX500 identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.gprf.measurement.fftSpecAn.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:REPetition \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:REPetition {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:SCOunt \n
		Snippet: value: int = driver.configure.gprf.measurement.fftSpecAn.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: Number of measurement intervals
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:SCOunt \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: Number of measurement intervals
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:SCOunt {param}')

	def clone(self) -> 'FftSpecAnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FftSpecAnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
