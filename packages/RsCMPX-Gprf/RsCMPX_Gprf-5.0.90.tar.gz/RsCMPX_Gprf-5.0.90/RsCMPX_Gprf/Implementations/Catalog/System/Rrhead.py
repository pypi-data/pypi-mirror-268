from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrheadCls:
	"""Rrhead commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrhead", core, parent)

	def get(self, filter_criteria: enums.FilterCriteria = None) -> List[str]:
		"""SCPI: CATalog:SYSTem:RRHead \n
		Snippet: value: List[str] = driver.catalog.system.rrhead.get(filter_criteria = enums.FilterCriteria.LOSupport) \n
		No command help available \n
			:param filter_criteria: No help available
			:return: rrh_name: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_criteria', filter_criteria, DataType.Enum, enums.FilterCriteria, is_optional=True))
		response = self._core.io.query_str(f'CATalog:SYSTem:RRHead? {param}'.rstrip())
		return Conversions.str_to_str_list(response)
