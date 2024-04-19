from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfPropertyCls:
	"""RfProperty commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfProperty", core, parent)

	def get_franges(self) -> List[int]:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:RFPRoperty:FRANges \n
		Snippet: value: List[int] = driver.diagnostic.gprf.generator.rfProperty.get_franges() \n
		No command help available \n
			:return: value: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('DIAGnostic:GPRF:GENerator<Instance>:RFPRoperty:FRANges?')
		return response
