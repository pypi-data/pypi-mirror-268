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
	def get_connector(self) -> enums.RfConnector:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:RFSettings:CONNector \n
		Snippet: value: enums.RfConnector = driver.route.gprf.measurement.rfSettings.get_connector() \n
		No command help available \n
			:return: rf_input_con: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:RFSettings:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.RfConnector)

	def set_connector(self, rf_input_con: enums.RfConnector) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:RFSettings:CONNector \n
		Snippet: driver.route.gprf.measurement.rfSettings.set_connector(rf_input_con = enums.RfConnector.I11I) \n
		No command help available \n
			:param rf_input_con: No help available
		"""
		param = Conversions.enum_scalar_to_str(rf_input_con, enums.RfConnector)
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:RFSettings:CONNector {param}')
