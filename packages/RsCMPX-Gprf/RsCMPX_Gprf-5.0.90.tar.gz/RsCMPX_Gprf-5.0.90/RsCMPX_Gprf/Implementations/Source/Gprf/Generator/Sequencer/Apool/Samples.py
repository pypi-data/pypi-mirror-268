from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SamplesCls:
	"""Samples commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("samples", core, parent)

	def get_all(self) -> List[int]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:SAMPles:ALL \n
		Snippet: value: List[int] = driver.source.gprf.generator.sequencer.apool.samples.get_all() \n
		Queries the numbers of samples in the ARB files of the file pool. \n
			:return: samples: Comma-separated list of values, one value per file
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:SAMPles:ALL?')
		return response

	def get(self, index: int) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:SAMPles \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.apool.samples.get(index = 1) \n
		Queries the number of samples in the ARB file with the specified <Index>. \n
			:param index: No help available
			:return: samples: Number of samples"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:SAMPles? {param}')
		return Conversions.str_to_int(response)
