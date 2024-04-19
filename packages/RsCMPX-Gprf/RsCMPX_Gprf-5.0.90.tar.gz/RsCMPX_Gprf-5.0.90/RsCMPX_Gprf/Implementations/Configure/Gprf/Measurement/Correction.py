from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionCls:
	"""Correction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	def set(self, rx_corr_string: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CORR \n
		Snippet: driver.configure.gprf.measurement.correction.set(rx_corr_string = 'abc') \n
		No command help available \n
			:param rx_corr_string: No help available
		"""
		param = Conversions.value_to_quoted_str(rx_corr_string)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:CORR {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CORR \n
		Snippet: value: str = driver.configure.gprf.measurement.correction.get() \n
		No command help available \n
			:return: op_reply_code: No help available"""
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:CORR?')
		return trim_str_response(response)
