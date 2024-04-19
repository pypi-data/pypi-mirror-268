from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqRecorderCls:
	"""IqRecorder commands group definition. 26 total commands, 4 Subgroups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqRecorder", core, parent)

	@property
	def capture(self):
		"""capture commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_capture'):
			from .Capture import CaptureCls
			self._capture = CaptureCls(self._core, self._cmd_group)
		return self._capture

	@property
	def iqSettings(self):
		"""iqSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqSettings'):
			from .IqSettings import IqSettingsCls
			self._iqSettings = IqSettingsCls(self._core, self._cmd_group)
		return self._iqSettings

	@property
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def listPy(self):
		"""listPy commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	def get_symbol_rate(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:SRATe \n
		Snippet: value: float = driver.configure.gprf.measurement.iqRecorder.get_symbol_rate() \n
		No command help available \n
			:return: sample_rate: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:SRATe?')
		return Conversions.str_to_float(response)

	def set_symbol_rate(self, sample_rate: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:SRATe \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_symbol_rate(sample_rate = 1.0) \n
		No command help available \n
			:param sample_rate: No help available
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:SRATe {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.MeasurementMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:MODE \n
		Snippet: value: enums.MeasurementMode = driver.configure.gprf.measurement.iqRecorder.get_mode() \n
		No command help available \n
			:return: measurement_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementMode)

	def set_mode(self, measurement_mode: enums.MeasurementMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:MODE \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_mode(measurement_mode = enums.MeasurementMode.NORMal) \n
		No command help available \n
			:param measurement_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(measurement_mode, enums.MeasurementMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:MODE {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:TOUT \n
		Snippet: value: float = driver.configure.gprf.measurement.iqRecorder.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: tcd_timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:TOUT \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_timeout(tcd_timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:TOUT {param}')

	def get_ratio(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:RATio \n
		Snippet: value: float = driver.configure.gprf.measurement.iqRecorder.get_ratio() \n
		Specifies a factor to reduce the sampling rate and to increase the measurement duration. The sampling rate resulting from
		the filter settings is multiplied with the specified ratio. \n
			:return: ratio: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:RATio \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_ratio(ratio = 1.0) \n
		Specifies a factor to reduce the sampling rate and to increase the measurement duration. The sampling rate resulting from
		the filter settings is multiplied with the specified ratio. \n
			:param ratio: No help available
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:RATio {param}')

	# noinspection PyTypeChecker
	def get_bypass(self) -> enums.IqRecBypass:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:BYPass \n
		Snippet: value: enums.IqRecBypass = driver.configure.gprf.measurement.iqRecorder.get_bypass() \n
		No command help available \n
			:return: bypass: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:BYPass?')
		return Conversions.str_to_scalar_enum(response, enums.IqRecBypass)

	def set_bypass(self, bypass: enums.IqRecBypass) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:BYPass \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_bypass(bypass = enums.IqRecBypass.BIT) \n
		No command help available \n
			:param bypass: No help available
		"""
		param = Conversions.enum_scalar_to_str(bypass, enums.IqRecBypass)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:BYPass {param}')

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.IqFormat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FORMat \n
		Snippet: value: enums.IqFormat = driver.configure.gprf.measurement.iqRecorder.get_format_py() \n
		Selects the coordinate system for the I/Q recorder results. \n
			:return: format_py: IQ: Cartesian coordinates (I- and Q-axis) RPHI: polar coordinates (radius R and angle PHI)
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.IqFormat)

	def set_format_py(self, format_py: enums.IqFormat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FORMat \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_format_py(format_py = enums.IqFormat.IQ) \n
		Selects the coordinate system for the I/Q recorder results. \n
			:param format_py: IQ: Cartesian coordinates (I- and Q-axis) RPHI: polar coordinates (radius R and angle PHI)
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.IqFormat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FORMat {param}')

	# noinspection PyTypeChecker
	def get_munit(self) -> enums.MagnitudeUnit:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:MUNit \n
		Snippet: value: enums.MagnitudeUnit = driver.configure.gprf.measurement.iqRecorder.get_munit() \n
		Selects the magnitude unit for the measurement results. \n
			:return: magnitude_unit: Voltage units or raw I/Q data relative to full-scale.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:MUNit?')
		return Conversions.str_to_scalar_enum(response, enums.MagnitudeUnit)

	def set_munit(self, magnitude_unit: enums.MagnitudeUnit) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:MUNit \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_munit(magnitude_unit = enums.MagnitudeUnit.RAW) \n
		Selects the magnitude unit for the measurement results. \n
			:param magnitude_unit: Voltage units or raw I/Q data relative to full-scale.
		"""
		param = Conversions.enum_scalar_to_str(magnitude_unit, enums.MagnitudeUnit)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:MUNit {param}')

	# noinspection PyTypeChecker
	def get_user(self) -> enums.UserDebugMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:USER \n
		Snippet: value: enums.UserDebugMode = driver.configure.gprf.measurement.iqRecorder.get_user() \n
		No command help available \n
			:return: user_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:USER?')
		return Conversions.str_to_scalar_enum(response, enums.UserDebugMode)

	def set_user(self, user_mode: enums.UserDebugMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:USER \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_user(user_mode = enums.UserDebugMode.DEBug) \n
		No command help available \n
			:param user_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(user_mode, enums.UserDebugMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:USER {param}')

	def get_iq_file(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:IQFile \n
		Snippet: value: str = driver.configure.gprf.measurement.iqRecorder.get_iq_file() \n
		Selects a file for storage of the I/Q recorder results in binary format. \n
			:return: iq_save_file: Name and path of the file. The extension *.iqw is appended automatically.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:IQFile?')
		return trim_str_response(response)

	def set_iq_file(self, iq_save_file: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:IQFile \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_iq_file(iq_save_file = 'abc') \n
		Selects a file for storage of the I/Q recorder results in binary format. \n
			:param iq_save_file: Name and path of the file. The extension *.iqw is appended automatically.
		"""
		param = Conversions.value_to_quoted_str(iq_save_file)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:IQFile {param}')

	# noinspection PyTypeChecker
	def get_wt_file(self) -> enums.FileSave:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:WTFile \n
		Snippet: value: enums.FileSave = driver.configure.gprf.measurement.iqRecorder.get_wt_file() \n
		Selects whether the results are written to a file, to the memory or both. For file selection, see method RsCMPX_Gprf.
		Configure.Gprf.Measurement.IqRecorder.iqFile. \n
			:return: write_to_iq_file: OFF: The results are only stored in the memory. ON: The results are stored in the memory and in a file. ONLY: The results are only stored in a file.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:WTFile?')
		return Conversions.str_to_scalar_enum(response, enums.FileSave)

	def set_wt_file(self, write_to_iq_file: enums.FileSave) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:WTFile \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_wt_file(write_to_iq_file = enums.FileSave.OFF) \n
		Selects whether the results are written to a file, to the memory or both. For file selection, see method RsCMPX_Gprf.
		Configure.Gprf.Measurement.IqRecorder.iqFile. \n
			:param write_to_iq_file: OFF: The results are only stored in the memory. ON: The results are stored in the memory and in a file. ONLY: The results are only stored in a file.
		"""
		param = Conversions.enum_scalar_to_str(write_to_iq_file, enums.FileSave)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:WTFile {param}')

	def get_ini_file(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:INIFile \n
		Snippet: value: str = driver.configure.gprf.measurement.iqRecorder.get_ini_file() \n
		No command help available \n
			:return: ini_file: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:INIFile?')
		return trim_str_response(response)

	def set_ini_file(self, ini_file: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:INIFile \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.set_ini_file(ini_file = 'abc') \n
		No command help available \n
			:param ini_file: No help available
		"""
		param = Conversions.value_to_quoted_str(ini_file)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:INIFile {param}')

	def clone(self) -> 'IqRecorderCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqRecorderCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
