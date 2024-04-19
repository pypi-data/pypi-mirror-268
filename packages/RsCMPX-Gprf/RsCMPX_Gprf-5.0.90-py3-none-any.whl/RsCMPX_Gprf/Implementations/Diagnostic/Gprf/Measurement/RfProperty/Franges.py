from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrangesCls:
	"""Franges commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("franges", core, parent)

	def get_mindex(self) -> int:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:FRANges:MINDex \n
		Snippet: value: int = driver.diagnostic.gprf.measurement.rfProperty.franges.get_mindex() \n
		No command help available \n
			:return: max_index: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:FRANges:MINDex?')
		return Conversions.str_to_int(response)
