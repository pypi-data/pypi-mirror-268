from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FillCls:
	"""Fill commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fill", core, parent)

	def get_apply(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:FILL:APPLy \n
		Snippet: value: int = driver.source.gprf.generator.listPy.fill.get_apply() \n
		No command help available \n
			:return: apply: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:FILL:APPLy?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Start_Index: float: No parameter help available
			- Range_Py: float: No parameter help available
			- Index_Repetition: int: No parameter help available
			- Start_Frequency: float: No parameter help available
			- Freq_Increment: float: No parameter help available
			- Start_Power: float: No parameter help available
			- Power_Increment: float: No parameter help available
			- Start_Dwell_Time: float: No parameter help available
			- Reenable: bool: No parameter help available
			- Modulation: bool: No parameter help available
			- Start_Gain: float: No parameter help available
			- Gain_Increment: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Start_Index'),
			ArgStruct.scalar_float('Range_Py'),
			ArgStruct.scalar_int('Index_Repetition'),
			ArgStruct.scalar_float('Start_Frequency'),
			ArgStruct.scalar_float('Freq_Increment'),
			ArgStruct.scalar_float('Start_Power'),
			ArgStruct.scalar_float('Power_Increment'),
			ArgStruct.scalar_float_optional('Start_Dwell_Time'),
			ArgStruct.scalar_bool_optional('Reenable'),
			ArgStruct.scalar_bool_optional('Modulation'),
			ArgStruct.scalar_float_optional('Start_Gain'),
			ArgStruct.scalar_float_optional('Gain_Increment')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: float = None
			self.Range_Py: float = None
			self.Index_Repetition: int = None
			self.Start_Frequency: float = None
			self.Freq_Increment: float = None
			self.Start_Power: float = None
			self.Power_Increment: float = None
			self.Start_Dwell_Time: float = None
			self.Reenable: bool = None
			self.Modulation: bool = None
			self.Start_Gain: float = None
			self.Gain_Increment: float = None

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:FILL \n
		Snippet with structure: \n
		structure = driver.source.gprf.generator.listPy.fill.ValueStruct() \n
		structure.Start_Index: float = 1.0 \n
		structure.Range_Py: float = 1.0 \n
		structure.Index_Repetition: int = 1 \n
		structure.Start_Frequency: float = 1.0 \n
		structure.Freq_Increment: float = 1.0 \n
		structure.Start_Power: float = 1.0 \n
		structure.Power_Increment: float = 1.0 \n
		structure.Start_Dwell_Time: float = 1.0 \n
		structure.Reenable: bool = False \n
		structure.Modulation: bool = False \n
		structure.Start_Gain: float = 1.0 \n
		structure.Gain_Increment: float = 1.0 \n
		driver.source.gprf.generator.listPy.fill.set_value(value = structure) \n
		No command help available \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:LIST:FILL', value)
