from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OfErrorCls:
	"""OfError commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ofError", core, parent)

	# noinspection PyTypeChecker
	def calculate(self) -> enums.ResultStatus2:
		"""SCPI: CALCulate:GPRF:MEASurement<Instance>:IQVSlot:OFERror \n
		Snippet: value: enums.ResultStatus2 = driver.gprf.measurement.iqVsSlot.ofError.calculate() \n
		Returns the overall frequency error. The values described below are returned by FETCh and READ commands.
		CALCulate commands return error codes instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: frequency_error: Overall frequency error, the arithmetic mean value of the frequency errors of all considered steps."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:GPRF:MEASurement<Instance>:IQVSlot:OFERror?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus2)

	def read(self) -> float:
		"""SCPI: READ:GPRF:MEASurement<Instance>:IQVSlot:OFERror \n
		Snippet: value: float = driver.gprf.measurement.iqVsSlot.ofError.read() \n
		Returns the overall frequency error. The values described below are returned by FETCh and READ commands.
		CALCulate commands return error codes instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: frequency_error: Overall frequency error, the arithmetic mean value of the frequency errors of all considered steps."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:GPRF:MEASurement<Instance>:IQVSlot:OFERror?', suppressed)
		return Conversions.str_to_float(response)

	def fetch(self) -> float:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:IQVSlot:OFERror \n
		Snippet: value: float = driver.gprf.measurement.iqVsSlot.ofError.fetch() \n
		Returns the overall frequency error. The values described below are returned by FETCh and READ commands.
		CALCulate commands return error codes instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: frequency_error: Overall frequency error, the arithmetic mean value of the frequency errors of all considered steps."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:GPRF:MEASurement<Instance>:IQVSlot:OFERror?', suppressed)
		return Conversions.str_to_float(response)
