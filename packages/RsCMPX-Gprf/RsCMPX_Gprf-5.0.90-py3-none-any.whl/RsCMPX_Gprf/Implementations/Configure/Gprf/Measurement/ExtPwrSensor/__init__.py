from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtPwrSensorCls:
	"""ExtPwrSensor commands group definition. 12 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extPwrSensor", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def attenuation(self):
		"""attenuation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_attenuation'):
			from .Attenuation import AttenuationCls
			self._attenuation = AttenuationCls(self._core, self._cmd_group)
		return self._attenuation

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:TOUT \n
		Snippet: value: float = driver.configure.gprf.measurement.extPwrSensor.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: tcd_timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:TOUT \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.set_timeout(tcd_timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:TOUT {param}')

	# noinspection PyTypeChecker
	def get_resolution(self) -> enums.PwrSensorResolution:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:RESolution \n
		Snippet: value: enums.PwrSensorResolution = driver.configure.gprf.measurement.extPwrSensor.get_resolution() \n
		Defines the number of digits of the displayed power results. This command does not affect the remote control results. \n
			:return: resolution: PD0: 1 (results rounded to 1 dB) PD1: 0.1 PD2: 0.01 PD3: 0.001
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:RESolution?')
		return Conversions.str_to_scalar_enum(response, enums.PwrSensorResolution)

	def set_resolution(self, resolution: enums.PwrSensorResolution) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:RESolution \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.set_resolution(resolution = enums.PwrSensorResolution.PD0) \n
		Defines the number of digits of the displayed power results. This command does not affect the remote control results. \n
			:param resolution: PD0: 1 (results rounded to 1 dB) PD1: 0.1 PD2: 0.01 PD3: 0.001
		"""
		param = Conversions.enum_scalar_to_str(resolution, enums.PwrSensorResolution)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:RESolution {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:SCOunt \n
		Snippet: value: int = driver.configure.gprf.measurement.extPwrSensor.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:SCOunt \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:SCOunt {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.gprf.measurement.extPwrSensor.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:REPetition \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:REPetition {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:FREQuency \n
		Snippet: value: float = driver.configure.gprf.measurement.extPwrSensor.get_frequency() \n
		Specifies the input frequency at the power sensor. \n
			:return: correction_freq: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, correction_freq: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:FREQuency \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.set_frequency(correction_freq = 1.0) \n
		Specifies the input frequency at the power sensor. \n
			:param correction_freq: No help available
		"""
		param = Conversions.decimal_value_to_str(correction_freq)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:FREQuency {param}')

	def clone(self) -> 'ExtPwrSensorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ExtPwrSensorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
