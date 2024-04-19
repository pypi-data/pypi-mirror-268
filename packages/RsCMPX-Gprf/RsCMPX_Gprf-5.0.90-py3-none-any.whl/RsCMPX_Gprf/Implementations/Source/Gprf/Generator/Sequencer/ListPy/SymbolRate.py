from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRateCls:
	"""SymbolRate commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SRATe \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.listPy.symbolRate.get(index = 1) \n
		Queries the sample rate for the sequencer list entry with the selected <Index>. \n
			:param index: No help available
			:return: sample_rate: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SRATe? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SRATe:ALL \n
		Snippet: value: List[float] = driver.source.gprf.generator.sequencer.listPy.symbolRate.get_all() \n
		Queries the sample rates for all sequencer list entries. \n
			:return: sample_rate: Comma-separated list of values, one value per list entry
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SRATe:ALL?')
		return response
