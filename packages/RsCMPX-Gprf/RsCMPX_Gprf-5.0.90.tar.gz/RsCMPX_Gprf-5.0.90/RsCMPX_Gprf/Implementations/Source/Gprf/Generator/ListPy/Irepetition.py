from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IrepetitionCls:
	"""Irepetition commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("irepetition", core, parent)

	def set(self, index: int, repetition: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:IREPetition \n
		Snippet: driver.source.gprf.generator.listPy.irepetition.set(index = 1, repetition = 1) \n
		No command help available \n
			:param index: No help available
			:param repetition: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('repetition', repetition, DataType.Integer))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:IREPetition {param}'.rstrip())

	def get(self, index: int) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:IREPetition \n
		Snippet: value: int = driver.source.gprf.generator.listPy.irepetition.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: repetition: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:LIST:IREPetition? {param}')
		return Conversions.str_to_int(response)

	def get_all(self) -> List[int]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:IREPetition:ALL \n
		Snippet: value: List[int] = driver.source.gprf.generator.listPy.irepetition.get_all() \n
		No command help available \n
			:return: index_repetitions: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SOURce:GPRF:GENerator<Instance>:LIST:IREPetition:ALL?')
		return response

	def set_all(self, index_repetitions: List[int]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:IREPetition:ALL \n
		Snippet: driver.source.gprf.generator.listPy.irepetition.set_all(index_repetitions = [1, 2, 3]) \n
		No command help available \n
			:param index_repetitions: No help available
		"""
		param = Conversions.list_to_csv_str(index_repetitions)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:IREPetition:ALL {param}')
