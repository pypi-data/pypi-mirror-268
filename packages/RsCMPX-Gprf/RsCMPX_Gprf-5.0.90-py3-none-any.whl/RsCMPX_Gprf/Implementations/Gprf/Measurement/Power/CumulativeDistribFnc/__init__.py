from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CumulativeDistribFncCls:
	"""CumulativeDistribFnc commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cumulativeDistribFnc", core, parent)

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def sample(self):
		"""sample commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sample'):
			from .Sample import SampleCls
			self._sample = SampleCls(self._core, self._cmd_group)
		return self._sample

	@property
	def probability(self):
		"""probability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_probability'):
			from .Probability import ProbabilityCls
			self._probability = ProbabilityCls(self._core, self._cmd_group)
		return self._probability

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CCDF \n
		Snippet: value: List[float] = driver.gprf.measurement.power.cumulativeDistribFnc.fetch() \n
		Returns the CCDF diagram contents. \n
		Suppressed linked return values: reliability \n
			:return: results: 4096 results, each representing a 0.047-dB interval ('bin')"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:CCDF?', suppressed)
		return response

	def clone(self) -> 'CumulativeDistribFncCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CumulativeDistribFncCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
