from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RnamesCls:
	"""Rnames commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rnames", core, parent)

	def set(self, trigger: enums.Trigger) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:RNAMes \n
		Snippet: driver.diagnostic.gprf.measurement.ploss.rnames.set(trigger = enums.Trigger.CLEarlist) \n
		No command help available \n
			:param trigger: No help available
		"""
		param = Conversions.enum_scalar_to_str(trigger, enums.Trigger)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:RNAMes {param}')

	def get(self) -> List[str]:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:RNAMes \n
		Snippet: value: List[str] = driver.diagnostic.gprf.measurement.ploss.rnames.get() \n
		No command help available \n
			:return: res_names: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:RNAMes?')
		return Conversions.str_to_str_list(response)
