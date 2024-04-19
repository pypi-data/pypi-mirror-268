from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BenchCls:
	"""Bench commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: Bench, default value after init: Bench.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bench", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bench_get', 'repcap_bench_set', repcap.Bench.Nr1)

	def repcap_bench_set(self, bench: repcap.Bench) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Bench.Default
		Default value after init: Bench.Nr1"""
		self._cmd_group.set_repcap_enum_value(bench)

	def repcap_bench_get(self) -> repcap.Bench:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def tx(self):
		"""tx commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tx'):
			from .Tx import TxCls
			self._tx = TxCls(self._core, self._cmd_group)
		return self._tx

	def set(self, index: float, enable: List[bool], bench=repcap.Bench.Default) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SPATh:USAGe:BENCh<nr> \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.spath.usage.bench.set(index = 1.0, enable = [True, False, True], bench = repcap.Bench.Default) \n
		Activates or deactivates the individual RF connectors of the connector group <no>, for the sequencer list entry with the
		selected <Index>. \n
			:param index: No help available
			:param enable: Comma-separated list of values, one value per connector of the connector group. ON: activate the connector OFF: deactivate the connector
			:param bench: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bench')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Float), ArgSingle.as_open_list('enable', enable, DataType.BooleanList, None))
		bench_cmd_val = self._cmd_group.get_repcap_cmd_value(bench, repcap.Bench)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SPATh:USAGe:BENCh{bench_cmd_val} {param}'.rstrip())

	def get(self, index: float, bench=repcap.Bench.Default) -> List[bool]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SPATh:USAGe:BENCh<nr> \n
		Snippet: value: List[bool] = driver.source.gprf.generator.sequencer.listPy.spath.usage.bench.get(index = 1.0, bench = repcap.Bench.Default) \n
		Activates or deactivates the individual RF connectors of the connector group <no>, for the sequencer list entry with the
		selected <Index>. \n
			:param index: No help available
			:param bench: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bench')
			:return: enable: Comma-separated list of values, one value per connector of the connector group. ON: activate the connector OFF: deactivate the connector"""
		param = Conversions.decimal_value_to_str(index)
		bench_cmd_val = self._cmd_group.get_repcap_cmd_value(bench, repcap.Bench)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SPATh:USAGe:BENCh{bench_cmd_val}? {param}')
		return Conversions.str_to_bool_list(response)

	def clone(self) -> 'BenchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BenchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
