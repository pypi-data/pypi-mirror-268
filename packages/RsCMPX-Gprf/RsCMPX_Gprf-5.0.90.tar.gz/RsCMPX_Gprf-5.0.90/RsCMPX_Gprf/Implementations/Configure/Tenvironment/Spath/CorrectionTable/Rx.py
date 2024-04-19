from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxCls:
	"""Rx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rx", core, parent)

	def set(self, name_signal_path: str, correction_table: List[str]) -> None:
		"""SCPI: [CONFigure]:TENVironment:SPATh:CTABle:RX \n
		Snippet: driver.configure.tenvironment.spath.correctionTable.rx.set(name_signal_path = 'abc', correction_table = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param name_signal_path: No help available
			:param correction_table: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_signal_path', name_signal_path, DataType.String), ArgSingle.as_open_list('correction_table', correction_table, DataType.StringList, None))
		self._core.io.write(f'CONFigure:TENVironment:SPATh:CTABle:RX {param}'.rstrip())

	def get(self, name_signal_path: str) -> List[str]:
		"""SCPI: [CONFigure]:TENVironment:SPATh:CTABle:RX \n
		Snippet: value: List[str] = driver.configure.tenvironment.spath.correctionTable.rx.get(name_signal_path = 'abc') \n
		No command help available \n
			:param name_signal_path: No help available
			:return: correction_table: No help available"""
		param = Conversions.value_to_quoted_str(name_signal_path)
		response = self._core.io.query_str(f'CONFigure:TENVironment:SPATh:CTABle:RX? {param}')
		return Conversions.str_to_str_list(response)
