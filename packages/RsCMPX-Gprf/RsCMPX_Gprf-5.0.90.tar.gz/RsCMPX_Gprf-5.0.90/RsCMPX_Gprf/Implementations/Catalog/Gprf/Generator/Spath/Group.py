from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GroupCls:
	"""Group commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("group", core, parent)

	def get_connector(self) -> str:
		"""SCPI: CATalog:GPRF:GENerator<Instance>:SPATh:GROup:CONNector \n
		Snippet: value: str = driver.catalog.gprf.generator.spath.group.get_connector() \n
		Returns the names of the connectors of the active connector group. Select the connector group via method RsCMPX_Gprf.
		Route.Gprf.Generator.Spath.value. \n
			:return: connector_name: Comma-separated list of values, one value per connector.
		"""
		response = self._core.io.query_str('CATalog:GPRF:GENerator<Instance>:SPATh:GROup:CONNector?')
		return trim_str_response(response)

	def get(self, connector_name: str) -> List[str]:
		"""SCPI: CATalog:GPRF:GENerator<Instance>:SPATh:GROup \n
		Snippet: value: List[str] = driver.catalog.gprf.generator.spath.group.get(connector_name = 'abc') \n
		Returns the names of the RF connections that start at the specified connector. This command is only relevant if you
		create your own RF connections (see base manual) . The default RF connections have the same name as the assigned
		connector. \n
			:param connector_name: Start point of the RF connections.
			:return: signal_path: Comma-separated list of strings, one string per RF connection."""
		param = Conversions.value_to_quoted_str(connector_name)
		response = self._core.io.query_str(f'CATalog:GPRF:GENerator<Instance>:SPATh:GROup? {param}')
		return Conversions.str_to_str_list(response)
