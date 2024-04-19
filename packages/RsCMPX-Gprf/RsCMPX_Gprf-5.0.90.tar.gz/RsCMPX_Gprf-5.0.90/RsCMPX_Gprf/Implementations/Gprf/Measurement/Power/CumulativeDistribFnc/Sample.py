from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SampleCls:
	"""Sample commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sample", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Count: int: Total sample count
			- Time: float: Total sample time"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Count'),
			ArgStruct.scalar_float('Time')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Count: int = None
			self.Time: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:SAMPle \n
		Snippet: value: FetchStruct = driver.gprf.measurement.power.cumulativeDistribFnc.sample.fetch() \n
		Returns the sample counters for the APD and CCDF results. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:SAMPle?', self.__class__.FetchStruct())
