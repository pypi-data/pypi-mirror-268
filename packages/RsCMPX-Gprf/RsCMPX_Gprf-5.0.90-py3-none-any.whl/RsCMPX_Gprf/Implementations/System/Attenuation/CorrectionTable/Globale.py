from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GlobaleCls:
	"""Globale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("globale", core, parent)

	def delete(self, name: str) -> None:
		"""SCPI: DELete:SYSTem:ATTenuation:CTABle:GLOBal \n
		Snippet: driver.system.attenuation.correctionTable.globale.delete(name = 'abc') \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'DELete:SYSTem:ATTenuation:CTABle:GLOBal {param}')
