from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 48 total commands, 4 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def parameterSetList(self):
		"""parameterSetList commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_parameterSetList'):
			from .ParameterSetList import ParameterSetListCls
			self._parameterSetList = ParameterSetListCls(self._core, self._cmd_group)
		return self._parameterSetList

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def listPy(self):
		"""listPy commands group. 7 Sub-classes, 8 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.CcdfMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:MODE \n
		Snippet: value: enums.CcdfMode = driver.configure.gprf.measurement.power.get_mode() \n
		Selects the measurement mode for measurements without list mode. Select the mode before starting the power measurement. \n
			:return: ccdf_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CcdfMode)

	def set_mode(self, ccdf_mode: enums.CcdfMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:MODE \n
		Snippet: driver.configure.gprf.measurement.power.set_mode(ccdf_mode = enums.CcdfMode.POWer) \n
		Selects the measurement mode for measurements without list mode. Select the mode before starting the power measurement. \n
			:param ccdf_mode: POWer: Power mode STATistic: Statistic mode
		"""
		param = Conversions.enum_scalar_to_str(ccdf_mode, enums.CcdfMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:MODE {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:TOUT \n
		Snippet: value: float = driver.configure.gprf.measurement.power.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: tcd_timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:TOUT \n
		Snippet: driver.configure.gprf.measurement.power.set_timeout(tcd_timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:TOUT {param}')

	def get_slength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:SLENgth \n
		Snippet: value: float = driver.configure.gprf.measurement.power.get_slength() \n
		Sets the time between the beginning of two consecutive measurement lengths. \n
			:return: step_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:SLENgth?')
		return Conversions.str_to_float(response)

	def set_slength(self, step_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:SLENgth \n
		Snippet: driver.configure.gprf.measurement.power.set_slength(step_length = 1.0) \n
		Sets the time between the beginning of two consecutive measurement lengths. \n
			:param step_length: No help available
		"""
		param = Conversions.decimal_value_to_str(step_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:SLENgth {param}')

	def get_mlength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:MLENgth \n
		Snippet: value: float = driver.configure.gprf.measurement.power.get_mlength() \n
		Sets the length of the evaluation interval used to measure a single set of current power results. The measurement length
		cannot be greater than the step length. \n
			:return: meas_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:MLENgth?')
		return Conversions.str_to_float(response)

	def set_mlength(self, meas_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:MLENgth \n
		Snippet: driver.configure.gprf.measurement.power.set_mlength(meas_length = 1.0) \n
		Sets the length of the evaluation interval used to measure a single set of current power results. The measurement length
		cannot be greater than the step length. \n
			:param meas_length: No help available
		"""
		param = Conversions.decimal_value_to_str(meas_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:MLENgth {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.gprf.measurement.power.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:REPetition \n
		Snippet: driver.configure.gprf.measurement.power.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:REPetition {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:SCOunt \n
		Snippet: value: int = driver.configure.gprf.measurement.power.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: Number of measurement intervals
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:SCOunt \n
		Snippet: driver.configure.gprf.measurement.power.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: Number of measurement intervals
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:SCOunt {param}')

	def get_pdef_set(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PDEFset \n
		Snippet: value: str = driver.configure.gprf.measurement.power.get_pdef_set() \n
		No command help available \n
			:return: predefined_set: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:PDEFset?')
		return trim_str_response(response)

	def set_pdef_set(self, predefined_set: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PDEFset \n
		Snippet: driver.configure.gprf.measurement.power.set_pdef_set(predefined_set = 'abc') \n
		No command help available \n
			:param predefined_set: No help available
		"""
		param = Conversions.value_to_quoted_str(predefined_set)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PDEFset {param}')

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
