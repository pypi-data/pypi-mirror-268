from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SequencerCls:
	"""Sequencer commands group definition. 105 total commands, 10 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequencer", core, parent)

	@property
	def apool(self):
		"""apool commands group. 13 Sub-classes, 8 commands."""
		if not hasattr(self, '_apool'):
			from .Apool import ApoolCls
			self._apool = ApoolCls(self._core, self._cmd_group)
		return self._apool

	@property
	def reliability(self):
		"""reliability commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_reliability'):
			from .Reliability import ReliabilityCls
			self._reliability = ReliabilityCls(self._core, self._cmd_group)
		return self._reliability

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def rfSettings(self):
		"""rfSettings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def listPy(self):
		"""listPy commands group. 13 Sub-classes, 3 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def marker(self):
		"""marker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import MarkerCls
			self._marker = MarkerCls(self._core, self._cmd_group)
		return self._marker

	@property
	def wmarker(self):
		"""wmarker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wmarker'):
			from .Wmarker import WmarkerCls
			self._wmarker = WmarkerCls(self._core, self._cmd_group)
		return self._wmarker

	@property
	def rmarker(self):
		"""rmarker commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmarker'):
			from .Rmarker import RmarkerCls
			self._rmarker = RmarkerCls(self._core, self._cmd_group)
		return self._rmarker

	@property
	def dtone(self):
		"""dtone commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtone'):
			from .Dtone import DtoneCls
			self._dtone = DtoneCls(self._core, self._cmd_group)
		return self._dtone

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import TddCls
			self._tdd = TddCls(self._core, self._cmd_group)
		return self._tdd

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepeatMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition \n
		Snippet: value: enums.RepeatMode = driver.source.gprf.generator.sequencer.get_repetition() \n
		Defines the repetition mode for the sequencer list. \n
			:return: repetition: CONTinuous: unlimited repetitions, with cyclic processing SINGle: configured number of repetitions, with cyclic processing
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepeatMode)

	def set_repetition(self, repetition: enums.RepeatMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition \n
		Snippet: driver.source.gprf.generator.sequencer.set_repetition(repetition = enums.RepeatMode.CONTinuous) \n
		Defines the repetition mode for the sequencer list. \n
			:param repetition: CONTinuous: unlimited repetitions, with cyclic processing SINGle: configured number of repetitions, with cyclic processing
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepeatMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition {param}')

	def get_nrepetition(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:NREPetition \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.get_nrepetition() \n
		Defines how often the sequencer list is processed in SINGle repetition mode. \n
			:return: num_of_rep: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:NREPetition?')
		return Conversions.str_to_int(response)

	def set_nrepetition(self, num_of_rep: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:NREPetition \n
		Snippet: driver.source.gprf.generator.sequencer.set_nrepetition(num_of_rep = 1) \n
		Defines how often the sequencer list is processed in SINGle repetition mode. \n
			:param num_of_rep: No help available
		"""
		param = Conversions.decimal_value_to_str(num_of_rep)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:NREPetition {param}')

	def get_rcount(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:RCOunt \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.get_rcount() \n
		Queries the number of completed repetitions of the sequencer list, for repetition mode SINGle. \n
			:return: repcount: If the sequencer is not running or the repetition mode is CONTinuous, NAV is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:RCOunt?')
		return Conversions.str_to_int(response)

	def get_signal(self) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:SIGNal \n
		Snippet: value: bool = driver.source.gprf.generator.sequencer.get_signal() \n
		Queries whether a signal is generated or not. \n
			:return: signal: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:SIGNal?')
		return Conversions.str_to_bool(response)

	def get_centry(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:CENTry \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.get_centry() \n
		Queries the index of the processed entry. The remote query takes between 2 ms and 3 ms, which introduces an uncertainty
		to the results. \n
			:return: current_entry: If the sequencer is not running, NAV is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:CENTry?')
		return Conversions.str_to_int(response)

	def get_uoptions(self) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:UOPTions \n
		Snippet: value: str = driver.source.gprf.generator.sequencer.get_uoptions() \n
		Queries a list of the used software options. \n
			:return: used_options: The string contains a comma-separated list of options. If the sequencer is OFF, NAV is returned. If the sequencer is not OFF but no options are used by the sequencer list, 'None' is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:UOPTions?')
		return trim_str_response(response)

	def clone(self) -> 'SequencerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SequencerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
