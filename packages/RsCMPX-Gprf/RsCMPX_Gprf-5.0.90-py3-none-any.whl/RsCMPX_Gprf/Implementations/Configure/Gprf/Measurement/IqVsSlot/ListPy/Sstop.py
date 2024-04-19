from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SstopCls:
	"""Sstop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sstop", core, parent)

	def set(self, start_index: int, stop_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:SSTop \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.listPy.sstop.set(start_index = 1, stop_index = 1) \n
		Selects the range of subsweeps to be measured (first and last subsweep of a sweep) . The total number of steps must not
		exceed 3000 (step count times number of subsweeps) . \n
			:param start_index: No help available
			:param stop_index: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start_index', start_index, DataType.Integer), ArgSingle('stop_index', stop_index, DataType.Integer))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:SSTop {param}'.rstrip())

	# noinspection PyTypeChecker
	class SstopStruct(StructBase):
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

	def get(self) -> SstopStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:SSTop \n
		Snippet: value: SstopStruct = driver.configure.gprf.measurement.iqVsSlot.listPy.sstop.get() \n
		Selects the range of subsweeps to be measured (first and last subsweep of a sweep) . The total number of steps must not
		exceed 3000 (step count times number of subsweeps) . \n
			:return: structure: for return value, see the help for SstopStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:SSTop?', self.__class__.SstopStruct())
