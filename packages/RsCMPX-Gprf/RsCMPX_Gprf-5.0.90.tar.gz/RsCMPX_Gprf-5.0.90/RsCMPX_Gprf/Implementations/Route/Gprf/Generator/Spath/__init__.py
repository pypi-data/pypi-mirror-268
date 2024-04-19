from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpathCls:
	"""Spath commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	@property
	def group(self):
		"""group commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_group'):
			from .Group import GroupCls
			self._group = GroupCls(self._core, self._cmd_group)
		return self._group

	def get_count(self) -> int:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SPATh:COUNt \n
		Snippet: value: int = driver.route.gprf.generator.spath.get_count() \n
		No command help available \n
			:return: signal_path_count: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:GENerator<Instance>:SPATh:COUNt?')
		return Conversions.str_to_int(response)

	def get_value(self) -> str:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SPATh \n
		Snippet: value: str = driver.route.gprf.generator.spath.get_value() \n
		Selects the RF connection (broadcast off) or connector group (broadcast on) for the generated signal. For possible values,
		see method RsCMPX_Gprf.Catalog.Gprf.Generator.Spath.get_. \n
			:return: signal_path: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:GENerator<Instance>:SPATh?')
		return trim_str_response(response)

	def set_value(self, signal_path: str) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SPATh \n
		Snippet: driver.route.gprf.generator.spath.set_value(signal_path = 'abc') \n
		Selects the RF connection (broadcast off) or connector group (broadcast on) for the generated signal. For possible values,
		see method RsCMPX_Gprf.Catalog.Gprf.Generator.Spath.get_. \n
			:param signal_path: No help available
		"""
		param = Conversions.value_to_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:GPRF:GENerator<Instance>:SPATh {param}')

	def clone(self) -> 'SpathCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpathCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
