from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdMarkerCls:
	"""UdMarker commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("udMarker", core, parent)

	@property
	def clist(self):
		"""clist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clist'):
			from .Clist import ClistCls
			self._clist = ClistCls(self._core, self._cmd_group)
		return self._clist

	def set(self, period: int, start_state: enums.SignalSlope, positions: List[int or bool]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:UDMarker \n
		Snippet: driver.source.gprf.generator.arb.udMarker.set(period = 1, start_state = enums.SignalSlope.FEDGe, positions = [1, True, 2, False, 3]) \n
		No command help available \n
			:param period: No help available
			:param start_state: No help available
			:param positions: (integer or boolean items) No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('period', period, DataType.Integer), ArgSingle('start_state', start_state, DataType.Enum, enums.SignalSlope), ArgSingle('positions', positions, DataType.IntegerExtList, None, False, False, 8))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:UDMarker {param}'.rstrip())

	# noinspection PyTypeChecker
	class UdMarkerStruct(StructBase):
		"""Response structure. Fields: \n
			- Period: int: No parameter help available
			- Start_State: enums.SignalSlope: No parameter help available
			- Positions: List[int or bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Period'),
			ArgStruct.scalar_enum('Start_State', enums.SignalSlope),
			ArgStruct('Positions', DataType.IntegerExtList, None, False, False, 8)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Period: int = None
			self.Start_State: enums.SignalSlope = None
			self.Positions: List[int or bool] = None

	def get(self) -> UdMarkerStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:UDMarker \n
		Snippet: value: UdMarkerStruct = driver.source.gprf.generator.arb.udMarker.get() \n
		No command help available \n
			:return: structure: for return value, see the help for UdMarkerStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:ARB:UDMarker?', self.__class__.UdMarkerStruct())

	def clone(self) -> 'UdMarkerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UdMarkerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
