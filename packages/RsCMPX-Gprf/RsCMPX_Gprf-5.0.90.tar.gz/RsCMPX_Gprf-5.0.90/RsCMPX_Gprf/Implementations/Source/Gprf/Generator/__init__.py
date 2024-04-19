from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeneratorCls:
	"""Generator commands group definition. 186 total commands, 8 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

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
	def iqSettings(self):
		"""iqSettings commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_iqSettings'):
			from .IqSettings import IqSettingsCls
			self._iqSettings = IqSettingsCls(self._core, self._cmd_group)
		return self._iqSettings

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def arb(self):
		"""arb commands group. 6 Sub-classes, 10 commands."""
		if not hasattr(self, '_arb'):
			from .Arb import ArbCls
			self._arb = ArbCls(self._core, self._cmd_group)
		return self._arb

	@property
	def dtone(self):
		"""dtone commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtone'):
			from .Dtone import DtoneCls
			self._dtone = DtoneCls(self._core, self._cmd_group)
		return self._dtone

	@property
	def listPy(self):
		"""listPy commands group. 13 Sub-classes, 9 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def sequencer(self):
		"""sequencer commands group. 10 Sub-classes, 6 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import SequencerCls
			self._sequencer = SequencerCls(self._core, self._cmd_group)
		return self._sequencer

	# noinspection PyTypeChecker
	def get_bb_mode(self) -> enums.BasebandMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:BBMode \n
		Snippet: value: enums.BasebandMode = driver.source.gprf.generator.get_bb_mode() \n
		Selects the baseband mode for the generator signal. \n
			:return: baseband_mode: CW: unmodulated continuous wave signal DTONe: dual-tone signal ARB: processing a waveform file
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:BBMode?')
		return Conversions.str_to_scalar_enum(response, enums.BasebandMode)

	def set_bb_mode(self, baseband_mode: enums.BasebandMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:BBMode \n
		Snippet: driver.source.gprf.generator.set_bb_mode(baseband_mode = enums.BasebandMode.ARB) \n
		Selects the baseband mode for the generator signal. \n
			:param baseband_mode: CW: unmodulated continuous wave signal DTONe: dual-tone signal ARB: processing a waveform file
		"""
		param = Conversions.enum_scalar_to_str(baseband_mode, enums.BasebandMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:BBMode {param}')

	def clone(self) -> 'GeneratorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GeneratorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
