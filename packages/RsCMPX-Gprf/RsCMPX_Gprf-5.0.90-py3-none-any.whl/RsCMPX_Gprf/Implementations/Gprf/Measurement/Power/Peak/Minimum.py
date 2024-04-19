from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum \n
		Snippet: value: List[enums.ResultStatus2] = driver.gprf.measurement.power.peak.minimum.calculate() \n
		Returns power results for all segments, see 'Results in list mode'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- Current RMS (...:POWer:CURRent?)
			- Current Min. (...:MINimum:CURRent?)
			- Current Max. (...:MAXimum:CURRent?)
			- Average RMS (...:AVERage?)
			- Minimum (...:PEAK:MINimum?)
			- Maximum (...:PEAK:MAXimum?)
			- Standard Deviation (...:SDEViation?)
		The values described below are returned by FETCh and READ commands. CALCulate commands return error codes instead, one
		value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: power_minimum_min: Comma-separated list of power values, one value per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum \n
		Snippet: value: List[float] = driver.gprf.measurement.power.peak.minimum.fetch() \n
		Returns power results for all segments, see 'Results in list mode'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- Current RMS (...:POWer:CURRent?)
			- Current Min. (...:MINimum:CURRent?)
			- Current Max. (...:MAXimum:CURRent?)
			- Average RMS (...:AVERage?)
			- Minimum (...:PEAK:MINimum?)
			- Maximum (...:PEAK:MAXimum?)
			- Standard Deviation (...:SDEViation?)
		The values described below are returned by FETCh and READ commands. CALCulate commands return error codes instead, one
		value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: power_minimum_min: Comma-separated list of power values, one value per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum \n
		Snippet: value: List[float] = driver.gprf.measurement.power.peak.minimum.read() \n
		Returns power results for all segments, see 'Results in list mode'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- Current RMS (...:POWer:CURRent?)
			- Current Min. (...:MINimum:CURRent?)
			- Current Max. (...:MAXimum:CURRent?)
			- Average RMS (...:AVERage?)
			- Minimum (...:PEAK:MINimum?)
			- Maximum (...:PEAK:MAXimum?)
			- Standard Deviation (...:SDEViation?)
		The values described below are returned by FETCh and READ commands. CALCulate commands return error codes instead, one
		value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: power_minimum_min: Comma-separated list of power values, one value per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum?', suppressed)
		return response
