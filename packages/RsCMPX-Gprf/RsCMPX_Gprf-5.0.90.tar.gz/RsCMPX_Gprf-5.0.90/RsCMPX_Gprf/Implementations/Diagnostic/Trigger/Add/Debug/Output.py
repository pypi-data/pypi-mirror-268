from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OutputCls:
	"""Output commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	def set(self, show_trigger_debug_output: bool, show_trigger_debug_scpi_output: bool) -> None:
		"""SCPI: DIAGnostic:TRIGger:ADD:DEBug:OUTPut \n
		Snippet: driver.diagnostic.trigger.add.debug.output.set(show_trigger_debug_output = False, show_trigger_debug_scpi_output = False) \n
		No command help available \n
			:param show_trigger_debug_output: No help available
			:param show_trigger_debug_scpi_output: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('show_trigger_debug_output', show_trigger_debug_output, DataType.Boolean), ArgSingle('show_trigger_debug_scpi_output', show_trigger_debug_scpi_output, DataType.Boolean))
		self._core.io.write(f'DIAGnostic:TRIGger:ADD:DEBug:OUTPut {param}'.rstrip())

	# noinspection PyTypeChecker
	class OutputStruct(StructBase):
		"""Response structure. Fields: \n
			- Show_Trigger_Debug_Output: bool: No parameter help available
			- Show_Trigger_Debug_Scpi_Output: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Show_Trigger_Debug_Output'),
			ArgStruct.scalar_bool('Show_Trigger_Debug_Scpi_Output')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Show_Trigger_Debug_Output: bool = None
			self.Show_Trigger_Debug_Scpi_Output: bool = None

	def get(self) -> OutputStruct:
		"""SCPI: DIAGnostic:TRIGger:ADD:DEBug:OUTPut \n
		Snippet: value: OutputStruct = driver.diagnostic.trigger.add.debug.output.get() \n
		No command help available \n
			:return: structure: for return value, see the help for OutputStruct structure arguments."""
		return self._core.io.query_struct(f'DIAGnostic:TRIGger:ADD:DEBug:OUTPut?', self.__class__.OutputStruct())
