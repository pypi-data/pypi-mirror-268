from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProbabilityCls:
	"""Probability commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("probability", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:PROBability \n
		Snippet: value: List[float] = driver.gprf.measurement.power.cumulativeDistribFnc.probability.fetch() \n
		Returns power values with a certain probability, taken from the CCDF diagram. \n
		Suppressed linked return values: reliability \n
			:return: probability: Comma-separated list of 6 power values with the following probabilities: 10 %, 1 %, 0.1 %, 0.01 %, 0.001 %, 0.0001 % The power values are indicated in dB relative to the average power."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:PROBability?', suppressed)
		return response
