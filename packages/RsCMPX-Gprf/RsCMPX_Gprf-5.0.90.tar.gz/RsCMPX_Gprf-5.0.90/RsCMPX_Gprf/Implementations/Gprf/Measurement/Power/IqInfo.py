from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqInfoCls:
	"""IqInfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqInfo", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Number_Of_Samples: float: No parameter help available
			- Sample_Rate: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Number_Of_Samples'),
			ArgStruct.scalar_float('Sample_Rate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Number_Of_Samples: float = None
			self.Sample_Rate: float = None

	def fetch(self, list_index: int, result_index: int = None) -> FetchStruct:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:IQINfo \n
		Snippet: value: FetchStruct = driver.gprf.measurement.power.iqInfo.fetch(list_index = 1, result_index = 1) \n
		No command help available \n
			:param list_index: No help available
			:param result_index: No help available
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('list_index', list_index, DataType.Integer), ArgSingle('result_index', result_index, DataType.Integer, None, is_optional=True))
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:POWer:IQINfo? {param}'.rstrip(), self.__class__.FetchStruct())
