from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsegmentCls:
	"""Msegment commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msegment", core, parent)

	def get_name(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:NAME \n
		Snippet: value: List[str] = driver.source.gprf.generator.arb.msegment.get_name() \n
		No command help available \n
			:return: name: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:NAME?')
		return Conversions.str_to_str_list(response)

	def get_poffset(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:POFFset \n
		Snippet: value: List[float] = driver.source.gprf.generator.arb.msegment.get_poffset() \n
		No command help available \n
			:return: peak_offset: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:POFFset?')
		return response

	def get_par(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:PAR \n
		Snippet: value: List[float] = driver.source.gprf.generator.arb.msegment.get_par() \n
		No command help available \n
			:return: par: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:PAR?')
		return response

	def get_duration(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:DURation \n
		Snippet: value: List[float] = driver.source.gprf.generator.arb.msegment.get_duration() \n
		No command help available \n
			:return: duration: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:DURation?')
		return response

	def get_samples(self) -> List[int]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:SAMPles \n
		Snippet: value: List[int] = driver.source.gprf.generator.arb.msegment.get_samples() \n
		No command help available \n
			:return: samples: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:SAMPles?')
		return response

	def get_crate(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:CRATe \n
		Snippet: value: List[float] = driver.source.gprf.generator.arb.msegment.get_crate() \n
		No command help available \n
			:return: clock_rate: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:CRATe?')
		return response

	def get_number(self) -> List[int]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:NUMBer \n
		Snippet: value: List[int] = driver.source.gprf.generator.arb.msegment.get_number() \n
		No command help available \n
			:return: seg_number: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SOURce:GPRF:GENerator<Instance>:ARB:MSEGment:NUMBer?')
		return response
