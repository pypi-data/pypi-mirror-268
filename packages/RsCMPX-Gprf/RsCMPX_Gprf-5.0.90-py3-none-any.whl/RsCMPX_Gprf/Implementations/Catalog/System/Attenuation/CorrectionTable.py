from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTableCls:
	"""CorrectionTable commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correctionTable", core, parent)

	def get_tenvironment(self) -> str:
		"""SCPI: CATalog:SYSTem:ATTenuation:CTABle[:TENVironment] \n
		Snippet: value: str = driver.catalog.system.attenuation.correctionTable.get_tenvironment() \n
		No command help available \n
			:return: name: No help available
		"""
		response = self._core.io.query_str('CATalog:SYSTem:ATTenuation:CTABle:TENVironment?')
		return trim_str_response(response)

	def get_globale(self) -> str:
		"""SCPI: CATalog:SYSTem:ATTenuation:CTABle:GLOBal \n
		Snippet: value: str = driver.catalog.system.attenuation.correctionTable.get_globale() \n
		No command help available \n
			:return: name: No help available
		"""
		response = self._core.io.query_str('CATalog:SYSTem:ATTenuation:CTABle:GLOBal?')
		return trim_str_response(response)
