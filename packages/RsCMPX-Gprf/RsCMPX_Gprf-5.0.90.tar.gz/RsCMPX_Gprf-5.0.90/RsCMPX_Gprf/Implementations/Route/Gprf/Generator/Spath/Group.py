from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GroupCls:
	"""Group commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("group", core, parent)

	def set(self, connector_name: str, signal_path: str) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SPATh:GROup \n
		Snippet: driver.route.gprf.generator.spath.group.set(connector_name = 'abc', signal_path = 'abc') \n
		Assigns an RF connection to an output connector. The connection is used if you activate the connector for signal output
		via a connector group. This command is only relevant if you create your own RF connections (see base manual) .
		The default RF connections have the same name as the assigned connector. \n
			:param connector_name: Name of the output connector.
			:param signal_path: RF connection to be assigned to the connector.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector_name', connector_name, DataType.String), ArgSingle('signal_path', signal_path, DataType.String))
		self._core.io.write(f'ROUTe:GPRF:GENerator<Instance>:SPATh:GROup {param}'.rstrip())

	def get(self, connector_name: str) -> str:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SPATh:GROup \n
		Snippet: value: str = driver.route.gprf.generator.spath.group.get(connector_name = 'abc') \n
		Assigns an RF connection to an output connector. The connection is used if you activate the connector for signal output
		via a connector group. This command is only relevant if you create your own RF connections (see base manual) .
		The default RF connections have the same name as the assigned connector. \n
			:param connector_name: Name of the output connector.
			:return: signal_path: RF connection to be assigned to the connector."""
		param = Conversions.value_to_quoted_str(connector_name)
		response = self._core.io.query_str(f'ROUTe:GPRF:GENerator<Instance>:SPATh:GROup? {param}')
		return trim_str_response(response)
