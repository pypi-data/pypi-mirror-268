from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqRecorderCls:
	"""IqRecorder commands group definition. 13 total commands, 5 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqRecorder", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def talignment(self):
		"""talignment commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_talignment'):
			from .Talignment import TalignmentCls
			self._talignment = TalignmentCls(self._core, self._cmd_group)
		return self._talignment

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def bin(self):
		"""bin commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bin'):
			from .Bin import BinCls
			self._bin = BinCls(self._core, self._cmd_group)
		return self._bin

	@property
	def reliability(self):
		"""reliability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reliability'):
			from .Reliability import ReliabilityCls
			self._reliability = ReliabilityCls(self._core, self._cmd_group)
		return self._reliability

	def initiate(self, save_to_iq_file: enums.FileSave = None) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:IQRecorder \n
		Snippet: driver.gprf.measurement.iqRecorder.initiate(save_to_iq_file = enums.FileSave.OFF) \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param save_to_iq_file: Optional parameter, selecting whether the results are written to an I/Q file, to the memory or both. For file selection, see method RsCMPX_Gprf.Configure.Gprf.Measurement.IqRecorder.iqFile. OFF: The results are only stored in the memory. ON: The results are stored in the memory and in a file. ONLY: The results are only stored in a file.
		"""
		param = ''
		if save_to_iq_file:
			param = Conversions.enum_scalar_to_str(save_to_iq_file, enums.FileSave)
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:IQRecorder {param}'.strip())

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:IQRecorder \n
		Snippet: driver.gprf.measurement.iqRecorder.abort() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:IQRecorder', opc_timeout_ms)

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:IQRecorder \n
		Snippet: driver.gprf.measurement.iqRecorder.stop() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:IQRecorder', opc_timeout_ms)

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:IQRecorder \n
		Snippet: value: List[float] = driver.gprf.measurement.iqRecorder.read() \n
		Returns the I and Q amplitudes in the format specified by FORMat:BASE:DATA. For a detailed description of the data
		formats, see 'ASCII and binary data formats'. For the number of values n, see method RsCMPX_Gprf.Configure.Gprf.
		Measurement.IqRecorder.Capture.set. \n
		Suppressed linked return values: reliability \n
			:return: iq_samples: For ASCII format: Comma-separated list of I and Q amplitudes {I, Q}1, ..., {I, Q}n For REAL format: Binary block data as listed in the table below. There are no commas within this parameter."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:IQRecorder?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:IQRecorder \n
		Snippet: value: List[float] = driver.gprf.measurement.iqRecorder.fetch() \n
		Returns the I and Q amplitudes in the format specified by FORMat:BASE:DATA. For a detailed description of the data
		formats, see 'ASCII and binary data formats'. For the number of values n, see method RsCMPX_Gprf.Configure.Gprf.
		Measurement.IqRecorder.Capture.set. \n
		Suppressed linked return values: reliability \n
			:return: iq_samples: For ASCII format: Comma-separated list of I and Q amplitudes {I, Q}1, ..., {I, Q}n For REAL format: Binary block data as listed in the table below. There are no commas within this parameter."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:IQRecorder?', suppressed)
		return response

	def clone(self) -> 'IqRecorderCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqRecorderCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
