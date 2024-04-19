from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def get_mtime(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AUTO:MTIMe \n
		Snippet: value: float = driver.configure.gprf.measurement.extPwrSensor.auto.get_mtime() \n
		No command help available \n
			:return: meas_time: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:AUTO:MTIMe?')
		return Conversions.str_to_float(response)

	def set_mtime(self, meas_time: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AUTO:MTIMe \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.auto.set_mtime(meas_time = 1.0) \n
		No command help available \n
			:param meas_time: No help available
		"""
		param = Conversions.decimal_value_to_str(meas_time)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:AUTO:MTIMe {param}')

	def get_nsr(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AUTO:NSR \n
		Snippet: value: float = driver.configure.gprf.measurement.extPwrSensor.auto.get_nsr() \n
		No command help available \n
			:return: nsr: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:AUTO:NSR?')
		return Conversions.str_to_float(response)

	def set_nsr(self, nsr: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AUTO:NSR \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.auto.set_nsr(nsr = 1.0) \n
		No command help available \n
			:param nsr: No help available
		"""
		param = Conversions.decimal_value_to_str(nsr)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:AUTO:NSR {param}')
