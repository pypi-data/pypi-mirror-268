from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EepromCls:
	"""Eeprom commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eeprom", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def ezz(self):
		"""ezz commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ezz'):
			from .Ezz import EzzCls
			self._ezz = EzzCls(self._core, self._cmd_group)
		return self._ezz

	@property
	def ezo(self):
		"""ezo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ezo'):
			from .Ezo import EzoCls
			self._ezo = EzoCls(self._core, self._cmd_group)
		return self._ezo

	@property
	def eoo(self):
		"""eoo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eoo'):
			from .Eoo import EooCls
			self._eoo = EooCls(self._core, self._cmd_group)
		return self._eoo

	def clone(self) -> 'EepromCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EepromCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
