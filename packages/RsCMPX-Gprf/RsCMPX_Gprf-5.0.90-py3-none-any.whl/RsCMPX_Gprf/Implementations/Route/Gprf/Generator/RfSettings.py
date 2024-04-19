from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.TxConnector:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:RFSettings:CONNector \n
		Snippet: value: enums.TxConnector = driver.route.gprf.generator.rfSettings.get_connector() \n
		No command help available \n
			:return: output_connector: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:GENerator<Instance>:RFSettings:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.TxConnector)

	def set_connector(self, output_connector: enums.TxConnector) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:RFSettings:CONNector \n
		Snippet: driver.route.gprf.generator.rfSettings.set_connector(output_connector = enums.TxConnector.I12O) \n
		No command help available \n
			:param output_connector: No help available
		"""
		param = Conversions.enum_scalar_to_str(output_connector, enums.TxConnector)
		self._core.io.write(f'ROUTe:GPRF:GENerator<Instance>:RFSettings:CONNector {param}')
