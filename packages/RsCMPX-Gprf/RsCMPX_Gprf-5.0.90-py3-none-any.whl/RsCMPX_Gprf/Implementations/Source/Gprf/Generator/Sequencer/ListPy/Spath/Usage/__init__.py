from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsageCls:
	"""Usage commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usage", core, parent)

	@property
	def bench(self):
		"""bench commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_bench'):
			from .Bench import BenchCls
			self._bench = BenchCls(self._core, self._cmd_group)
		return self._bench

	def set(self, index: int, connectors_state: List[bool]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SPATh:USAGe \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.spath.usage.set(index = 1, connectors_state = [True, False, True]) \n
		Activates or deactivates the individual RF connectors of the active connector group, for the sequencer list entry with
		the selected <Index>. Select the connector group via method RsCMPX_Gprf.Route.Gprf.Generator.Spath.value. Query a list of
		the connectors of the connector group via method RsCMPX_Gprf.Catalog.Gprf.Generator.Spath.Group.connector. \n
			:param index: No help available
			:param connectors_state: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle.as_open_list('connectors_state', connectors_state, DataType.BooleanList, None))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SPATh:USAGe {param}'.rstrip())

	def get(self, index: int) -> List[bool]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SPATh:USAGe \n
		Snippet: value: List[bool] = driver.source.gprf.generator.sequencer.listPy.spath.usage.get(index = 1) \n
		Activates or deactivates the individual RF connectors of the active connector group, for the sequencer list entry with
		the selected <Index>. Select the connector group via method RsCMPX_Gprf.Route.Gprf.Generator.Spath.value. Query a list of
		the connectors of the connector group via method RsCMPX_Gprf.Catalog.Gprf.Generator.Spath.Group.connector. \n
			:param index: Comma-separated list of values, one value per connector of the connector group. ON: activate the connector OFF: deactivate the connector
			:return: connectors_state: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SPATh:USAGe? {param}')
		return Conversions.str_to_bool_list(response)

	def clone(self) -> 'UsageCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UsageCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
