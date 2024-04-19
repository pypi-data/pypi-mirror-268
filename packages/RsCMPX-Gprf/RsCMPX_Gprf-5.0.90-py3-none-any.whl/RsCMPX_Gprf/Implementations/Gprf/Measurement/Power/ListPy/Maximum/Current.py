from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	def calculate(self, list_index: int) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:GPRF:MEASurement<Instance>:POWer:LIST:MAXimum:CURRent \n
		Snippet: value: List[enums.ResultStatus2] = driver.gprf.measurement.power.listPy.maximum.current.calculate(list_index = 1) \n
		Returns power results for segment <ListIndex>, see 'Results in list mode'.
			INTRO_CMD_HELP: The following powers can be retrieved: \n
			- Current RMS (...:LIST:CURRent?)
			- Current Min. (...:MINimum:CURRent?)
			- Current Max. (...:MAXimum:CURRent?)
			- Average RMS (...:AVERage?)
			- Minimum (...:PEAK:MINimum?)
			- Maximum (...:PEAK:MAXimum?)
			- Standard Deviation (...:SDEViation?)
		The values described below are returned by FETCh and READ commands. CALCulate commands return error codes instead, one
		value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param list_index: Index of the segment
			:return: power_current_max: Power value for the selected segment"""
		param = Conversions.decimal_value_to_str(list_index)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:GPRF:MEASurement<Instance>:POWer:LIST:MAXimum:CURRent? {param}', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)

	def fetch(self, list_index: int) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:LIST:MAXimum:CURRent \n
		Snippet: value: List[float] = driver.gprf.measurement.power.listPy.maximum.current.fetch(list_index = 1) \n
		Returns power results for segment <ListIndex>, see 'Results in list mode'.
			INTRO_CMD_HELP: The following powers can be retrieved: \n
			- Current RMS (...:LIST:CURRent?)
			- Current Min. (...:MINimum:CURRent?)
			- Current Max. (...:MAXimum:CURRent?)
			- Average RMS (...:AVERage?)
			- Minimum (...:PEAK:MINimum?)
			- Maximum (...:PEAK:MAXimum?)
			- Standard Deviation (...:SDEViation?)
		The values described below are returned by FETCh and READ commands. CALCulate commands return error codes instead, one
		value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param list_index: Index of the segment
			:return: power_current_max: Power value for the selected segment"""
		param = Conversions.decimal_value_to_str(list_index)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:LIST:MAXimum:CURRent? {param}', suppressed)
		return response

	def read(self, list_index: int) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:POWer:LIST:MAXimum:CURRent \n
		Snippet: value: List[float] = driver.gprf.measurement.power.listPy.maximum.current.read(list_index = 1) \n
		Returns power results for segment <ListIndex>, see 'Results in list mode'.
			INTRO_CMD_HELP: The following powers can be retrieved: \n
			- Current RMS (...:LIST:CURRent?)
			- Current Min. (...:MINimum:CURRent?)
			- Current Max. (...:MAXimum:CURRent?)
			- Average RMS (...:AVERage?)
			- Minimum (...:PEAK:MINimum?)
			- Maximum (...:PEAK:MAXimum?)
			- Standard Deviation (...:SDEViation?)
		The values described below are returned by FETCh and READ commands. CALCulate commands return error codes instead, one
		value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param list_index: Index of the segment
			:return: power_current_max: Power value for the selected segment"""
		param = Conversions.decimal_value_to_str(list_index)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:LIST:MAXimum:CURRent? {param}', suppressed)
		return response
