from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TtimeCls:
	"""Ttime commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttime", core, parent)

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:TTIMe \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.listPy.ttime.get(index = 1) \n
		Queries the transition time for the sequencer list entry with the selected <Index>. \n
			:param index: No help available
			:return: trans_time: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:TTIMe? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:TTIMe:ALL \n
		Snippet: value: List[float] = driver.source.gprf.generator.sequencer.listPy.ttime.get_all() \n
		Queries the transition times for all sequencer list entries. \n
			:return: trans_time: Comma-separated list of values, one value per list entry
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:TTIMe:ALL?')
		return response
