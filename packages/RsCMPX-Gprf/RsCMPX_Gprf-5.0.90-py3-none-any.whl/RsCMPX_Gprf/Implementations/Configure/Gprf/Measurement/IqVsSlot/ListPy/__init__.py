from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 11 total commands, 4 Subgroups, 4 group commands"""

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

	@property
	def retrigger(self):
		"""retrigger commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_retrigger'):
			from .Retrigger import RetriggerCls
			self._retrigger = RetriggerCls(self._core, self._cmd_group)
		return self._retrigger

	def get_start(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STARt \n
		Snippet: value: int = driver.configure.gprf.measurement.iqVsSlot.listPy.get_start() \n
		Selects the first subsweep to be measured. The <StartIndex> must not be greater than the <StopIndex>. The total number of
		steps must not exceed 3000 (step count times number of subsweeps) . \n
			:return: start_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STARt \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.listPy.set_start(start_index = 1) \n
		Selects the first subsweep to be measured. The <StartIndex> must not be greater than the <StopIndex>. The total number of
		steps must not exceed 3000 (step count times number of subsweeps) . \n
			:param start_index: No help available
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STOP \n
		Snippet: value: int = driver.configure.gprf.measurement.iqVsSlot.listPy.get_stop() \n
		Selects the last subsweep to be measured. The <StopIndex> must not be smaller than the <StartIndex>. The total number of
		steps must not exceed 3000 (step count times number of subsweeps) . \n
			:return: stop_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STOP \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.listPy.set_stop(stop_index = 1) \n
		Selects the last subsweep to be measured. The <StopIndex> must not be smaller than the <StartIndex>. The total number of
		steps must not exceed 3000 (step count times number of subsweeps) . \n
			:param stop_index: No help available
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STOP {param}')

	def get_count(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:COUNt \n
		Snippet: value: int = driver.configure.gprf.measurement.iqVsSlot.listPy.get_count() \n
		Queries the number of subsweeps per sweep. The total number of steps must not exceed 3000 (step count times number of
		subsweeps) . \n
			:return: sweep_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def get_value(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST \n
		Snippet: value: bool = driver.configure.gprf.measurement.iqVsSlot.listPy.get_value() \n
		Enables or disables the list mode for the I/Q vs slot measurement. \n
			:return: list_mode: OFF: list mode off ON: list mode on
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, list_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.listPy.set_value(list_mode = False) \n
		Enables or disables the list mode for the I/Q vs slot measurement. \n
			:param list_mode: OFF: list mode off ON: list mode on
		"""
		param = Conversions.bool_to_str(list_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST {param}')

	def clone(self) -> 'ListPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
