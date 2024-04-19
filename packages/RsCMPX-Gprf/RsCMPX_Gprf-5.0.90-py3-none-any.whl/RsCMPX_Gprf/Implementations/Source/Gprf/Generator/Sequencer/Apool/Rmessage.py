from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmessageCls:
	"""Rmessage commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmessage", core, parent)

	def get_all(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RMESsage:ALL \n
		Snippet: value: List[str] = driver.source.gprf.generator.sequencer.apool.rmessage.get_all() \n
		Queries the reliability messages for all ARB files in the file pool. For possible values, see 'Reliability indicator'. \n
			:return: reliability_msg: Comma-separated list of strings One string per file, from index 0 to index n
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RMESsage:ALL?')
		return Conversions.str_to_str_list(response)

	def get(self, index: int) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RMESsage \n
		Snippet: value: str = driver.source.gprf.generator.sequencer.apool.rmessage.get(index = 1) \n
		Queries the reliability message for the ARB file with the specified <Index>. For possible values, see 'Reliability
		indicator'. \n
			:param index: No help available
			:return: reliability_msg: Reliability message"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RMESsage? {param}')
		return trim_str_response(response)
