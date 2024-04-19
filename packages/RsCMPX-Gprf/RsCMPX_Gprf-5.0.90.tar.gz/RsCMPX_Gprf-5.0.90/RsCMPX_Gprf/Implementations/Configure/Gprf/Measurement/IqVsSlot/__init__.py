from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqVsSlotCls:
	"""IqVsSlot commands group definition. 18 total commands, 1 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqVsSlot", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 4 Sub-classes, 4 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TOUT \n
		Snippet: value: float = driver.configure.gprf.measurement.iqVsSlot.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: tcd_timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TOUT \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.set_timeout(tcd_timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.gprf.measurement.iqVsSlot.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:REPetition \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:REPetition {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SCOunt \n
		Snippet: value: int = driver.configure.gprf.measurement.iqVsSlot.get_scount() \n
		Defines the number of steps (measurement intervals) per subsweep. In list mode, the total number of steps must not exceed
		3000 (step count times number of subsweeps) . \n
			:return: step_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, step_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SCOunt \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.set_scount(step_count = 1) \n
		Defines the number of steps (measurement intervals) per subsweep. In list mode, the total number of steps must not exceed
		3000 (step count times number of subsweeps) . \n
			:param step_count: No help available
		"""
		param = Conversions.decimal_value_to_str(step_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SCOunt {param}')

	def get_mlength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:MLENgth \n
		Snippet: value: float = driver.configure.gprf.measurement.iqVsSlot.get_mlength() \n
		Sets the length of the evaluation intervals used to calculate the I/Q vs slot results for one measurement step. \n
			:return: meas_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:MLENgth?')
		return Conversions.str_to_float(response)

	def set_mlength(self, meas_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:MLENgth \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.set_mlength(meas_length = 1.0) \n
		Sets the length of the evaluation intervals used to calculate the I/Q vs slot results for one measurement step. \n
			:param meas_length: No help available
		"""
		param = Conversions.decimal_value_to_str(meas_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:MLENgth {param}')

	def get_slength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SLENgth \n
		Snippet: value: float = driver.configure.gprf.measurement.iqVsSlot.get_slength() \n
		Sets the time between the beginning of two consecutive measurement steps. \n
			:return: step_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SLENgth?')
		return Conversions.str_to_float(response)

	def set_slength(self, step_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SLENgth \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.set_slength(step_length = 1.0) \n
		Sets the time between the beginning of two consecutive measurement steps. \n
			:param step_length: No help available
		"""
		param = Conversions.decimal_value_to_str(step_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SLENgth {param}')

	# noinspection PyTypeChecker
	def get_ftype(self) -> enums.FilterType:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FTYPe \n
		Snippet: value: enums.FilterType = driver.configure.gprf.measurement.iqVsSlot.get_ftype() \n
		Selects the IF filter type. \n
			:return: filter_type: IF unit: B1MHz | B10Mhz RF unit: B1MHz | B10Mhz R&S CMW: GAUSs | NYQuist | NY1Mhz B1MHz: bandpass, 1-MHz BW B10Mhz: bandpass, 10-MHz BW GAUSs: Gaussian, 100-kHz BW NYQuist: Nyquist, 100-kHz BW NY1Mhz: Nyquist, 1-MHz BW
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.FilterType)

	def set_ftype(self, filter_type: enums.FilterType) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FTYPe \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.set_ftype(filter_type = enums.FilterType.B10Mhz) \n
		Selects the IF filter type. \n
			:param filter_type: IF unit: B1MHz | B10Mhz RF unit: B1MHz | B10Mhz R&S CMW: GAUSs | NYQuist | NY1Mhz B1MHz: bandpass, 1-MHz BW B10Mhz: bandpass, 10-MHz BW GAUSs: Gaussian, 100-kHz BW NYQuist: Nyquist, 100-kHz BW NY1Mhz: Nyquist, 1-MHz BW
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.FilterType)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FTYPe {param}')

	def get_fe_limit(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FELimit \n
		Snippet: value: float = driver.configure.gprf.measurement.iqVsSlot.get_fe_limit() \n
		Defines the frequency estimation limit as a signal level relative to the expected nominal power. Steps with a level below
		this limit are not used for the frequency correction and do not contribute to the frequency results. \n
			:return: limit: Range-100 dB to 0 dB*RST-100 dBDefault unitdB
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FELimit?')
		return Conversions.str_to_float(response)

	def set_fe_limit(self, limit: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FELimit \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.set_fe_limit(limit = 1.0) \n
		Defines the frequency estimation limit as a signal level relative to the expected nominal power. Steps with a level below
		this limit are not used for the frequency correction and do not contribute to the frequency results. \n
			:param limit: Range-100 dB to 0 dB*RST-100 dBDefault unitdB
		"""
		param = Conversions.decimal_value_to_str(limit)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FELimit {param}')

	def clone(self) -> 'IqVsSlotCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqVsSlotCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
