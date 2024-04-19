from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, index: int, modulation: bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:MODulation \n
		Snippet: driver.source.gprf.generator.listPy.modulation.set(index = 1, modulation = False) \n
		No command help available \n
			:param index: No help available
			:param modulation: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('modulation', modulation, DataType.Boolean))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:MODulation {param}'.rstrip())

	def get(self, index: int) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:MODulation \n
		Snippet: value: bool = driver.source.gprf.generator.listPy.modulation.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: modulation: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:LIST:MODulation? {param}')
		return Conversions.str_to_bool(response)

	def get_all(self) -> List[bool]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:MODulation:ALL \n
		Snippet: value: List[bool] = driver.source.gprf.generator.listPy.modulation.get_all() \n
		No command help available \n
			:return: all_modulations: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:MODulation:ALL?')
		return Conversions.str_to_bool_list(response)

	def set_all(self, all_modulations: List[bool]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:MODulation:ALL \n
		Snippet: driver.source.gprf.generator.listPy.modulation.set_all(all_modulations = [True, False, True]) \n
		No command help available \n
			:param all_modulations: No help available
		"""
		param = Conversions.list_to_csv_str(all_modulations)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:MODulation:ALL {param}')
