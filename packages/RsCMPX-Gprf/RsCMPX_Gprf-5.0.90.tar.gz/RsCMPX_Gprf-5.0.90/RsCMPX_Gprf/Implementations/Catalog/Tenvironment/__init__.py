from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TenvironmentCls:
	"""Tenvironment commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tenvironment", core, parent)

	@property
	def connectors(self):
		"""connectors commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_connectors'):
			from .Connectors import ConnectorsCls
			self._connectors = ConnectorsCls(self._core, self._cmd_group)
		return self._connectors

	def get_spath(self) -> List[str]:
		"""SCPI: CATalog:TENVironment:SPATh \n
		Snippet: value: List[str] = driver.catalog.tenvironment.get_spath() \n
		No command help available \n
			:return: name_signal_path: No help available
		"""
		response = self._core.io.query_str('CATalog:TENVironment:SPATh?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'TenvironmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TenvironmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
