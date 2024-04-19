from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpathCls:
	"""Spath commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	def get_count(self) -> int:
		"""SCPI: ROUTe:NRDL:MEASurement<Instance>:SPATh:COUNt \n
		Snippet: value: int = driver.route.nrDl.measurement.spath.get_count() \n
		No command help available \n
			:return: signal_path_count: No help available
		"""
		response = self._core.io.query_str('ROUTe:NRDL:MEASurement<Instance>:SPATh:COUNt?')
		return Conversions.str_to_int(response)

	def get_value(self) -> List[str]:
		"""SCPI: ROUTe:NRDL:MEASurement<Instance>:SPATh \n
		Snippet: value: List[str] = driver.route.nrDl.measurement.spath.get_value() \n
		No command help available \n
			:return: signal_path: No help available
		"""
		response = self._core.io.query_str('ROUTe:NRDL:MEASurement<Instance>:SPATh?')
		return Conversions.str_to_str_list(response)

	def set_value(self, signal_path: List[str]) -> None:
		"""SCPI: ROUTe:NRDL:MEASurement<Instance>:SPATh \n
		Snippet: driver.route.nrDl.measurement.spath.set_value(signal_path = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param signal_path: No help available
		"""
		param = Conversions.list_to_csv_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:NRDL:MEASurement<Instance>:SPATh {param}')
