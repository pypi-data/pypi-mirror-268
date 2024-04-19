from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReliabilityCls:
	"""Reliability commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reliability", core, parent)

	def get_all(self) -> List[int]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RELiability:ALL \n
		Snippet: value: List[int] = driver.source.gprf.generator.sequencer.apool.reliability.get_all() \n
		Queries the reliability indicators for all ARB files in the file pool. For possible values, see 'Reliability indicator'. \n
			:return: reliability: Comma-separated list of values One value per file, from index 0 to index n
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RELiability:ALL?')
		return response

	def get(self, index: int) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RELiability \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.apool.reliability.get(index = 1) \n
		Queries the reliability indicator for the ARB file with the specified <Index>. For possible values, see 'Reliability
		indicator'. \n
			:param index: No help available
			:return: reliability: Reliability indicator"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RELiability? {param}')
		return Conversions.str_to_int(response)
