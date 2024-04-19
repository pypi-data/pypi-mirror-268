from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, index: int, frequency: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FREQuency \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.frequency.set(index = 1, frequency = 1.0) \n
		Defines or queries the RF generator frequency for the sequencer list entry with the selected <Index>. For the supported
		frequency range, see 'Frequency ranges'. \n
			:param index: No help available
			:param frequency: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('frequency', frequency, DataType.Float))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FREQuency {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FREQuency \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.listPy.frequency.get(index = 1) \n
		Defines or queries the RF generator frequency for the sequencer list entry with the selected <Index>. For the supported
		frequency range, see 'Frequency ranges'. \n
			:param index: No help available
			:return: frequency: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FREQuency? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FREQuency:ALL \n
		Snippet: value: List[float] = driver.source.gprf.generator.sequencer.listPy.frequency.get_all() \n
		Defines the RF generator frequencies for all sequencer list entries. For the supported frequency range, see 'Frequency
		ranges'. \n
			:return: frequency: Comma-separated list of values, one value per list entry
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FREQuency:ALL?')
		return response

	def set_all(self, frequency: List[float]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FREQuency:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.frequency.set_all(frequency = [1.1, 2.2, 3.3]) \n
		Defines the RF generator frequencies for all sequencer list entries. For the supported frequency range, see 'Frequency
		ranges'. \n
			:param frequency: Comma-separated list of values, one value per list entry
		"""
		param = Conversions.list_to_csv_str(frequency)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FREQuency:ALL {param}')
