from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IndexCls:
	"""Index commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("index", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def set(self, row: int, signal_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:INDex \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.index.set(row = 1, signal_index = 1) \n
		No command help available \n
			:param row: No help available
			:param signal_index: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('row', row, DataType.Integer), ArgSingle('signal_index', signal_index, DataType.Integer))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:INDex {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Signal_Index: int: No parameter help available
			- Signal: str: No parameter help available
			- Path: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Signal_Index'),
			ArgStruct.scalar_str('Signal'),
			ArgStruct.scalar_str('Path')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Signal_Index: int = None
			self.Signal: str = None
			self.Path: str = None

	def get(self, row: int) -> GetStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:INDex \n
		Snippet: value: GetStruct = driver.source.gprf.generator.sequencer.listPy.signal.index.get(row = 1) \n
		No command help available \n
			:param row: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(row)
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:INDex? {param}', self.__class__.GetStruct())

	def clone(self) -> 'IndexCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IndexCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
