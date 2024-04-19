from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GaussCls:
	"""Gauss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gauss", core, parent)

	def get_bandwidth(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:GAUSs:BWIDth \n
		Snippet: value: float = driver.configure.gprf.measurement.power.filterPy.gauss.get_bandwidth() \n
		Selects the bandwidth for a filter of Gaussian shape. \n
			:return: gauss_bw: For allowed values, see Table 'Supported values'.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:GAUSs:BWIDth?')
		return Conversions.str_to_float(response)

	def set_bandwidth(self, gauss_bw: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:GAUSs:BWIDth \n
		Snippet: driver.configure.gprf.measurement.power.filterPy.gauss.set_bandwidth(gauss_bw = 1.0) \n
		Selects the bandwidth for a filter of Gaussian shape. \n
			:param gauss_bw: For allowed values, see Table 'Supported values'.
		"""
		param = Conversions.decimal_value_to_str(gauss_bw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:GAUSs:BWIDth {param}')
