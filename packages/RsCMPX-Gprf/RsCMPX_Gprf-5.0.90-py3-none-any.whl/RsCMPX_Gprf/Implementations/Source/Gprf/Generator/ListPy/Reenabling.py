from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReenablingCls:
	"""Reenabling commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reenabling", core, parent)

	def set(self, index: int, reenabling: bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:REENabling \n
		Snippet: driver.source.gprf.generator.listPy.reenabling.set(index = 1, reenabling = False) \n
		No command help available \n
			:param index: No help available
			:param reenabling: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('reenabling', reenabling, DataType.Boolean))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:REENabling {param}'.rstrip())

	def get(self, index: int) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:REENabling \n
		Snippet: value: bool = driver.source.gprf.generator.listPy.reenabling.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: reenabling: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:LIST:REENabling? {param}')
		return Conversions.str_to_bool(response)

	def get_all(self) -> List[bool]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:REENabling:ALL \n
		Snippet: value: List[bool] = driver.source.gprf.generator.listPy.reenabling.get_all() \n
		No command help available \n
			:return: all_reenables: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:REENabling:ALL?')
		return Conversions.str_to_bool_list(response)

	def set_all(self, all_reenables: List[bool]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:REENabling:ALL \n
		Snippet: driver.source.gprf.generator.listPy.reenabling.set_all(all_reenables = [True, False, True]) \n
		No command help available \n
			:param all_reenables: No help available
		"""
		param = Conversions.list_to_csv_str(all_reenables)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:REENabling:ALL {param}')
