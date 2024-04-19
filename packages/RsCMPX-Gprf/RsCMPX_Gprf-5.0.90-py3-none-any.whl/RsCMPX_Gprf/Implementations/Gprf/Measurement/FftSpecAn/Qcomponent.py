from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QcomponentCls:
	"""Qcomponent commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qcomponent", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:FFTSanalyzer:Q \n
		Snippet: value: List[float] = driver.gprf.measurement.fftSpecAn.qcomponent.read() \n
		Returns the measured normalized I and Q amplitudes in the time domain. \n
		Suppressed linked return values: reliability \n
			:return: qdata: Comma-separated list of N normalized I or Q amplitudes. N equals the configured FFT length."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:FFTSanalyzer:Q?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:FFTSanalyzer:Q \n
		Snippet: value: List[float] = driver.gprf.measurement.fftSpecAn.qcomponent.fetch() \n
		Returns the measured normalized I and Q amplitudes in the time domain. \n
		Suppressed linked return values: reliability \n
			:return: qdata: Comma-separated list of N normalized I or Q amplitudes. N equals the configured FFT length."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:FFTSanalyzer:Q?', suppressed)
		return response
