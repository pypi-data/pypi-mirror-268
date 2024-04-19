from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, signal_index: List[int]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:INDex:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.index.all.set(signal_index = [1, 2, 3]) \n
		No command help available \n
			:param signal_index: No help available
		"""
		param = Conversions.list_to_csv_str(signal_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:INDex:ALL {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Signal_Index: List[int]: No parameter help available
			- Signal: List[str]: No parameter help available
			- Path: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Signal_Index', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Signal', DataType.StringList, None, False, True, 1),
			ArgStruct('Path', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Signal_Index: List[int] = None
			self.Signal: List[str] = None
			self.Path: List[str] = None

	def get(self) -> GetStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:INDex:ALL \n
		Snippet: value: GetStruct = driver.source.gprf.generator.sequencer.listPy.signal.index.all.get() \n
		No command help available \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:INDex:ALL?', self.__class__.GetStruct())
