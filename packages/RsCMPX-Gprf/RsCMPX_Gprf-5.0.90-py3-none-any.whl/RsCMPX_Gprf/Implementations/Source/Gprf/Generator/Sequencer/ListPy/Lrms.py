from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LrmsCls:
	"""Lrms commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrms", core, parent)

	def set(self, index: int, level_rms: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:LRMS \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.lrms.set(index = 1, level_rms = 1.0) \n
		Defines or queries the level for the sequencer list entry with the selected <Index>. \n
			:param index: No help available
			:param level_rms: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('level_rms', level_rms, DataType.Float))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:LRMS {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:LRMS \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.listPy.lrms.get(index = 1) \n
		Defines or queries the level for the sequencer list entry with the selected <Index>. \n
			:param index: No help available
			:return: level_rms: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:LRMS? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:LRMS:ALL \n
		Snippet: value: List[float] = driver.source.gprf.generator.sequencer.listPy.lrms.get_all() \n
		Defines the level for all sequencer list entries. \n
			:return: level_rms: Comma-separated list of values, one value per list entry
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:LRMS:ALL?')
		return response

	def set_all(self, level_rms: List[float]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:LRMS:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.lrms.set_all(level_rms = [1.1, 2.2, 3.3]) \n
		Defines the level for all sequencer list entries. \n
			:param level_rms: Comma-separated list of values, one value per list entry
		"""
		param = Conversions.list_to_csv_str(level_rms)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:LRMS:ALL {param}')
