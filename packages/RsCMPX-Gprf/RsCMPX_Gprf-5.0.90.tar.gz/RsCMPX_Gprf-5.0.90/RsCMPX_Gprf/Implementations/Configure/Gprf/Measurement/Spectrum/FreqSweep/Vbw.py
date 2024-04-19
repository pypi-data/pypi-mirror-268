from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VbwCls:
	"""Vbw commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vbw", core, parent)

	def get_auto(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO \n
		Snippet: value: bool = driver.configure.gprf.measurement.spectrum.freqSweep.vbw.get_auto() \n
		No command help available \n
			:return: vbw_auto: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, vbw_auto: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO \n
		Snippet: driver.configure.gprf.measurement.spectrum.freqSweep.vbw.set_auto(vbw_auto = False) \n
		No command help available \n
			:param vbw_auto: No help available
		"""
		param = Conversions.bool_to_str(vbw_auto)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO {param}')

	def get_value(self) -> float or bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW \n
		Snippet: value: float or bool = driver.configure.gprf.measurement.spectrum.freqSweep.vbw.get_value() \n
		No command help available \n
			:return: vbw: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW?')
		return Conversions.str_to_float_or_bool(response)

	def set_value(self, vbw: float or bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW \n
		Snippet: driver.configure.gprf.measurement.spectrum.freqSweep.vbw.set_value(vbw = 1.0) \n
		No command help available \n
			:param vbw: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(vbw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW {param}')
