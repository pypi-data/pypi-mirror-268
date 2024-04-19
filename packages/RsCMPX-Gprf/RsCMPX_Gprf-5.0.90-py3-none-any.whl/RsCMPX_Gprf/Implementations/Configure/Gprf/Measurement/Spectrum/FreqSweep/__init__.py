from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqSweepCls:
	"""FreqSweep commands group definition. 7 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("freqSweep", core, parent)

	@property
	def rbw(self):
		"""rbw commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rbw'):
			from .Rbw import RbwCls
			self._rbw = RbwCls(self._core, self._cmd_group)
		return self._rbw

	@property
	def vbw(self):
		"""vbw commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_vbw'):
			from .Vbw import VbwCls
			self._vbw = VbwCls(self._core, self._cmd_group)
		return self._vbw

	@property
	def swt(self):
		"""swt commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_swt'):
			from .Swt import SwtCls
			self._swt = SwtCls(self._core, self._cmd_group)
		return self._swt

	# noinspection PyTypeChecker
	class DebugStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Span: float: No parameter help available
			- Rbw_Auto: bool: No parameter help available
			- Rbw: float: No parameter help available
			- Vbw_Auto: bool: No parameter help available
			- Vbw: float: No parameter help available
			- Swt_Auto: bool: No parameter help available
			- Swt: float: No parameter help available
			- Kfactor: float: No parameter help available
			- Rbw_Index: int: No parameter help available
			- Vbw_Index: int: No parameter help available
			- Vbw_Enable: bool: No parameter help available
			- Error_Reason: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Span'),
			ArgStruct.scalar_bool('Rbw_Auto'),
			ArgStruct.scalar_float('Rbw'),
			ArgStruct.scalar_bool('Vbw_Auto'),
			ArgStruct.scalar_float('Vbw'),
			ArgStruct.scalar_bool('Swt_Auto'),
			ArgStruct.scalar_float('Swt'),
			ArgStruct.scalar_float('Kfactor'),
			ArgStruct.scalar_int('Rbw_Index'),
			ArgStruct.scalar_int('Vbw_Index'),
			ArgStruct.scalar_bool('Vbw_Enable'),
			ArgStruct.scalar_int('Error_Reason')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Span: float = None
			self.Rbw_Auto: bool = None
			self.Rbw: float = None
			self.Vbw_Auto: bool = None
			self.Vbw: float = None
			self.Swt_Auto: bool = None
			self.Swt: float = None
			self.Kfactor: float = None
			self.Rbw_Index: int = None
			self.Vbw_Index: int = None
			self.Vbw_Enable: bool = None
			self.Error_Reason: int = None

	def get_debug(self) -> DebugStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:DEBug \n
		Snippet: value: DebugStruct = driver.configure.gprf.measurement.spectrum.freqSweep.get_debug() \n
		No command help available \n
			:return: structure: for return value, see the help for DebugStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:DEBug?', self.__class__.DebugStruct())

	def clone(self) -> 'FreqSweepCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FreqSweepCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
