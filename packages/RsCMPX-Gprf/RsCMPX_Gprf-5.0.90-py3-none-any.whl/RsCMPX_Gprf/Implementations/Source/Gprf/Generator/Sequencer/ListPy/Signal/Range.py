from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RangeCls:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, start_index: float, stop_index: float, signal: str) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:RANGe \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.range.set(start_index = 1.0, stop_index = 1.0, signal = 'abc') \n
		No command help available \n
			:param start_index: No help available
			:param stop_index: No help available
			:param signal: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start_index', start_index, DataType.Float), ArgSingle('stop_index', stop_index, DataType.Float), ArgSingle('signal', signal, DataType.String))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:RANGe {param}'.rstrip())

	def get(self, start_index: float, stop_index: float) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:RANGe \n
		Snippet: value: List[str] = driver.source.gprf.generator.sequencer.listPy.signal.range.get(start_index = 1.0, stop_index = 1.0) \n
		No command help available \n
			:param start_index: No help available
			:param stop_index: No help available
			:return: result: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start_index', start_index, DataType.Float), ArgSingle('stop_index', stop_index, DataType.Float))
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:RANGe? {param}'.rstrip())
		return Conversions.str_to_str_list(response)
