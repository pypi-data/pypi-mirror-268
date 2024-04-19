from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FileCls:
	"""File commands group definition. 8 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	@property
	def rpc(self):
		"""rpc commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_rpc'):
			from .Rpc import RpcCls
			self._rpc = RpcCls(self._core, self._cmd_group)
		return self._rpc

	@property
	def psub(self):
		"""psub commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_psub'):
			from .Psub import PsubCls
			self._psub = PsubCls(self._core, self._cmd_group)
		return self._psub

	def clone(self) -> 'FileCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FileCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
