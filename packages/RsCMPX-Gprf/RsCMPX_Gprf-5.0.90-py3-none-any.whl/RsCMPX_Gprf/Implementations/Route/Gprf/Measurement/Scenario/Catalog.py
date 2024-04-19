from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_cspath(self) -> List[str]:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:CATalog:CSPath \n
		Snippet: value: List[str] = driver.route.gprf.measurement.scenario.catalog.get_cspath() \n
		No command help available \n
			:return: csp_masters: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SCENario:CATalog:CSPath?')
		return Conversions.str_to_str_list(response)
