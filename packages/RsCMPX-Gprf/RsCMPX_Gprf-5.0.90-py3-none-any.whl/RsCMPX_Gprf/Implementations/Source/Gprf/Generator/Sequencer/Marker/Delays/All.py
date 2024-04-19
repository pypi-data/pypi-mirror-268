from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, restart_marker: float, marker_1: float, marker_2: float, marker_3: float, marker_4: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.marker.delays.all.set(restart_marker = 1.0, marker_1 = 1.0, marker_2 = 1.0, marker_3 = 1.0, marker_4 = 1.0) \n
		No command help available \n
			:param restart_marker: No help available
			:param marker_1: No help available
			:param marker_2: No help available
			:param marker_3: No help available
			:param marker_4: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('restart_marker', restart_marker, DataType.Float), ArgSingle('marker_1', marker_1, DataType.Float), ArgSingle('marker_2', marker_2, DataType.Float), ArgSingle('marker_3', marker_3, DataType.Float), ArgSingle('marker_4', marker_4, DataType.Float))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Restart_Marker: float: No parameter help available
			- Marker_1: float: No parameter help available
			- Marker_2: float: No parameter help available
			- Marker_3: float: No parameter help available
			- Marker_4: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Restart_Marker'),
			ArgStruct.scalar_float('Marker_1'),
			ArgStruct.scalar_float('Marker_2'),
			ArgStruct.scalar_float('Marker_3'),
			ArgStruct.scalar_float('Marker_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Restart_Marker: float = None
			self.Marker_1: float = None
			self.Marker_2: float = None
			self.Marker_3: float = None
			self.Marker_4: float = None

	def get(self) -> AllStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays:ALL \n
		Snippet: value: AllStruct = driver.source.gprf.generator.sequencer.marker.delays.all.get() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays:ALL?', self.__class__.AllStruct())
