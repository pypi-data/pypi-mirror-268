from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AttenuationCls:
	"""Attenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def set(self, attenuation: float) -> None:
		"""SCPI: [CONFigure]:SYSTem:Z310:ATTenuation \n
		Snippet: driver.configure.system.z310.attenuation.set(attenuation = 1.0) \n
		No command help available \n
			:param attenuation: No help available
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'CONFigure:SYSTem:Z310:ATTenuation {param}')

	def get(self, connector_name: str) -> float:
		"""SCPI: [CONFigure]:SYSTem:Z310:ATTenuation \n
		Snippet: value: float = driver.configure.system.z310.attenuation.get(connector_name = 'abc') \n
		No command help available \n
			:param connector_name: No help available
			:return: attenuation: No help available"""
		param = Conversions.value_to_quoted_str(connector_name)
		response = self._core.io.query_str(f'CONFigure:SYSTem:Z310:ATTenuation? {param}')
		return Conversions.str_to_float(response)
