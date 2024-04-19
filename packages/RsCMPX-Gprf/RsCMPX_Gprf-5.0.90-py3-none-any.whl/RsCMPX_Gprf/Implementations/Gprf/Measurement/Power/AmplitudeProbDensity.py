from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmplitudeProbDensityCls:
	"""AmplitudeProbDensity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amplitudeProbDensity", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:APD \n
		Snippet: value: List[float] = driver.gprf.measurement.power.amplitudeProbDensity.fetch() \n
		Returns the APD diagram contents. \n
		Suppressed linked return values: reliability \n
			:return: results: 4096 results, each representing a 0.047-dB interval ('bin')"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:APD?', suppressed)
		return response
