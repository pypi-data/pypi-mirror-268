from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, index: int, trigger_offset: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:PSET:OFFSet \n
		Snippet: driver.trigger.gprf.measurement.power.parameterSetList.offset.set(index = 1, trigger_offset = 1.0) \n
		Defines a delay time relative to the trigger event for the parameter set <Index>. \n
			:param index: No help available
			:param trigger_offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('trigger_offset', trigger_offset, DataType.Float))
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:POWer:PSET:OFFSet {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:PSET:OFFSet \n
		Snippet: value: float = driver.trigger.gprf.measurement.power.parameterSetList.offset.get(index = 1) \n
		Defines a delay time relative to the trigger event for the parameter set <Index>. \n
			:param index: No help available
			:return: trigger_offset: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'TRIGger:GPRF:MEASurement<Instance>:POWer:PSET:OFFSet? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:PSET:OFFSet:ALL \n
		Snippet: value: List[float] = driver.trigger.gprf.measurement.power.parameterSetList.offset.get_all() \n
		Defines a delay time relative to the trigger event for all parameter sets. \n
			:return: trigger_offset: Comma-separated list of 32 offsets, for parameter set 0 to 31.
		"""
		response = self._core.io.query_bin_or_ascii_float_list('TRIGger:GPRF:MEASurement<Instance>:POWer:PSET:OFFSet:ALL?')
		return response

	def set_all(self, trigger_offset: List[float]) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:POWer:PSET:OFFSet:ALL \n
		Snippet: driver.trigger.gprf.measurement.power.parameterSetList.offset.set_all(trigger_offset = [1.1, 2.2, 3.3]) \n
		Defines a delay time relative to the trigger event for all parameter sets. \n
			:param trigger_offset: Comma-separated list of 32 offsets, for parameter set 0 to 31.
		"""
		param = Conversions.list_to_csv_str(trigger_offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:POWer:PSET:OFFSet:ALL {param}')
