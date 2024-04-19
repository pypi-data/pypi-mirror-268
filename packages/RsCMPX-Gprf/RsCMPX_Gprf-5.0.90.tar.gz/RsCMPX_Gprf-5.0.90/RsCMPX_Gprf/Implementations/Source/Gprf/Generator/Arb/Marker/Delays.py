from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DelaysCls:
	"""Delays commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delays", core, parent)

	def set(self, marker_2: int, marker_3: int, marker_4: int, restart_marker: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays \n
		Snippet: driver.source.gprf.generator.arb.marker.delays.set(marker_2 = 1, marker_3 = 1, marker_4 = 1, restart_marker = 1) \n
		No command help available \n
			:param marker_2: No help available
			:param marker_3: No help available
			:param marker_4: No help available
			:param restart_marker: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('marker_2', marker_2, DataType.Integer), ArgSingle('marker_3', marker_3, DataType.Integer), ArgSingle('marker_4', marker_4, DataType.Integer), ArgSingle('restart_marker', restart_marker, DataType.Integer))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays {param}'.rstrip())

	# noinspection PyTypeChecker
	class DelaysStruct(StructBase):
		"""Response structure. Fields: \n
			- Marker_2: int: No parameter help available
			- Marker_3: int: No parameter help available
			- Marker_4: int: No parameter help available
			- Restart_Marker: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Marker_2'),
			ArgStruct.scalar_int('Marker_3'),
			ArgStruct.scalar_int('Marker_4'),
			ArgStruct.scalar_int('Restart_Marker')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Marker_2: int = None
			self.Marker_3: int = None
			self.Marker_4: int = None
			self.Restart_Marker: int = None

	def get(self) -> DelaysStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays \n
		Snippet: value: DelaysStruct = driver.source.gprf.generator.arb.marker.delays.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DelaysStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays?', self.__class__.DelaysStruct())
