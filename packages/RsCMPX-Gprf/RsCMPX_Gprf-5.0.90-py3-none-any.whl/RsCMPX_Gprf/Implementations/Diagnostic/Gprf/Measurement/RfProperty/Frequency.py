from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, min_py: float, max_py: float, def: float) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:FREQuency \n
		Snippet: driver.diagnostic.gprf.measurement.rfProperty.frequency.set(min_py = 1.0, max_py = 1.0, def = 1.0) \n
		No command help available \n
			:param min_py: No help available
			:param max_py: No help available
			:param def: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('min_py', min_py, DataType.Float), ArgSingle('max_py', max_py, DataType.Float), ArgSingle('def', def, DataType.Float))
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:FREQuency {param}'.rstrip())

	# noinspection PyTypeChecker
	class FrequencyStruct(StructBase):
		"""Response structure. Fields: \n
			- Min_Py: float: No parameter help available
			- Max_Py: float: No parameter help available
			- Def: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Min_Py'),
			ArgStruct.scalar_float('Max_Py'),
			ArgStruct.scalar_float('Def')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Min_Py: float = None
			self.Max_Py: float = None
			self.Def: float = None

	def get(self) -> FrequencyStruct:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:FREQuency \n
		Snippet: value: FrequencyStruct = driver.diagnostic.gprf.measurement.rfProperty.frequency.get() \n
		No command help available \n
			:return: structure: for return value, see the help for FrequencyStruct structure arguments."""
		return self._core.io.query_struct(f'DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:FREQuency?', self.__class__.FrequencyStruct())
