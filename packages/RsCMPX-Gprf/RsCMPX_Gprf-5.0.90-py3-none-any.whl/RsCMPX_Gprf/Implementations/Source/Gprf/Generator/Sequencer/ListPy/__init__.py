from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 54 total commands, 13 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def spath(self):
		"""spath commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spath'):
			from .Spath import SpathCls
			self._spath = SpathCls(self._core, self._cmd_group)
		return self._spath

	@property
	def fill(self):
		"""fill commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_fill'):
			from .Fill import FillCls
			self._fill = FillCls(self._core, self._cmd_group)
		return self._fill

	@property
	def signal(self):
		"""signal commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_signal'):
			from .Signal import SignalCls
			self._signal = SignalCls(self._core, self._cmd_group)
		return self._signal

	@property
	def entry(self):
		"""entry commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_entry'):
			from .Entry import EntryCls
			self._entry = EntryCls(self._core, self._cmd_group)
		return self._entry

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def lrms(self):
		"""lrms commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_lrms'):
			from .Lrms import LrmsCls
			self._lrms = LrmsCls(self._core, self._cmd_group)
		return self._lrms

	@property
	def dgain(self):
		"""dgain commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dgain'):
			from .Dgain import DgainCls
			self._dgain = DgainCls(self._core, self._cmd_group)
		return self._dgain

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def lincrement(self):
		"""lincrement commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_lincrement'):
			from .Lincrement import LincrementCls
			self._lincrement = LincrementCls(self._core, self._cmd_group)
		return self._lincrement

	@property
	def itransition(self):
		"""itransition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_itransition'):
			from .Itransition import ItransitionCls
			self._itransition = ItransitionCls(self._core, self._cmd_group)
		return self._itransition

	@property
	def acycles(self):
		"""acycles commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_acycles'):
			from .Acycles import AcyclesCls
			self._acycles = AcyclesCls(self._core, self._cmd_group)
		return self._acycles

	@property
	def dtime(self):
		"""dtime commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dtime'):
			from .Dtime import DtimeCls
			self._dtime = DtimeCls(self._core, self._cmd_group)
		return self._dtime

	@property
	def ttime(self):
		"""ttime commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ttime'):
			from .Ttime import TtimeCls
			self._ttime = TtimeCls(self._core, self._cmd_group)
		return self._ttime

	def set_create(self, entries: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:CREate \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.set_create(entries = 1.0) \n
		Deletes all entries of the sequencer list and creates the defined number of new entries with default settings. \n
			:param entries: Number of entries to be created.
		"""
		param = Conversions.decimal_value_to_str(entries)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:CREate {param}')

	def get_index(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:INDex \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.listPy.get_index() \n
		Selects an entry of the sequencer list. Some other commands use this setting. \n
			:return: current_index: Index of the selected list entry
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:INDex?')
		return Conversions.str_to_int(response)

	def set_index(self, current_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:INDex \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.set_index(current_index = 1) \n
		Selects an entry of the sequencer list. Some other commands use this setting. \n
			:param current_index: Index of the selected list entry
		"""
		param = Conversions.decimal_value_to_str(current_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:INDex {param}')

	def get_mindex(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:MINDex \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.listPy.get_mindex() \n
		Queries the highest index of the sequencer list. The list contains entries with the indices 0 to <MaximumIndex>. \n
			:return: maximum_index: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:MINDex?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'ListPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
