from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxCls:
	"""Tx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

	def set(self, name_signal_path: str, correction_table: List[str]) -> None:
		"""SCPI: ADD:TENVironment:SPATh:CTABle:TX \n
		Snippet: driver.add.tenvironment.spath.correctionTable.tx.set(name_signal_path = 'abc', correction_table = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param name_signal_path: No help available
			:param correction_table: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_signal_path', name_signal_path, DataType.String), ArgSingle.as_open_list('correction_table', correction_table, DataType.StringList, None))
		self._core.io.write(f'ADD:TENVironment:SPATh:CTABle:TX {param}'.rstrip())
