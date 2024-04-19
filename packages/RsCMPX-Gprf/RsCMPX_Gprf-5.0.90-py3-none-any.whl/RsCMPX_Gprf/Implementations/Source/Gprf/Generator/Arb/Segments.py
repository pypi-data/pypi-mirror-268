from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SegmentsCls:
	"""Segments commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segments", core, parent)

	def get_next(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SEGMents:NEXT \n
		Snippet: value: int = driver.source.gprf.generator.arb.segments.get_next() \n
		No command help available \n
			:return: segment_number: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:SEGMents:NEXT?')
		return Conversions.str_to_int(response)

	def set_next(self, segment_number: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SEGMents:NEXT \n
		Snippet: driver.source.gprf.generator.arb.segments.set_next(segment_number = 1) \n
		No command help available \n
			:param segment_number: No help available
		"""
		param = Conversions.decimal_value_to_str(segment_number)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:SEGMents:NEXT {param}')

	# noinspection PyTypeChecker
	class CurrentStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Segment_Number: int: No parameter help available
			- Segment_Name: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Number'),
			ArgStruct.scalar_str('Segment_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Number: int = None
			self.Segment_Name: str = None

	def get_current(self) -> CurrentStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SEGMents:CURRent \n
		Snippet: value: CurrentStruct = driver.source.gprf.generator.arb.segments.get_current() \n
		No command help available \n
			:return: structure: for return value, see the help for CurrentStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:ARB:SEGMents:CURRent?', self.__class__.CurrentStruct())
