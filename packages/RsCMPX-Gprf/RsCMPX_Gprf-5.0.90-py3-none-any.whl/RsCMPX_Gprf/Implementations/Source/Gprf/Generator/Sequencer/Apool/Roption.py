from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RoptionCls:
	"""Roption commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("roption", core, parent)

	def get_all(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:ROPTion:ALL \n
		Snippet: value: List[str] = driver.source.gprf.generator.sequencer.apool.roption.get_all() \n
		Queries the options required by the ARB files in the file pool. \n
			:return: required_options: Comma-separated list of strings, one string per file
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:ROPTion:ALL?')
		return Conversions.str_to_str_list(response)

	def get(self, index: int) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:ROPTion \n
		Snippet: value: str = driver.source.gprf.generator.sequencer.apool.roption.get(index = 1) \n
		Queries the options required by the ARB file with the specified <Index>. \n
			:param index: No help available
			:return: required_options: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:ROPTion? {param}')
		return trim_str_response(response)
