from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IrepetitionCls:
	"""Irepetition commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("irepetition", core, parent)

	def set(self, index: int, repetition: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IREPetition \n
		Snippet: driver.configure.gprf.measurement.power.listPy.irepetition.set(index = 1, repetition = 1) \n
		Configures the number of repetitions of segment <Index>. The total number of repetitions over all measured segments must
		not be higher than 10000. \n
			:param index: No help available
			:param repetition: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('repetition', repetition, DataType.Integer))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IREPetition {param}'.rstrip())

	def get(self, index: int) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IREPetition \n
		Snippet: value: int = driver.configure.gprf.measurement.power.listPy.irepetition.get(index = 1) \n
		Configures the number of repetitions of segment <Index>. The total number of repetitions over all measured segments must
		not be higher than 10000. \n
			:param index: No help available
			:return: repetition: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IREPetition? {param}')
		return Conversions.str_to_int(response)

	def get_all(self) -> List[int]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IREPetition:ALL \n
		Snippet: value: List[int] = driver.configure.gprf.measurement.power.listPy.irepetition.get_all() \n
		Configures the number of repetitions for all segments. The total number of repetitions over all measured segments must
		not be higher than 10000. \n
			:return: repetition: Comma-separated list of repetitions, one value per segment
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IREPetition:ALL?')
		return response

	def set_all(self, repetition: List[int]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IREPetition:ALL \n
		Snippet: driver.configure.gprf.measurement.power.listPy.irepetition.set_all(repetition = [1, 2, 3]) \n
		Configures the number of repetitions for all segments. The total number of repetitions over all measured segments must
		not be higher than 10000. \n
			:param repetition: Comma-separated list of repetitions, one value per segment
		"""
		param = Conversions.list_to_csv_str(repetition)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IREPetition:ALL {param}')
