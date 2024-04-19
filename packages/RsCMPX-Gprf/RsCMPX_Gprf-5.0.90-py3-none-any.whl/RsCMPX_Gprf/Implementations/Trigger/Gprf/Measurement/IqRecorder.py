from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqRecorderCls:
	"""IqRecorder commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqRecorder", core, parent)

	def get_offset(self) -> int:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:OFFSet \n
		Snippet: value: int = driver.trigger.gprf.measurement.iqRecorder.get_offset() \n
		Defines a delay time for triggered measurements. The trigger offset delays the start of the measurement relative to the
		trigger event. \n
			:return: trigger_offset: Trigger offset in samples.
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:OFFSet?')
		return Conversions.str_to_int(response)

	def set_offset(self, trigger_offset: int) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:OFFSet \n
		Snippet: driver.trigger.gprf.measurement.iqRecorder.set_offset(trigger_offset = 1) \n
		Defines a delay time for triggered measurements. The trigger offset delays the start of the measurement relative to the
		trigger event. \n
			:param trigger_offset: Trigger offset in samples.
		"""
		param = Conversions.decimal_value_to_str(trigger_offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:OFFSet {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:MGAP \n
		Snippet: value: float = driver.trigger.gprf.measurement.iqRecorder.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. The I/Q recorder always runs in single-shot mode. Therefore it is controlled by
		a single trigger event. The minimum trigger gap condition is valid between the start of the measurement and the first
		trigger event. \n
			:return: minimum_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:MGAP \n
		Snippet: driver.trigger.gprf.measurement.iqRecorder.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. The I/Q recorder always runs in single-shot mode. Therefore it is controlled by
		a single trigger event. The minimum trigger gap condition is valid between the start of the measurement and the first
		trigger event. \n
			:param minimum_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:MGAP {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:TOUT \n
		Snippet: value: float or bool = driver.trigger.gprf.measurement.iqRecorder.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:return: timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:TOUT \n
		Snippet: driver.trigger.gprf.measurement.iqRecorder.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:param timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:TOUT {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:THReshold \n
		Snippet: value: float = driver.trigger.gprf.measurement.iqRecorder.get_threshold() \n
		Defines the trigger threshold for power trigger sources. Signals below the threshold are not evaluated for the phase
		change trigger source. \n
			:return: threshold: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:THReshold \n
		Snippet: driver.trigger.gprf.measurement.iqRecorder.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. Signals below the threshold are not evaluated for the phase
		change trigger source. \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:THReshold {param}')

	def get_pc_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTHreshold \n
		Snippet: value: float = driver.trigger.gprf.measurement.iqRecorder.get_pc_threshold() \n
		Defines the minimum absolute phase change required to generate a trigger event for the phase change trigger source. \n
			:return: phase_chg_thres: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTHreshold?')
		return Conversions.str_to_float(response)

	def set_pc_threshold(self, phase_chg_thres: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTHreshold \n
		Snippet: driver.trigger.gprf.measurement.iqRecorder.set_pc_threshold(phase_chg_thres = 1.0) \n
		Defines the minimum absolute phase change required to generate a trigger event for the phase change trigger source. \n
			:param phase_chg_thres: No help available
		"""
		param = Conversions.decimal_value_to_str(phase_chg_thres)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTHreshold {param}')

	def get_pc_time(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTime \n
		Snippet: value: float or bool = driver.trigger.gprf.measurement.iqRecorder.get_pc_time() \n
		Defines the time interval during which a phase change must occur to generate a trigger event for the phase change trigger
		source. \n
			:return: phase_chg_time: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTime?')
		return Conversions.str_to_float_or_bool(response)

	def set_pc_time(self, phase_chg_time: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTime \n
		Snippet: driver.trigger.gprf.measurement.iqRecorder.set_pc_time(phase_chg_time = 1.0) \n
		Defines the time interval during which a phase change must occur to generate a trigger event for the phase change trigger
		source. \n
			:param phase_chg_time: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(phase_chg_time)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:PCTime {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlopeExt:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SLOPe \n
		Snippet: value: enums.SignalSlopeExt = driver.trigger.gprf.measurement.iqRecorder.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: event: REDGe: rising edge FEDGe: falling edge
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlopeExt)

	def set_slope(self, event: enums.SignalSlopeExt) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SLOPe \n
		Snippet: driver.trigger.gprf.measurement.iqRecorder.set_slope(event = enums.SignalSlopeExt.FALLing) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param event: REDGe: rising edge FEDGe: falling edge
		"""
		param = Conversions.enum_scalar_to_str(event, enums.SignalSlopeExt)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQRecorder:SLOPe {param}')
