from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	# noinspection PyTypeChecker
	class LongStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Signal_Type_Index: List[int]: No parameter help available
			- Signal_Type: List[str]: No parameter help available
			- Arb_File_Path: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Signal_Type_Index', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Signal_Type', DataType.StringList, None, False, True, 1),
			ArgStruct('Arb_File_Path', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Signal_Type_Index: List[int] = None
			self.Signal_Type: List[str] = None
			self.Arb_File_Path: List[str] = None

	def get_long(self) -> LongStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:CATalog:LONG \n
		Snippet: value: LongStruct = driver.source.gprf.generator.sequencer.listPy.signal.catalog.get_long() \n
		No command help available \n
			:return: structure: for return value, see the help for LongStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:CATalog:LONG?', self.__class__.LongStruct())

	def get_value(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:CATalog \n
		Snippet: value: List[str] = driver.source.gprf.generator.sequencer.listPy.signal.catalog.get_value() \n
		Queries all available signal types. The available types depend on the ARB file pool. \n
			:return: signal_types: Comma-separated list of strings, one string per supported signal type
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:CATalog?')
		return Conversions.str_to_str_list(response)
