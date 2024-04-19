from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtPwrSensorCls:
	"""ExtPwrSensor commands group definition. 8 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extPwrSensor", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:EPSensor \n
		Snippet: driver.gprf.measurement.extPwrSensor.initiate() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:EPSensor', opc_timeout_ms)

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:EPSensor \n
		Snippet: driver.gprf.measurement.extPwrSensor.stop() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:EPSensor', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:EPSensor \n
		Snippet: driver.gprf.measurement.extPwrSensor.abort() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:EPSensor', opc_timeout_ms)

	def get_idn(self) -> str:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:EPSensor:IDN \n
		Snippet: value: str = driver.gprf.measurement.extPwrSensor.get_idn() \n
		Returns the identification string of the connected external sensor. \n
			:return: idn: No help available
		"""
		response = self._core.io.query_str('FETCh:GPRF:MEASurement<Instance>:EPSensor:IDN?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Current_Power: float: No parameter help available
			- Average_Power: float: No parameter help available
			- Minimum_Power: float: No parameter help available
			- Maximum_Power: float: No parameter help available
			- Elapsed_Stat: int: Elapsed measurement cycles"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Current_Power'),
			ArgStruct.scalar_float('Average_Power'),
			ArgStruct.scalar_float('Minimum_Power'),
			ArgStruct.scalar_float('Maximum_Power'),
			ArgStruct.scalar_int('Elapsed_Stat')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Current_Power: float = None
			self.Average_Power: float = None
			self.Minimum_Power: float = None
			self.Maximum_Power: float = None
			self.Elapsed_Stat: int = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:EPSensor \n
		Snippet: value: ResultData = driver.gprf.measurement.extPwrSensor.fetch() \n
		Returns all results of the EPS measurement. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:EPSensor?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:GPRF:MEASurement<Instance>:EPSensor \n
		Snippet: value: ResultData = driver.gprf.measurement.extPwrSensor.read() \n
		Returns all results of the EPS measurement. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GPRF:MEASurement<Instance>:EPSensor?', self.__class__.ResultData())

	def clone(self) -> 'ExtPwrSensorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ExtPwrSensorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
