from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCls:
	"""Single commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("single", core, parent)

	def set(self, tx_index: float, usage: bool, bench=repcap.Bench.Default) -> None:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe:BENCh<nr>:TX:SINGle \n
		Snippet: driver.configure.gprf.generator.spath.usage.bench.tx.single.set(tx_index = 1.0, usage = False, bench = repcap.Bench.Default) \n
		Activates or deactivates the RF connector RF<no>.<TxIndex>+1. Example: <no>=2 plus <TxIndex>=4 means connector RF2.5. \n
			:param tx_index: No help available
			:param usage: ON: activate the connector OFF: deactivate the connector
			:param bench: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bench')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tx_index', tx_index, DataType.Float), ArgSingle('usage', usage, DataType.Boolean))
		bench_cmd_val = self._cmd_group.get_repcap_cmd_value(bench, repcap.Bench)
		self._core.io.write(f'CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe:BENCh{bench_cmd_val}:TX:SINGle {param}'.rstrip())

	def get(self, tx_index: float, bench=repcap.Bench.Default) -> bool:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe:BENCh<nr>:TX:SINGle \n
		Snippet: value: bool = driver.configure.gprf.generator.spath.usage.bench.tx.single.get(tx_index = 1.0, bench = repcap.Bench.Default) \n
		Activates or deactivates the RF connector RF<no>.<TxIndex>+1. Example: <no>=2 plus <TxIndex>=4 means connector RF2.5. \n
			:param tx_index: No help available
			:param bench: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bench')
			:return: usage: ON: activate the connector OFF: deactivate the connector"""
		param = Conversions.decimal_value_to_str(tx_index)
		bench_cmd_val = self._cmd_group.get_repcap_cmd_value(bench, repcap.Bench)
		response = self._core.io.query_str(f'CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe:BENCh{bench_cmd_val}:TX:SINGle? {param}')
		return Conversions.str_to_bool(response)
