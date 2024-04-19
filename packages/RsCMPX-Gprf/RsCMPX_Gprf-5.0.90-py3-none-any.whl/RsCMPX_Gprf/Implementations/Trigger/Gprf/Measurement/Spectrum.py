from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrumCls:
	"""Spectrum commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:THReshold \n
		Snippet: value: float = driver.trigger.gprf.measurement.spectrum.get_threshold() \n
		No command help available \n
			:return: threshold: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:THReshold \n
		Snippet: driver.trigger.gprf.measurement.spectrum.set_threshold(threshold = 1.0) \n
		No command help available \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlopeExt:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SLOPe \n
		Snippet: value: enums.SignalSlopeExt = driver.trigger.gprf.measurement.spectrum.get_slope() \n
		No command help available \n
			:return: slope: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlopeExt)

	def set_slope(self, slope: enums.SignalSlopeExt) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SLOPe \n
		Snippet: driver.trigger.gprf.measurement.spectrum.set_slope(slope = enums.SignalSlopeExt.FALLing) \n
		No command help available \n
			:param slope: No help available
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlopeExt)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:SLOPe {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:MGAP \n
		Snippet: value: float = driver.trigger.gprf.measurement.spectrum.get_mgap() \n
		No command help available \n
			:return: minimum_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:MGAP \n
		Snippet: driver.trigger.gprf.measurement.spectrum.set_mgap(minimum_gap = 1.0) \n
		No command help available \n
			:param minimum_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:MGAP {param}')

	def get_offset(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:OFFSet \n
		Snippet: value: float = driver.trigger.gprf.measurement.spectrum.get_offset() \n
		No command help available \n
			:return: trigger_offset: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, trigger_offset: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:OFFSet \n
		Snippet: driver.trigger.gprf.measurement.spectrum.set_offset(trigger_offset = 1.0) \n
		No command help available \n
			:param trigger_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(trigger_offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:OFFSet {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:TOUT \n
		Snippet: value: float or bool = driver.trigger.gprf.measurement.spectrum.get_timeout() \n
		No command help available \n
			:return: trigger_timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:SPECtrum:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, trigger_timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:SPECtrum:TOUT \n
		Snippet: driver.trigger.gprf.measurement.spectrum.set_timeout(trigger_timeout = 1.0) \n
		No command help available \n
			:param trigger_timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(trigger_timeout)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:SPECtrum:TOUT {param}')
