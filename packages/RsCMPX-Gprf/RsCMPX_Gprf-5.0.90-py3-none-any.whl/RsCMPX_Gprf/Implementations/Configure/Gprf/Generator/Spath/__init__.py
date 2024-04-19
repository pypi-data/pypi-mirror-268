from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpathCls:
	"""Spath commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	@property
	def usage(self):
		"""usage commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .Usage import UsageCls
			self._usage = UsageCls(self._core, self._cmd_group)
		return self._usage

	def get_bc_switch(self) -> bool:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:SPATh:BCSWitch \n
		Snippet: value: bool = driver.configure.gprf.generator.spath.get_bc_switch() \n
		Enables signal broadcast to several connectors of an R&S CM-Z310A. \n
			:return: connect_switch: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:GENerator<Instance>:SPATh:BCSWitch?')
		return Conversions.str_to_bool(response)

	def set_bc_switch(self, connect_switch: bool) -> None:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:SPATh:BCSWitch \n
		Snippet: driver.configure.gprf.generator.spath.set_bc_switch(connect_switch = False) \n
		Enables signal broadcast to several connectors of an R&S CM-Z310A. \n
			:param connect_switch: No help available
		"""
		param = Conversions.bool_to_str(connect_switch)
		self._core.io.write(f'CONFigure:GPRF:GENerator<Instance>:SPATh:BCSWitch {param}')

	def clone(self) -> 'SpathCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpathCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
