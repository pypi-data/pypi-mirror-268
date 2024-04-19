from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MdownCls:
	"""Mdown commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mdown", core, parent)

	def set(self, index: int = None) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:MDOWn \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.entry.mdown.set(index = 1) \n
		Moves the selected entry of the sequencer list one position down. You can specify <Index> to select that entry. Or you
		can select an entry via method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.index. The selection moves with the
		entry. \n
			:param index: Index of the entry to be moved.
		"""
		param = ''
		if index:
			param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:MDOWn {param}'.strip())
