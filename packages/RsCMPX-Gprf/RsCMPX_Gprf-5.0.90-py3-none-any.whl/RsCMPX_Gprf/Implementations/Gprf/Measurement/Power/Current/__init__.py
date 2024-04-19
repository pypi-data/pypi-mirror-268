from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 9 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	@property
	def rms(self):
		"""rms commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import RmsCls
			self._rms = RmsCls(self._core, self._cmd_group)
		return self._rms

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:GPRF:MEASurement<Instance>:POWer:CURRent \n
		Snippet: value: List[enums.ResultStatus2] = driver.gprf.measurement.power.current.calculate() \n
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
			:return: power_current_rms: Comma-separated list of power values, one value per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:GPRF:MEASurement<Instance>:POWer:CURRent?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CURRent \n
		Snippet: value: List[float] = driver.gprf.measurement.power.current.fetch() \n
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
			:return: power_current_rms: Comma-separated list of power values, one value per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:POWer:CURRent \n
		Snippet: value: List[float] = driver.gprf.measurement.power.current.read() \n
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
			:return: power_current_rms: Comma-separated list of power values, one value per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:CURRent?', suppressed)
		return response

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
