from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, sensor=repcap.Sensor.Default) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:NRPM:SENSor<nr_NRPM>:FREQuency \n
		Snippet: driver.configure.gprf.measurement.nrpm.sensor.frequency.set(frequency = 1.0, sensor = repcap.Sensor.Default) \n
		Specifies the input frequency at the power sensor connected to Sensor <no>. \n
			:param frequency: No help available
			:param sensor: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sensor')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		sensor_cmd_val = self._cmd_group.get_repcap_cmd_value(sensor, repcap.Sensor)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:NRPM:SENSor{sensor_cmd_val}:FREQuency {param}')

	def get(self, sensor=repcap.Sensor.Default) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:NRPM:SENSor<nr_NRPM>:FREQuency \n
		Snippet: value: float = driver.configure.gprf.measurement.nrpm.sensor.frequency.get(sensor = repcap.Sensor.Default) \n
		Specifies the input frequency at the power sensor connected to Sensor <no>. \n
			:param sensor: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sensor')
			:return: frequency: No help available"""
		sensor_cmd_val = self._cmd_group.get_repcap_cmd_value(sensor, repcap.Sensor)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:NRPM:SENSor{sensor_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)
