from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnablingCls:
	"""Enabling commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enabling", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:INCRement:ENABling:CATalog \n
		Snippet: value: List[str] = driver.source.gprf.generator.listPy.increment.enabling.get_catalog() \n
		No command help available \n
			:return: enabling_srcs: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:INCRement:ENABling:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:INCRement:ENABling \n
		Snippet: value: str = driver.source.gprf.generator.listPy.increment.enabling.get_value() \n
		No command help available \n
			:return: enabling: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:INCRement:ENABling?')
		return trim_str_response(response)

	def set_value(self, enabling: str) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:INCRement:ENABling \n
		Snippet: driver.source.gprf.generator.listPy.increment.enabling.set_value(enabling = 'abc') \n
		No command help available \n
			:param enabling: No help available
		"""
		param = Conversions.value_to_quoted_str(enabling)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:INCRement:ENABling {param}')
