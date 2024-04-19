from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqSettingsCls:
	"""IqSettings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqSettings", core, parent)

	def get_symbol_rate(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:IQSettings:SRATe \n
		Snippet: value: float = driver.configure.gprf.measurement.iqRecorder.iqSettings.get_symbol_rate() \n
		No command help available \n
			:return: sample_rate: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:IQSettings:SRATe?')
		return Conversions.str_to_float(response)

	def set_symbol_rate(self, sample_rate: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:IQSettings:SRATe \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.iqSettings.set_symbol_rate(sample_rate = 1.0) \n
		No command help available \n
			:param sample_rate: No help available
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:IQSettings:SRATe {param}')
