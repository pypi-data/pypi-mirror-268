from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Power_Antenna_1: float: Power measured at antenna 1 of the sensor
			- Power_Antenna_2: float: Power measured at antenna 2 of the sensor
			- Power_Antenna_3: float: Power measured at antenna 3 of the sensor"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Power_Antenna_1'),
			ArgStruct.scalar_float('Power_Antenna_2'),
			ArgStruct.scalar_float('Power_Antenna_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Power_Antenna_1: float = None
			self.Power_Antenna_2: float = None
			self.Power_Antenna_3: float = None

	def read(self, sensor=repcap.Sensor.Default) -> ResultData:
		"""SCPI: READ:GPRF:MEASurement<Instance>:NRPM:SENSor<nr_NRPM>:POWer \n
		Snippet: value: ResultData = driver.gprf.measurement.nrpm.sensor.power.read(sensor = repcap.Sensor.Default) \n
		Returns the measurement results for the power sensor connected to Sensor <no>. The values described below are returned by
		FETCh and READ commands. CALCulate commands return error codes instead, one value for each result listed below. \n
			:param sensor: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sensor')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		sensor_cmd_val = self._cmd_group.get_repcap_cmd_value(sensor, repcap.Sensor)
		return self._core.io.query_struct(f'READ:GPRF:MEASurement<Instance>:NRPM:SENSor{sensor_cmd_val}:POWer?', self.__class__.ResultData())

	def fetch(self, sensor=repcap.Sensor.Default) -> ResultData:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:NRPM:SENSor<nr_NRPM>:POWer \n
		Snippet: value: ResultData = driver.gprf.measurement.nrpm.sensor.power.fetch(sensor = repcap.Sensor.Default) \n
		Returns the measurement results for the power sensor connected to Sensor <no>. The values described below are returned by
		FETCh and READ commands. CALCulate commands return error codes instead, one value for each result listed below. \n
			:param sensor: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sensor')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		sensor_cmd_val = self._cmd_group.get_repcap_cmd_value(sensor, repcap.Sensor)
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:NRPM:SENSor{sensor_cmd_val}:POWer?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- State_Antenna_1: enums.ResultStatus2: No parameter help available
			- State_Antenna_2: enums.ResultStatus2: No parameter help available
			- State_Antenna_3: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('State_Antenna_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('State_Antenna_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('State_Antenna_3', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.State_Antenna_1: enums.ResultStatus2 = None
			self.State_Antenna_2: enums.ResultStatus2 = None
			self.State_Antenna_3: enums.ResultStatus2 = None

	def calculate(self, sensor=repcap.Sensor.Default) -> CalculateStruct:
		"""SCPI: CALCulate:GPRF:MEASurement<Instance>:NRPM:SENSor<nr_NRPM>:POWer \n
		Snippet: value: CalculateStruct = driver.gprf.measurement.nrpm.sensor.power.calculate(sensor = repcap.Sensor.Default) \n
		Returns the measurement results for the power sensor connected to Sensor <no>. The values described below are returned by
		FETCh and READ commands. CALCulate commands return error codes instead, one value for each result listed below. \n
			:param sensor: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sensor')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		sensor_cmd_val = self._cmd_group.get_repcap_cmd_value(sensor, repcap.Sensor)
		return self._core.io.query_struct(f'CALCulate:GPRF:MEASurement<Instance>:NRPM:SENSor{sensor_cmd_val}:POWer?', self.__class__.CalculateStruct())
