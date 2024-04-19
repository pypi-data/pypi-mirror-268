from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:FFTSanalyzer:POWer:AVERage \n
		Snippet: value: List[float] = driver.gprf.measurement.fftSpecAn.power.average.fetch() \n
		Returns the traces of the spectrum diagram. The current, average, minimum and maximum traces can be retrieved. Each trace
		contains 801 power values and covers the configured frequency span. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of 801 power values"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:FFTSanalyzer:POWer:AVERage?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:FFTSanalyzer:POWer:AVERage \n
		Snippet: value: List[float] = driver.gprf.measurement.fftSpecAn.power.average.read() \n
		Returns the traces of the spectrum diagram. The current, average, minimum and maximum traces can be retrieved. Each trace
		contains 801 power values and covers the configured frequency span. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of 801 power values"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:FFTSanalyzer:POWer:AVERage?', suppressed)
		return response
