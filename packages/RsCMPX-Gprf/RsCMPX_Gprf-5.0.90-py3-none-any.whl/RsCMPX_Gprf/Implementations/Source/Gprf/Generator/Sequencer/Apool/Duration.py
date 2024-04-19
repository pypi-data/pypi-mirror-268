from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DurationCls:
	"""Duration commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def get_all(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:DURation:ALL \n
		Snippet: value: List[float] = driver.source.gprf.generator.sequencer.apool.duration.get_all() \n
		Queries the durations of the ARB files in the file pool. \n
			:return: duration: Comma-separated list of values, one value per file
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:DURation:ALL?')
		return response

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:DURation \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.apool.duration.get(index = 1) \n
		Queries the duration of the ARB file with the specified <Index>. \n
			:param index: No help available
			:return: duration: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:DURation? {param}')
		return Conversions.str_to_float(response)
