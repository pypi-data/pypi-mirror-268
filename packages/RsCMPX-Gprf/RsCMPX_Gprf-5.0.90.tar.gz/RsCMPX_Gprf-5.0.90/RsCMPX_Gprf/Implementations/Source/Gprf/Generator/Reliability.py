from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReliabilityCls:
	"""Reliability commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reliability", core, parent)

	def get(self, details: str = None) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RELiability \n
		Snippet: value: str = driver.source.gprf.generator.reliability.get(details = 'abc') \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param details: No help available
			:return: reliability_msg: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('details', details, DataType.String, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'SOURce:GPRF:GENerator<Instance>:RELiability? {param}'.rstrip(), suppressed)
		return trim_str_response(response)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Reliability: int: Reliability indicator
			- Reliability_Msg: str: Reason for the reliability value. Empty string '' for reliability = 0.
			- Reliability_Add_Info: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Reliability_Msg'),
			ArgStruct.scalar_str('Reliability_Add_Info')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Reliability_Msg: str = None
			self.Reliability_Add_Info: str = None

	def get_all(self) -> AllStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RELiability:ALL \n
		Snippet: value: AllStruct = driver.source.gprf.generator.reliability.get_all() \n
		Reports if and why there are problems generating the configured signal. For possible values, see 'Reliability indicator'. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:RELiability:ALL?', self.__class__.AllStruct())
