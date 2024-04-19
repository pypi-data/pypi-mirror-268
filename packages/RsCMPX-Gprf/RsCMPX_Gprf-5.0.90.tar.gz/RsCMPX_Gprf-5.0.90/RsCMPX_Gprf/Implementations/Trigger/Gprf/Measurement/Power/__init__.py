from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 8 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def parameterSetList(self):
		"""parameterSetList commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_parameterSetList'):
			from .ParameterSetList import ParameterSetListCls
			self._parameterSetList = ParameterSetListCls(self._core, self._cmd_group)
		return self._parameterSetList

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:MGAP \n
		Snippet: value: float = driver.trigger.gprf.measurement.power.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: minimum_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:POWer:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:MGAP \n
		Snippet: driver.trigger.gprf.measurement.power.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param minimum_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:POWer:MGAP {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:TOUT \n
		Snippet: value: float or bool = driver.trigger.gprf.measurement.power.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:return: timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:POWer:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:TOUT \n
		Snippet: driver.trigger.gprf.measurement.power.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:param timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:POWer:TOUT {param}')

	def get_offset(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:OFFSet \n
		Snippet: value: float = driver.trigger.gprf.measurement.power.get_offset() \n
		Defines a delay time for triggered measurements. The trigger offset delays the start of the measurement relative to the
		trigger event. \n
			:return: offset: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:POWer:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:OFFSet \n
		Snippet: driver.trigger.gprf.measurement.power.set_offset(offset = 1.0) \n
		Defines a delay time for triggered measurements. The trigger offset delays the start of the measurement relative to the
		trigger event. \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:POWer:OFFSet {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.TriggerPowerMode:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:MODE \n
		Snippet: value: enums.TriggerPowerMode = driver.trigger.gprf.measurement.power.get_mode() \n
		Selects the measurement sequence that is triggered by each single trigger event. This setting is not valid for free run
		measurements. \n
			:return: mode: ONCE: Trigger Once SWEep: Retrigger Sweep ALL: Retrigger All PRESelect: Retrigger Preselect
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:POWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerPowerMode)

	def set_mode(self, mode: enums.TriggerPowerMode) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:MODE \n
		Snippet: driver.trigger.gprf.measurement.power.set_mode(mode = enums.TriggerPowerMode.ALL) \n
		Selects the measurement sequence that is triggered by each single trigger event. This setting is not valid for free run
		measurements. \n
			:param mode: ONCE: Trigger Once SWEep: Retrigger Sweep ALL: Retrigger All PRESelect: Retrigger Preselect
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TriggerPowerMode)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:POWer:MODE {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:THReshold \n
		Snippet: value: float = driver.trigger.gprf.measurement.power.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: threshold: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:POWer:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:THReshold \n
		Snippet: driver.trigger.gprf.measurement.power.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:POWer:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlopeExt:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:SLOPe \n
		Snippet: value: enums.SignalSlopeExt = driver.trigger.gprf.measurement.power.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: event: REDGe: rising edge FEDGe: falling edge
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:POWer:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlopeExt)

	def set_slope(self, event: enums.SignalSlopeExt) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:SLOPe \n
		Snippet: driver.trigger.gprf.measurement.power.set_slope(event = enums.SignalSlopeExt.FALLing) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param event: REDGe: rising edge FEDGe: falling edge
		"""
		param = Conversions.enum_scalar_to_str(event, enums.SignalSlopeExt)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:POWer:SLOPe {param}')

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
