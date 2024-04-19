from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbwCls:
	"""Rbw commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbw", core, parent)

	def get_auto(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW:AUTO \n
		Snippet: value: bool = driver.configure.gprf.measurement.spectrum.freqSweep.rbw.get_auto() \n
		No command help available \n
			:return: rbw_auto: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, rbw_auto: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW:AUTO \n
		Snippet: driver.configure.gprf.measurement.spectrum.freqSweep.rbw.set_auto(rbw_auto = False) \n
		No command help available \n
			:param rbw_auto: No help available
		"""
		param = Conversions.bool_to_str(rbw_auto)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW:AUTO {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW \n
		Snippet: value: float = driver.configure.gprf.measurement.spectrum.freqSweep.rbw.get_value() \n
		No command help available \n
			:return: rbw: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW?')
		return Conversions.str_to_float(response)

	def set_value(self, rbw: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW \n
		Snippet: driver.configure.gprf.measurement.spectrum.freqSweep.rbw.set_value(rbw = 1.0) \n
		No command help available \n
			:param rbw: No help available
		"""
		param = Conversions.decimal_value_to_str(rbw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW {param}')
