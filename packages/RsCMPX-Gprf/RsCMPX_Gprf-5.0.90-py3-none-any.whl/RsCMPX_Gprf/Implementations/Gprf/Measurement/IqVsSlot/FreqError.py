from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqErrorCls:
	"""FreqError commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("freqError", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:IQVSlot:FERRor \n
		Snippet: value: List[float] = driver.gprf.measurement.iqVsSlot.freqError.read() \n
		Returns the contents of the frequency error result diagram. \n
		Suppressed linked return values: reliability \n
			:return: frequency_error: Comma-separated list of frequency errors, one value per measured step"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:IQVSlot:FERRor?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:IQVSlot:FERRor \n
		Snippet: value: List[float] = driver.gprf.measurement.iqVsSlot.freqError.fetch() \n
		Returns the contents of the frequency error result diagram. \n
		Suppressed linked return values: reliability \n
			:return: frequency_error: Comma-separated list of frequency errors, one value per measured step"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:IQVSlot:FERRor?', suppressed)
		return response
