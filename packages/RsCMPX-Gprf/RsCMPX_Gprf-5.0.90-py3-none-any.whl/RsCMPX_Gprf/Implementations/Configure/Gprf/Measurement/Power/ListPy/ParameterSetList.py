from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ParameterSetListCls:
	"""ParameterSetList commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("parameterSetList", core, parent)

	def set(self, index: int, parameter_set: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET \n
		Snippet: driver.configure.gprf.measurement.power.listPy.parameterSetList.set(index = 1, parameter_set = 1) \n
		Selects the parameter set for segment <Index>. \n
			:param index: No help available
			:param parameter_set: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('parameter_set', parameter_set, DataType.Integer))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET {param}'.rstrip())

	def get(self, index: int) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET \n
		Snippet: value: int = driver.configure.gprf.measurement.power.listPy.parameterSetList.get(index = 1) \n
		Selects the parameter set for segment <Index>. \n
			:param index: No help available
			:return: parameter_set: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET? {param}')
		return Conversions.str_to_int(response)

	def get_all(self) -> List[int]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET:ALL \n
		Snippet: value: List[int] = driver.configure.gprf.measurement.power.listPy.parameterSetList.get_all() \n
		Selects the parameter set for all segments. \n
			:return: parameter_set: Comma-separated list of parameter set numbers, one value per segment.
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET:ALL?')
		return response

	def set_all(self, parameter_set: List[int]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET:ALL \n
		Snippet: driver.configure.gprf.measurement.power.listPy.parameterSetList.set_all(parameter_set = [1, 2, 3]) \n
		Selects the parameter set for all segments. \n
			:param parameter_set: Comma-separated list of parameter set numbers, one value per segment.
		"""
		param = Conversions.list_to_csv_str(parameter_set)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET:ALL {param}')
