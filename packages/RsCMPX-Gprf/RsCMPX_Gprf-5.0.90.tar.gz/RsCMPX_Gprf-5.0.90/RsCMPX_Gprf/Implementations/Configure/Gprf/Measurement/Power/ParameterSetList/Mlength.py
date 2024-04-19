from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MlengthCls:
	"""Mlength commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mlength", core, parent)

	def set(self, index: int, meas_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth \n
		Snippet: driver.configure.gprf.measurement.power.parameterSetList.mlength.set(index = 1, meas_length = 1.0) \n
		Sets the length of the evaluation interval used to measure a single set of current power results for the parameter set
		<Index>. The measurement length cannot be greater than the step length. \n
			:param index: No help available
			:param meas_length: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('meas_length', meas_length, DataType.Float))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth \n
		Snippet: value: float = driver.configure.gprf.measurement.power.parameterSetList.mlength.get(index = 1) \n
		Sets the length of the evaluation interval used to measure a single set of current power results for the parameter set
		<Index>. The measurement length cannot be greater than the step length. \n
			:param index: No help available
			:return: meas_length: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth:ALL \n
		Snippet: value: List[float] = driver.configure.gprf.measurement.power.parameterSetList.mlength.get_all() \n
		Sets the length of the evaluation interval used to measure a single set of current power results, for all parameter sets.
		The measurement length cannot be greater than the step length. \n
			:return: meas_length: Comma-separated list of 32 values, for parameter set 0 to 31.
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth:ALL?')
		return response

	def set_all(self, meas_length: List[float]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth:ALL \n
		Snippet: driver.configure.gprf.measurement.power.parameterSetList.mlength.set_all(meas_length = [1.1, 2.2, 3.3]) \n
		Sets the length of the evaluation interval used to measure a single set of current power results, for all parameter sets.
		The measurement length cannot be greater than the step length. \n
			:param meas_length: Comma-separated list of 32 values, for parameter set 0 to 31.
		"""
		param = Conversions.list_to_csv_str(meas_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth:ALL {param}')
