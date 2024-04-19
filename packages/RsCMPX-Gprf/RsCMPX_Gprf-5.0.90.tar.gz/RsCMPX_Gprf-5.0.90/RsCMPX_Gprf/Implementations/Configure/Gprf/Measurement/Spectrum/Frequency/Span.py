from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpanCls:
	"""Span commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("span", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SpanMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN:MODE \n
		Snippet: value: enums.SpanMode = driver.configure.gprf.measurement.spectrum.frequency.span.get_mode() \n
		No command help available \n
			:return: span_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SpanMode)

	def set_mode(self, span_mode: enums.SpanMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN:MODE \n
		Snippet: driver.configure.gprf.measurement.spectrum.frequency.span.set_mode(span_mode = enums.SpanMode.FSWeep) \n
		No command help available \n
			:param span_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(span_mode, enums.SpanMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN \n
		Snippet: value: float = driver.configure.gprf.measurement.spectrum.frequency.span.get_value() \n
		No command help available \n
			:return: frequency_span: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN?')
		return Conversions.str_to_float(response)

	def set_value(self, frequency_span: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN \n
		Snippet: driver.configure.gprf.measurement.spectrum.frequency.span.set_value(frequency_span = 1.0) \n
		No command help available \n
			:param frequency_span: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency_span)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN {param}')
