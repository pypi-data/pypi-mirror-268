from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfLevelCls:
	"""RfLevel commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfLevel", core, parent)

	def set(self, index: int, level: float or bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:RFLevel \n
		Snippet: driver.source.gprf.generator.listPy.rfLevel.set(index = 1, level = 1.0) \n
		No command help available \n
			:param index: No help available
			:param level: (float or boolean) No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('level', level, DataType.FloatExt))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:RFLevel {param}'.rstrip())

	def get(self, index: int) -> float or bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:RFLevel \n
		Snippet: value: float or bool = driver.source.gprf.generator.listPy.rfLevel.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: level: (float or boolean) No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:LIST:RFLevel? {param}')
		return Conversions.str_to_float_or_bool(response)

	def get_all(self) -> List[float or bool]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:RFLevel:ALL \n
		Snippet: value: List[float or bool] = driver.source.gprf.generator.listPy.rfLevel.get_all() \n
		No command help available \n
			:return: all_levels: (float or boolean items) No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:RFLevel:ALL?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_all(self, all_levels: List[float or bool]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:RFLevel:ALL \n
		Snippet: driver.source.gprf.generator.listPy.rfLevel.set_all(all_levels = [1.1, True, 2.2, False, 3.3]) \n
		No command help available \n
			:param all_levels: (float or boolean items) No help available
		"""
		param = Conversions.list_to_csv_str(all_levels)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:RFLevel:ALL {param}')
