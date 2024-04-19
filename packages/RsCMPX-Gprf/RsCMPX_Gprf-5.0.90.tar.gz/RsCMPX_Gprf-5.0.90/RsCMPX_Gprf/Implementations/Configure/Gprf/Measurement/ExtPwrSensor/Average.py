from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ExtPwrSensorAvgMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:MODE \n
		Snippet: value: enums.ExtPwrSensorAvgMode = driver.configure.gprf.measurement.extPwrSensor.average.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ExtPwrSensorAvgMode)

	def set_mode(self, mode: enums.ExtPwrSensorAvgMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:MODE \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.average.set_mode(mode = enums.ExtPwrSensorAvgMode.MANual) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ExtPwrSensorAvgMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:MODE {param}')

	def get_count(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:COUNt \n
		Snippet: value: int = driver.configure.gprf.measurement.extPwrSensor.average.get_count() \n
		No command help available \n
			:return: average_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, average_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:COUNt \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.average.set_count(average_count = 1) \n
		No command help available \n
			:param average_count: No help available
		"""
		param = Conversions.decimal_value_to_str(average_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:COUNt {param}')

	def get_aperture(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:APERture \n
		Snippet: value: float = driver.configure.gprf.measurement.extPwrSensor.average.get_aperture() \n
		No command help available \n
			:return: aperture: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:APERture?')
		return Conversions.str_to_float(response)

	def set_aperture(self, aperture: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:APERture \n
		Snippet: driver.configure.gprf.measurement.extPwrSensor.average.set_aperture(aperture = 1.0) \n
		No command help available \n
			:param aperture: No help available
		"""
		param = Conversions.decimal_value_to_str(aperture)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:AVERage:APERture {param}')
