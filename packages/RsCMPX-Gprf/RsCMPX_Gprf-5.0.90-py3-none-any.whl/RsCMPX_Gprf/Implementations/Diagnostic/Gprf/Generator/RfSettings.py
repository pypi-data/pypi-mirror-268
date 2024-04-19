from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	def get_ns_margin(self) -> float:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:RFSettings:NSMargin \n
		Snippet: value: float = driver.diagnostic.gprf.generator.rfSettings.get_ns_margin() \n
		No command help available \n
			:return: net_std_margin: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:GENerator<Instance>:RFSettings:NSMargin?')
		return Conversions.str_to_float(response)

	def set_ns_margin(self, net_std_margin: float) -> None:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:RFSettings:NSMargin \n
		Snippet: driver.diagnostic.gprf.generator.rfSettings.set_ns_margin(net_std_margin = 1.0) \n
		No command help available \n
			:param net_std_margin: No help available
		"""
		param = Conversions.decimal_value_to_str(net_std_margin)
		self._core.io.write(f'DIAGnostic:GPRF:GENerator<Instance>:RFSettings:NSMargin {param}')
