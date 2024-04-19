from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 10 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def prach(self):
		"""prach commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	@property
	def tpc(self):
		"""tpc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpc'):
			from .Tpc import TpcCls
			self._tpc = TpcCls(self._core, self._cmd_group)
		return self._tpc

	@property
	def olpControl(self):
		"""olpControl commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_olpControl'):
			from .OlpControl import OlpControlCls
			self._olpControl = OlpControlCls(self._core, self._cmd_group)
		return self._olpControl

	@property
	def ooSync(self):
		"""ooSync commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ooSync'):
			from .OoSync import OoSyncCls
			self._ooSync = OoSyncCls(self._core, self._cmd_group)
		return self._ooSync

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
