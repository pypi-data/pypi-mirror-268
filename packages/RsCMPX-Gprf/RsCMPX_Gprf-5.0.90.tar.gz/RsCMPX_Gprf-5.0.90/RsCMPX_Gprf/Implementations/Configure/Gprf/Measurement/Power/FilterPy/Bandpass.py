from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandpassCls:
	"""Bandpass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandpass", core, parent)

	def get_bandwidth(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:BANDpass:BWIDth \n
		Snippet: value: float = driver.configure.gprf.measurement.power.filterPy.bandpass.get_bandwidth() \n
		Selects the bandwidth for a bandpass filter. \n
			:return: bandpass_bw: For allowed values, see Table 'Supported values'.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:BANDpass:BWIDth?')
		return Conversions.str_to_float(response)

	def set_bandwidth(self, bandpass_bw: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:BANDpass:BWIDth \n
		Snippet: driver.configure.gprf.measurement.power.filterPy.bandpass.set_bandwidth(bandpass_bw = 1.0) \n
		Selects the bandwidth for a bandpass filter. \n
			:param bandpass_bw: For allowed values, see Table 'Supported values'.
		"""
		param = Conversions.decimal_value_to_str(bandpass_bw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:BANDpass:BWIDth {param}')
