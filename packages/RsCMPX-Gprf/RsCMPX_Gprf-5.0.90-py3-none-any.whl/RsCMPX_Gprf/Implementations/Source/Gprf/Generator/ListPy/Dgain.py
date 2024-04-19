from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DgainCls:
	"""Dgain commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dgain", core, parent)

	def set(self, index: int, digital_gain: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:DGAin \n
		Snippet: driver.source.gprf.generator.listPy.dgain.set(index = 1, digital_gain = 1.0) \n
		No command help available \n
			:param index: No help available
			:param digital_gain: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('digital_gain', digital_gain, DataType.Float))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:DGAin {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:DGAin \n
		Snippet: value: float = driver.source.gprf.generator.listPy.dgain.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: digital_gain: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:LIST:DGAin? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:DGAin:ALL \n
		Snippet: value: List[float] = driver.source.gprf.generator.listPy.dgain.get_all() \n
		No command help available \n
			:return: all_digital_gains: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:LIST:DGAin:ALL?')
		return response

	def set_all(self, all_digital_gains: List[float]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:DGAin:ALL \n
		Snippet: driver.source.gprf.generator.listPy.dgain.set_all(all_digital_gains = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param all_digital_gains: No help available
		"""
		param = Conversions.list_to_csv_str(all_digital_gains)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:DGAin:ALL {param}')
