from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


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

	def set(self, enable: List[bool], bench=repcap.Bench.Default) -> None:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe:BENCh<nr> \n
		Snippet: driver.configure.gprf.generator.spath.usage.bench.set(enable = [True, False, True], bench = repcap.Bench.Default) \n
		Activates or deactivates the individual RF connectors of the connector group <no> (global definition) . \n
			:param enable: Comma-separated list of values, one value per connector of the connector group. ON: activate the connector OFF: deactivate the connector
			:param bench: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bench')
		"""
		param = Conversions.list_to_csv_str(enable)
		bench_cmd_val = self._cmd_group.get_repcap_cmd_value(bench, repcap.Bench)
		self._core.io.write(f'CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe:BENCh{bench_cmd_val} {param}')

	def get(self, bench=repcap.Bench.Default) -> List[bool]:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe:BENCh<nr> \n
		Snippet: value: List[bool] = driver.configure.gprf.generator.spath.usage.bench.get(bench = repcap.Bench.Default) \n
		Activates or deactivates the individual RF connectors of the connector group <no> (global definition) . \n
			:param bench: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bench')
			:return: enable: Comma-separated list of values, one value per connector of the connector group. ON: activate the connector OFF: deactivate the connector"""
		bench_cmd_val = self._cmd_group.get_repcap_cmd_value(bench, repcap.Bench)
		response = self._core.io.query_str(f'CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe:BENCh{bench_cmd_val}?')
		return Conversions.str_to_bool_list(response)

	def clone(self) -> 'BenchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BenchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
