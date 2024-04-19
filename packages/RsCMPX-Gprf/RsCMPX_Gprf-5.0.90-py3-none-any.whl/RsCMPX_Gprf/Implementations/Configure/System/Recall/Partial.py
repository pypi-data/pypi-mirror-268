from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PartialCls:
	"""Partial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("partial", core, parent)

	def set(self, saving_path: str, saving_module: List[str] = None) -> None:
		"""SCPI: [CONFigure]:SYSTem:RECall:PARTial \n
		Snippet: driver.configure.system.recall.partial.set(saving_path = 'abc', saving_module = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param saving_path: No help available
			:param saving_module: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('saving_path', saving_path, DataType.String), ArgSingle('saving_module', saving_module, DataType.StringList, None, True, True, 1))
		self._core.io.write(f'CONFigure:SYSTem:RECall:PARTial {param}'.rstrip())

	def get(self, saving_path: str) -> List[str]:
		"""SCPI: [CONFigure]:SYSTem:RECall:PARTial \n
		Snippet: value: List[str] = driver.configure.system.recall.partial.get(saving_path = 'abc') \n
		No command help available \n
			:param saving_path: No help available
			:return: saving_module: No help available"""
		param = Conversions.value_to_quoted_str(saving_path)
		response = self._core.io.query_str(f'CONFigure:SYSTem:RECall:PARTial? {param}')
		return Conversions.str_to_str_list(response)
