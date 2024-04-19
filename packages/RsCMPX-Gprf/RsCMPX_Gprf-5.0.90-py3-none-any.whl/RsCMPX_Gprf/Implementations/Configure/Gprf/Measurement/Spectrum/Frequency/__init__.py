from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 6 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def span(self):
		"""span commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_span'):
			from .Span import SpanCls
			self._span = SpanCls(self._core, self._cmd_group)
		return self._span

	def get_center(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:CENTer \n
		Snippet: value: float = driver.configure.gprf.measurement.spectrum.frequency.get_center() \n
		No command help available \n
			:return: center_frequency: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:CENTer?')
		return Conversions.str_to_float(response)

	def set_center(self, center_frequency: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:CENTer \n
		Snippet: driver.configure.gprf.measurement.spectrum.frequency.set_center(center_frequency = 1.0) \n
		No command help available \n
			:param center_frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(center_frequency)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:CENTer {param}')

	def get_start(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STARt \n
		Snippet: value: float = driver.configure.gprf.measurement.spectrum.frequency.get_start() \n
		No command help available \n
			:return: start_frequency: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, start_frequency: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STARt \n
		Snippet: driver.configure.gprf.measurement.spectrum.frequency.set_start(start_frequency = 1.0) \n
		No command help available \n
			:param start_frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(start_frequency)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STARt {param}')

	def get_stop(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STOP \n
		Snippet: value: float = driver.configure.gprf.measurement.spectrum.frequency.get_stop() \n
		No command help available \n
			:return: stop_frequency: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STOP?')
		return Conversions.str_to_float(response)

	def set_stop(self, stop_frequency: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STOP \n
		Snippet: driver.configure.gprf.measurement.spectrum.frequency.set_stop(stop_frequency = 1.0) \n
		No command help available \n
			:param stop_frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(stop_frequency)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STOP {param}')

	def get_laspan(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:LASPan \n
		Snippet: value: float = driver.configure.gprf.measurement.spectrum.frequency.get_laspan() \n
		No command help available \n
			:return: last_span: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:LASPan?')
		return Conversions.str_to_float(response)

	def set_laspan(self, last_span: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:LASPan \n
		Snippet: driver.configure.gprf.measurement.spectrum.frequency.set_laspan(last_span = 1.0) \n
		No command help available \n
			:param last_span: No help available
		"""
		param = Conversions.decimal_value_to_str(last_span)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:LASPan {param}')

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
