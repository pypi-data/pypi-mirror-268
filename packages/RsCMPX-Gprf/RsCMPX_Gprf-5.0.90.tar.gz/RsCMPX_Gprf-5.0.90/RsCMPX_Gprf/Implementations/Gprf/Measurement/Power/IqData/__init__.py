from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqDataCls:
	"""IqData commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqData", core, parent)

	@property
	def bin(self):
		"""bin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bin'):
			from .Bin import BinCls
			self._bin = BinCls(self._core, self._cmd_group)
		return self._bin

	def fetch(self, list_index: int, result_index: int = None) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:IQData \n
		Snippet: value: List[float] = driver.gprf.measurement.power.iqData.fetch(list_index = 1, result_index = 1) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param list_index: No help available
			:param result_index: No help available
			:return: iq_data: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('list_index', list_index, DataType.Integer), ArgSingle('result_index', result_index, DataType.Integer, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:IQData? {param}'.rstrip(), suppressed)
		return response

	def read(self, list_index: int, result_index: int = None) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:POWer:IQData \n
		Snippet: value: List[float] = driver.gprf.measurement.power.iqData.read(list_index = 1, result_index = 1) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param list_index: No help available
			:param result_index: No help available
			:return: iq_data: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('list_index', list_index, DataType.Integer), ArgSingle('result_index', result_index, DataType.Integer, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:IQData? {param}'.rstrip(), suppressed)
		return response

	def clone(self) -> 'IqDataCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqDataCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
