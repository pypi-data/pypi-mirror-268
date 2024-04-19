from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, index: int, bandwidth: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:BWIDth \n
		Snippet: driver.configure.gprf.measurement.power.parameterSetList.filterPy.bandwidth.set(index = 1, bandwidth = 1.0) \n
		No command help available \n
			:param index: No help available
			:param bandwidth: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('bandwidth', bandwidth, DataType.Float))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:BWIDth {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:BWIDth \n
		Snippet: value: float = driver.configure.gprf.measurement.power.parameterSetList.filterPy.bandwidth.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: bandwidth: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:BWIDth? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:BWIDth:ALL \n
		Snippet: value: List[float] = driver.configure.gprf.measurement.power.parameterSetList.filterPy.bandwidth.get_all() \n
		No command help available \n
			:return: bandwidth: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:BWIDth:ALL?')
		return response

	def set_all(self, bandwidth: List[float]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:BWIDth:ALL \n
		Snippet: driver.configure.gprf.measurement.power.parameterSetList.filterPy.bandwidth.set_all(bandwidth = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param bandwidth: No help available
		"""
		param = Conversions.list_to_csv_str(bandwidth)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:BWIDth:ALL {param}')
