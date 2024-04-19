from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpathCls:
	"""Spath commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	def get_count(self) -> int:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SPATh:COUNt \n
		Snippet: value: int = driver.route.gprf.measurement.spath.get_count() \n
		No command help available \n
			:return: signal_path_count: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SPATh:COUNt?')
		return Conversions.str_to_int(response)

	def get_value(self) -> str:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SPATh \n
		Snippet: value: str = driver.route.gprf.measurement.spath.get_value() \n
		Selects one or more RF connections (signal input paths) for the measured signal. The number of expected connections
		depends on the list mode settings of the power measurement. Configure them before sending this command.
			INTRO_CMD_HELP: Distinguish the following situations: \n
			- List mode OFF: One connection is expected.
			- List mode ON and connection source GLOBal: One connection is expected. It is used for all list mode segments.
			- List mode ON and connection source INDex: The number of connections configured via [CONFigure:]GPRF:MEAS<i>:POWer:LIST:NIDX is expected. The order of the connections assigns them to an index (connection with index 1, index 2, index 3, ...) .
			INTRO_CMD_HELP: Related commands: \n
			- List mode state: method RsCMPX_Gprf.Configure.Gprf.Measurement.Power.ListPy.value
			- Connection source: [CONFigure:]GPRF:MEAS<i>:POWer:LIST:CSOurce
			- Connection index per segment: [CONFigure:]GPRF:MEAS<i>:POWer:LIST:CIDX
		For possible connection names, see method RsCMPX_Gprf.Catalog.Gprf.Measurement.Spath.get_. \n
			:return: signal_path: Comma-separated list of strings, one string per RF connection.
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SPATh?')
		return trim_str_response(response)

	def set_value(self, signal_path: str) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SPATh \n
		Snippet: driver.route.gprf.measurement.spath.set_value(signal_path = 'abc') \n
		Selects one or more RF connections (signal input paths) for the measured signal. The number of expected connections
		depends on the list mode settings of the power measurement. Configure them before sending this command.
			INTRO_CMD_HELP: Distinguish the following situations: \n
			- List mode OFF: One connection is expected.
			- List mode ON and connection source GLOBal: One connection is expected. It is used for all list mode segments.
			- List mode ON and connection source INDex: The number of connections configured via [CONFigure:]GPRF:MEAS<i>:POWer:LIST:NIDX is expected. The order of the connections assigns them to an index (connection with index 1, index 2, index 3, ...) .
			INTRO_CMD_HELP: Related commands: \n
			- List mode state: method RsCMPX_Gprf.Configure.Gprf.Measurement.Power.ListPy.value
			- Connection source: [CONFigure:]GPRF:MEAS<i>:POWer:LIST:CSOurce
			- Connection index per segment: [CONFigure:]GPRF:MEAS<i>:POWer:LIST:CIDX
		For possible connection names, see method RsCMPX_Gprf.Catalog.Gprf.Measurement.Spath.get_. \n
			:param signal_path: Comma-separated list of strings, one string per RF connection.
		"""
		param = Conversions.value_to_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SPATh {param}')
