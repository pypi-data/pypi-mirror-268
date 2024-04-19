from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZeroSpanCls:
	"""ZeroSpan commands group definition. 7 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zeroSpan", core, parent)

	@property
	def rbw(self):
		"""rbw commands group. 0 Sub-classes, 3 commands."""
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

	def get_swt(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:SWT \n
		Snippet: value: float = driver.configure.gprf.measurement.spectrum.zeroSpan.get_swt() \n
		No command help available \n
			:return: sweep_time: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:SWT?')
		return Conversions.str_to_float(response)

	def set_swt(self, sweep_time: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:SWT \n
		Snippet: driver.configure.gprf.measurement.spectrum.zeroSpan.set_swt(sweep_time = 1.0) \n
		No command help available \n
			:param sweep_time: No help available
		"""
		param = Conversions.decimal_value_to_str(sweep_time)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:SWT {param}')

	# noinspection PyTypeChecker
	class DebugStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Rbw: float: No parameter help available
			- Vbw_Auto: bool: No parameter help available
			- Vbw: float: No parameter help available
			- Swt: float: No parameter help available
			- Rbw_Index: int: No parameter help available
			- Vbw_Index: int: No parameter help available
			- Vbw_Enable: bool: No parameter help available
			- Error_Reason: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Rbw'),
			ArgStruct.scalar_bool('Vbw_Auto'),
			ArgStruct.scalar_float('Vbw'),
			ArgStruct.scalar_float('Swt'),
			ArgStruct.scalar_int('Rbw_Index'),
			ArgStruct.scalar_int('Vbw_Index'),
			ArgStruct.scalar_bool('Vbw_Enable'),
			ArgStruct.scalar_int('Error_Reason')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rbw: float = None
			self.Vbw_Auto: bool = None
			self.Vbw: float = None
			self.Swt: float = None
			self.Rbw_Index: int = None
			self.Vbw_Index: int = None
			self.Vbw_Enable: bool = None
			self.Error_Reason: int = None

	def get_debug(self) -> DebugStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:DEBug \n
		Snippet: value: DebugStruct = driver.configure.gprf.measurement.spectrum.zeroSpan.get_debug() \n
		No command help available \n
			:return: structure: for return value, see the help for DebugStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:DEBug?', self.__class__.DebugStruct())

	def clone(self) -> 'ZeroSpanCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ZeroSpanCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
