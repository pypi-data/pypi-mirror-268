from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Stat_Count: int: No parameter help available
			- Power_Current_Rms: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Stat_Count'),
			ArgStruct('Power_Current_Rms', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Stat_Count: int = None
			self.Power_Current_Rms: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:RESults:GPRF:MEASurement<Instance>:POWer:CURRent \n
		Snippet: value: FetchStruct = driver.results.gprf.measurement.power.current.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:RESults:GPRF:MEASurement<Instance>:POWer:CURRent?', self.__class__.FetchStruct())
