from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqVsSlotCls:
	"""IqVsSlot commands group definition. 6 total commands, 0 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqVsSlot", core, parent)

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:MGAP \n
		Snippet: value: float = driver.trigger.gprf.measurement.iqVsSlot.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: minimum_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQVSlot:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:MGAP \n
		Snippet: driver.trigger.gprf.measurement.iqVsSlot.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param minimum_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQVSlot:MGAP {param}')

	def get_offset(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:OFFSet \n
		Snippet: value: float = driver.trigger.gprf.measurement.iqVsSlot.get_offset() \n
		Defines a delay time for triggered measurements. The trigger offset delays the start of the measurement relative to the
		trigger event. \n
			:return: offset: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQVSlot:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:OFFSet \n
		Snippet: driver.trigger.gprf.measurement.iqVsSlot.set_offset(offset = 1.0) \n
		Defines a delay time for triggered measurements. The trigger offset delays the start of the measurement relative to the
		trigger event. \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQVSlot:OFFSet {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:TOUT \n
		Snippet: value: float or bool = driver.trigger.gprf.measurement.iqVsSlot.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:return: timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQVSlot:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:TOUT \n
		Snippet: driver.trigger.gprf.measurement.iqVsSlot.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:param timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQVSlot:TOUT {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:THReshold \n
		Snippet: value: float = driver.trigger.gprf.measurement.iqVsSlot.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: threshold: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQVSlot:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:THReshold \n
		Snippet: driver.trigger.gprf.measurement.iqVsSlot.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQVSlot:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlopeExt:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:SLOPe \n
		Snippet: value: enums.SignalSlopeExt = driver.trigger.gprf.measurement.iqVsSlot.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: event: REDGe: Rising edge FEDGe: Falling edge
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQVSlot:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlopeExt)

	def set_slope(self, event: enums.SignalSlopeExt) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:SLOPe \n
		Snippet: driver.trigger.gprf.measurement.iqVsSlot.set_slope(event = enums.SignalSlopeExt.FALLing) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param event: REDGe: Rising edge FEDGe: Falling edge
		"""
		param = Conversions.enum_scalar_to_str(event, enums.SignalSlopeExt)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQVSlot:SLOPe {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.TriggerSequenceMode:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:MODE \n
		Snippet: value: enums.TriggerSequenceMode = driver.trigger.gprf.measurement.iqVsSlot.get_mode() \n
		Selects the measurement sequence that is triggered by each single trigger event. This setting is not valid for free run
		measurements. \n
			:return: mode: ONCE: Trigger Once PRESelect: Retrigger Preselect
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:IQVSlot:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSequenceMode)

	def set_mode(self, mode: enums.TriggerSequenceMode) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:IQVSlot:MODE \n
		Snippet: driver.trigger.gprf.measurement.iqVsSlot.set_mode(mode = enums.TriggerSequenceMode.ONCE) \n
		Selects the measurement sequence that is triggered by each single trigger event. This setting is not valid for free run
		measurements. \n
			:param mode: ONCE: Trigger Once PRESelect: Retrigger Preselect
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TriggerSequenceMode)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:IQVSlot:MODE {param}')
