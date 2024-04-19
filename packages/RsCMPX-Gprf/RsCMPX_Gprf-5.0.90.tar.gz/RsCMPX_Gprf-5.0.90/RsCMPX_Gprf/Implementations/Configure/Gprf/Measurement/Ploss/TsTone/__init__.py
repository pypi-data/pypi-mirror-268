from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsToneCls:
	"""TsTone commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsTone", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_file'):
			from .File import FileCls
			self._file = FileCls(self._core, self._cmd_group)
		return self._file

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:ENABle \n
		Snippet: value: bool = driver.configure.gprf.measurement.ploss.tsTone.get_enable() \n
		Enables using configured Touchstone files. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:ENABle \n
		Snippet: driver.configure.gprf.measurement.ploss.tsTone.set_enable(enable = False) \n
		Enables using configured Touchstone files. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:ENABle {param}')

	def clone(self) -> 'TsToneCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TsToneCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
