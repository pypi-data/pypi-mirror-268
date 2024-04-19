from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TenvironmentCls:
	"""Tenvironment commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tenvironment", core, parent)

	@property
	def spath(self):
		"""spath commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spath'):
			from .Spath import SpathCls
			self._spath = SpathCls(self._core, self._cmd_group)
		return self._spath

	def clone(self) -> 'TenvironmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TenvironmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
