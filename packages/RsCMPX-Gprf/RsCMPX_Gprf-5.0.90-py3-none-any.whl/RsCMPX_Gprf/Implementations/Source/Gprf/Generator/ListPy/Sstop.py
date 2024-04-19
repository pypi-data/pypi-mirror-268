from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SstopCls:
	"""Sstop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sstop", core, parent)

	def set(self, start_index: int, stop_index: int, goto_index: int = None) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:SSTop \n
		Snippet: driver.source.gprf.generator.listPy.sstop.set(start_index = 1, stop_index = 1, goto_index = 1) \n
		No command help available \n
			:param start_index: No help available
			:param stop_index: No help available
			:param goto_index: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start_index', start_index, DataType.Integer), ArgSingle('stop_index', stop_index, DataType.Integer), ArgSingle('goto_index', goto_index, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:SSTop {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Start_Index: int: No parameter help available
			- Stop_Index: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Stop_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Stop_Index: int = None

	def get(self) -> GetStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:SSTop \n
		Snippet: value: GetStruct = driver.source.gprf.generator.listPy.sstop.get() \n
		No command help available \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:LIST:SSTop?', self.__class__.GetStruct())
