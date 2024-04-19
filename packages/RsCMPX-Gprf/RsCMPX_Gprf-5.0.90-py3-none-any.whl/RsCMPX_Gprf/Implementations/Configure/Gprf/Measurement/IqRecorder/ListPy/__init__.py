from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 10 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def sstop(self):
		"""sstop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sstop'):
			from .Sstop import SstopCls
			self._sstop = SstopCls(self._core, self._cmd_group)
		return self._sstop

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_envelopePower'):
			from .EnvelopePower import EnvelopePowerCls
			self._envelopePower = EnvelopePowerCls(self._core, self._cmd_group)
		return self._envelopePower

	def get_slength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SLENgth \n
		Snippet: value: float = driver.configure.gprf.measurement.iqRecorder.listPy.get_slength() \n
		No command help available \n
			:return: step_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SLENgth?')
		return Conversions.str_to_float(response)

	def set_slength(self, step_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SLENgth \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.listPy.set_slength(step_length = 1.0) \n
		No command help available \n
			:param step_length: No help available
		"""
		param = Conversions.decimal_value_to_str(step_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SLENgth {param}')

	def get_count(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:COUNt \n
		Snippet: value: int = driver.configure.gprf.measurement.iqRecorder.listPy.get_count() \n
		No command help available \n
			:return: result_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def get_start(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STARt \n
		Snippet: value: int = driver.configure.gprf.measurement.iqRecorder.listPy.get_start() \n
		No command help available \n
			:return: start_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STARt \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.listPy.set_start(start_index = 1) \n
		No command help available \n
			:param start_index: No help available
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STOP \n
		Snippet: value: int = driver.configure.gprf.measurement.iqRecorder.listPy.get_stop() \n
		No command help available \n
			:return: stop_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STOP \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.listPy.set_stop(stop_index = 1) \n
		No command help available \n
			:param stop_index: No help available
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STOP {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST \n
		Snippet: value: bool = driver.configure.gprf.measurement.iqRecorder.listPy.get_value() \n
		No command help available \n
			:return: enable_list_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable_list_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.listPy.set_value(enable_list_mode = False) \n
		No command help available \n
			:param enable_list_mode: No help available
		"""
		param = Conversions.bool_to_str(enable_list_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST {param}')

	def clone(self) -> 'ListPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
