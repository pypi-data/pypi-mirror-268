from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DelaysCls:
	"""Delays commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delays", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def set(self, restart_marker: float, marker_2: float, marker_3: float, marker_4: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays \n
		Snippet: driver.source.gprf.generator.sequencer.marker.delays.set(restart_marker = 1.0, marker_2 = 1.0, marker_3 = 1.0, marker_4 = 1.0) \n
		Defines delay times for the ARB output trigger events relative to the marker events. \n
			:param restart_marker: No help available
			:param marker_2: No help available
			:param marker_3: No help available
			:param marker_4: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('restart_marker', restart_marker, DataType.Float), ArgSingle('marker_2', marker_2, DataType.Float), ArgSingle('marker_3', marker_3, DataType.Float), ArgSingle('marker_4', marker_4, DataType.Float))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays {param}'.rstrip())

	# noinspection PyTypeChecker
	class DelaysStruct(StructBase):
		"""Response structure. Fields: \n
			- Restart_Marker: float: No parameter help available
			- Marker_2: float: No parameter help available
			- Marker_3: float: No parameter help available
			- Marker_4: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Restart_Marker'),
			ArgStruct.scalar_float('Marker_2'),
			ArgStruct.scalar_float('Marker_3'),
			ArgStruct.scalar_float('Marker_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Restart_Marker: float = None
			self.Marker_2: float = None
			self.Marker_3: float = None
			self.Marker_4: float = None

	def get(self) -> DelaysStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays \n
		Snippet: value: DelaysStruct = driver.source.gprf.generator.sequencer.marker.delays.get() \n
		Defines delay times for the ARB output trigger events relative to the marker events. \n
			:return: structure: for return value, see the help for DelaysStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays?', self.__class__.DelaysStruct())

	def clone(self) -> 'DelaysCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DelaysCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
