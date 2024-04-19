from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqRecorderCls:
	"""IqRecorder commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqRecorder", core, parent)

	@property
	def bandpass(self):
		"""bandpass commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandpass'):
			from .Bandpass import BandpassCls
			self._bandpass = BandpassCls(self._core, self._cmd_group)
		return self._bandpass

	@property
	def gauss(self):
		"""gauss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gauss'):
			from .Gauss import GaussCls
			self._gauss = GaussCls(self._core, self._cmd_group)
		return self._gauss

	@property
	def samples(self):
		"""samples commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_samples'):
			from .Samples import SamplesCls
			self._samples = SamplesCls(self._core, self._cmd_group)
		return self._samples

	def clone(self) -> 'IqRecorderCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqRecorderCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
