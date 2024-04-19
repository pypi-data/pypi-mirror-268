from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InsertCls:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, after_index: int = None) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:INSert \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.entry.insert.set(after_index = 1) \n
		Inserts a new entry after the selected entry into the sequencer list. You can specify <AfterIndex> to select that entry.
		Or you can select an entry via method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.index. \n
			:param after_index: Index of the entry to be selected.
		"""
		param = ''
		if after_index:
			param = Conversions.decimal_value_to_str(after_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:INSert {param}'.strip())
