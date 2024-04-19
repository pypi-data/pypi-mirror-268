from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoFrequencyCls:
	"""LoFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loFrequency", core, parent)

	def get_available(self) -> bool:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:LOFRequency:AVAilable \n
		Snippet: value: bool = driver.diagnostic.gprf.measurement.rfProperty.loFrequency.get_available() \n
		No command help available \n
			:return: def: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:LOFRequency:AVAilable?')
		return Conversions.str_to_bool(response)

	def set_available(self, def: bool) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:LOFRequency:AVAilable \n
		Snippet: driver.diagnostic.gprf.measurement.rfProperty.loFrequency.set_available(def = False) \n
		No command help available \n
			:param def: No help available
		"""
		param = Conversions.bool_to_str(def)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:LOFRequency:AVAilable {param}')
