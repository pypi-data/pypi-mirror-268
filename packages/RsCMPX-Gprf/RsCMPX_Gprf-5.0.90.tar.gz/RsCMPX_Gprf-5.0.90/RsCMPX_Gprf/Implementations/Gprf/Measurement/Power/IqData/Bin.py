from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BinCls:
	"""Bin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bin", core, parent)

	def fetch(self, list_index: int, result_index: int = None) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:IQData:BIN \n
		Snippet: value: List[float] = driver.gprf.measurement.power.iqData.bin.fetch(list_index = 1, result_index = 1) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param list_index: No help available
			:param result_index: No help available
			:return: iq_data: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('list_index', list_index, DataType.Integer), ArgSingle('result_index', result_index, DataType.Integer, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:IQData:BIN? {param}'.rstrip(), suppressed)
		return response
