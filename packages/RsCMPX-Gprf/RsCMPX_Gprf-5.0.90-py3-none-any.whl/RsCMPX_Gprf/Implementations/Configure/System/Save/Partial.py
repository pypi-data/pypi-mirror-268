from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PartialCls:
	"""Partial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("partial", core, parent)

	def set(self, saving_path: str, saving_module: List[str]) -> None:
		"""SCPI: [CONFigure]:SYSTem:SAVE:PARTial \n
		Snippet: driver.configure.system.save.partial.set(saving_path = 'abc', saving_module = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param saving_path: No help available
			:param saving_module: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('saving_path', saving_path, DataType.String), ArgSingle.as_open_list('saving_module', saving_module, DataType.StringList, None))
		self._core.io.write(f'CONFigure:SYSTem:SAVE:PARTial {param}'.rstrip())
