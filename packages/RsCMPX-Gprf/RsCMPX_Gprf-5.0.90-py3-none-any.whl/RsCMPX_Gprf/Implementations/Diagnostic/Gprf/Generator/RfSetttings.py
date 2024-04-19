from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSetttingsCls:
	"""RfSetttings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSetttings", core, parent)

	def get_paratio(self) -> float:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:RFSetttings:PARatio \n
		Snippet: value: float = driver.diagnostic.gprf.generator.rfSetttings.get_paratio() \n
		No command help available \n
			:return: peak_avg_ratio: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:GENerator<Instance>:RFSetttings:PARatio?')
		return Conversions.str_to_float(response)

	def set_paratio(self, peak_avg_ratio: float) -> None:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:RFSetttings:PARatio \n
		Snippet: driver.diagnostic.gprf.generator.rfSetttings.set_paratio(peak_avg_ratio = 1.0) \n
		No command help available \n
			:param peak_avg_ratio: No help available
		"""
		param = Conversions.decimal_value_to_str(peak_avg_ratio)
		self._core.io.write(f'DIAGnostic:GPRF:GENerator<Instance>:RFSetttings:PARatio {param}')
