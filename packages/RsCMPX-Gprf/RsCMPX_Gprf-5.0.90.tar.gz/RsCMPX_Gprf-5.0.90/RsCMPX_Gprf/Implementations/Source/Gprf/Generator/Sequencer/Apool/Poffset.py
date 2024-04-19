from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoffsetCls:
	"""Poffset commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def get_all(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:POFFset:ALL \n
		Snippet: value: List[float] = driver.source.gprf.generator.sequencer.apool.poffset.get_all() \n
		Queries the peak offsets of the ARB files in the file pool. \n
			:return: peak_offset: Comma-separated list of values, one value per file
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:POFFset:ALL?')
		return response

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:POFFset \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.apool.poffset.get(index = 1) \n
		Queries the peak offset of the ARB file with the specified <Index>. \n
			:param index: No help available
			:return: peak_offset: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:POFFset? {param}')
		return Conversions.str_to_float(response)
