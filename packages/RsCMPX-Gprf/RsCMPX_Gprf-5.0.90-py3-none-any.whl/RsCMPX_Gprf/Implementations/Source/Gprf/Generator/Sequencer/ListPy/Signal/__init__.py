from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.Utilities import trim_str_response
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalCls:
	"""Signal commands group definition. 13 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import RangeCls
			self._range = RangeCls(self._core, self._cmd_group)
		return self._range

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def all(self):
		"""all commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def index(self):
		"""index commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_index'):
			from .Index import IndexCls
			self._index = IndexCls(self._core, self._cmd_group)
		return self._index

	def set(self, index: int, signal: str) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.set(index = 1, signal = 'abc') \n
		Defines or queries the signal type for the sequencer list entry with the selected <Index>. A complete list of all
		supported strings can be queried using method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.Signal.Catalog.value. \n
			:param index: No help available
			:param signal: Signal type
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('signal', signal, DataType.String))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal {param}'.rstrip())

	def get(self, index: int) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal \n
		Snippet: value: str = driver.source.gprf.generator.sequencer.listPy.signal.get(index = 1) \n
		Defines or queries the signal type for the sequencer list entry with the selected <Index>. A complete list of all
		supported strings can be queried using method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.Signal.Catalog.value. \n
			:param index: No help available
			:return: signal: Signal type"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal? {param}')
		return trim_str_response(response)

	def clone(self) -> 'SignalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
