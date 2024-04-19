from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZeroCls:
	"""Zero commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zero", core, parent)

	def set(self) -> None:
		"""SCPI: CALibration:GPRF:MEASurement<Instance>:EPSensor:ZERO \n
		Snippet: driver.calibration.gprf.measurement.extPwrSensor.zero.set() \n
		Initiates zeroing of the power sensor or reads the zeroing state. A running external power sensor measurement is
		interrupted and restarted after the zeroing procedure has been completed. Zeroing takes a few seconds (3 to 10) . \n
		Suppressed linked return values: reliability \n
		"""
		self._core.io.write(f'CALibration:GPRF:MEASurement<Instance>:EPSensor:ZERO')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALibration:GPRF:MEASurement<Instance>:EPSensor:ZERO \n
		Snippet: driver.calibration.gprf.measurement.extPwrSensor.zero.set_with_opc() \n
		Initiates zeroing of the power sensor or reads the zeroing state. A running external power sensor measurement is
		interrupted and restarted after the zeroing procedure has been completed. Zeroing takes a few seconds (3 to 10) . \n
		Suppressed linked return values: reliability \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Gprf.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALibration:GPRF:MEASurement<Instance>:EPSensor:ZERO', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get(self) -> enums.ZeroingState:
		"""SCPI: CALibration:GPRF:MEASurement<Instance>:EPSensor:ZERO \n
		Snippet: value: enums.ZeroingState = driver.calibration.gprf.measurement.extPwrSensor.zero.get() \n
		Initiates zeroing of the power sensor or reads the zeroing state. A running external power sensor measurement is
		interrupted and restarted after the zeroing procedure has been completed. Zeroing takes a few seconds (3 to 10) . \n
		Suppressed linked return values: reliability \n
			:return: zeroing_state: 'PASSed': The previous zeroing was successful. 'FAILed': The previous zeroing resulted in an error, e.g. because the signal power was not switched off."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALibration:GPRF:MEASurement<Instance>:EPSensor:ZERO?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ZeroingState)
