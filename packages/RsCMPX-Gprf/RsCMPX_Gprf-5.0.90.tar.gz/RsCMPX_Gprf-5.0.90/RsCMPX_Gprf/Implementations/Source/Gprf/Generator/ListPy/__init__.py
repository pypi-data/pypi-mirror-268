from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 33 total commands, 13 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def slist(self):
		"""slist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slist'):
			from .Slist import SlistCls
			self._slist = SlistCls(self._core, self._cmd_group)
		return self._slist

	@property
	def esingle(self):
		"""esingle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_esingle'):
			from .Esingle import EsingleCls
			self._esingle = EsingleCls(self._core, self._cmd_group)
		return self._esingle

	@property
	def rlist(self):
		"""rlist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlist'):
			from .Rlist import RlistCls
			self._rlist = RlistCls(self._core, self._cmd_group)
		return self._rlist

	@property
	def fill(self):
		"""fill commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fill'):
			from .Fill import FillCls
			self._fill = FillCls(self._core, self._cmd_group)
		return self._fill

	@property
	def increment(self):
		"""increment commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_increment'):
			from .Increment import IncrementCls
			self._increment = IncrementCls(self._core, self._cmd_group)
		return self._increment

	@property
	def sstop(self):
		"""sstop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sstop'):
			from .Sstop import SstopCls
			self._sstop = SstopCls(self._core, self._cmd_group)
		return self._sstop

	@property
	def rfLevel(self):
		"""rfLevel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rfLevel'):
			from .RfLevel import RfLevelCls
			self._rfLevel = RfLevelCls(self._core, self._cmd_group)
		return self._rfLevel

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def irepetition(self):
		"""irepetition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_irepetition'):
			from .Irepetition import IrepetitionCls
			self._irepetition = IrepetitionCls(self._core, self._cmd_group)
		return self._irepetition

	@property
	def dgain(self):
		"""dgain commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dgain'):
			from .Dgain import DgainCls
			self._dgain = DgainCls(self._core, self._cmd_group)
		return self._dgain

	@property
	def dtime(self):
		"""dtime commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dtime'):
			from .Dtime import DtimeCls
			self._dtime = DtimeCls(self._core, self._cmd_group)
		return self._dtime

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def reenabling(self):
		"""reenabling commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_reenabling'):
			from .Reenabling import ReenablingCls
			self._reenabling = ReenablingCls(self._core, self._cmd_group)
		return self._reenabling

	def get_aindex(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:AINDex \n
		Snippet: value: int = driver.source.gprf.generator.listPy.get_aindex() \n
		No command help available \n
			:return: active_index: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:AINDex?')
		return Conversions.str_to_int(response)

	def get_goto(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:GOTO \n
		Snippet: value: int = driver.source.gprf.generator.listPy.get_goto() \n
		No command help available \n
			:return: goto_index: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:GOTO?')
		return Conversions.str_to_int(response)

	def set_goto(self, goto_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:GOTO \n
		Snippet: driver.source.gprf.generator.listPy.set_goto(goto_index = 1) \n
		No command help available \n
			:param goto_index: No help available
		"""
		param = Conversions.decimal_value_to_str(goto_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:GOTO {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepeatMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:REPetition \n
		Snippet: value: enums.RepeatMode = driver.source.gprf.generator.listPy.get_repetition() \n
		No command help available \n
			:return: repetition: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepeatMode)

	def set_repetition(self, repetition: enums.RepeatMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:REPetition \n
		Snippet: driver.source.gprf.generator.listPy.set_repetition(repetition = enums.RepeatMode.CONTinuous) \n
		No command help available \n
			:param repetition: No help available
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepeatMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:REPetition {param}')

	def get_start(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:STARt \n
		Snippet: value: int = driver.source.gprf.generator.listPy.get_start() \n
		No command help available \n
			:return: start_index: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:STARt \n
		Snippet: driver.source.gprf.generator.listPy.set_start(start_index = 1) \n
		No command help available \n
			:param start_index: No help available
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:STOP \n
		Snippet: value: int = driver.source.gprf.generator.listPy.get_stop() \n
		No command help available \n
			:return: stop_index: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:STOP \n
		Snippet: driver.source.gprf.generator.listPy.set_stop(stop_index = 1) \n
		No command help available \n
			:param stop_index: No help available
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:STOP {param}')

	def get_count(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:COUNt \n
		Snippet: value: int = driver.source.gprf.generator.listPy.get_count() \n
		No command help available \n
			:return: list_count: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:COUNt?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ListSubMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:MODE \n
		Snippet: value: enums.ListSubMode = driver.source.gprf.generator.listPy.get_mode() \n
		No command help available \n
			:return: list_sub_mode: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ListSubMode)

	def set_mode(self, list_sub_mode: enums.ListSubMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:MODE \n
		Snippet: driver.source.gprf.generator.listPy.set_mode(list_sub_mode = enums.ListSubMode.AUTO) \n
		No command help available \n
			:param list_sub_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(list_sub_mode, enums.ListSubMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:MODE {param}')

	def get_cindex(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:CINDex \n
		Snippet: value: int = driver.source.gprf.generator.listPy.get_cindex() \n
		No command help available \n
			:return: current_index: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:CINDex?')
		return Conversions.str_to_int(response)

	def set_cindex(self, current_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:CINDex \n
		Snippet: driver.source.gprf.generator.listPy.set_cindex(current_index = 1) \n
		No command help available \n
			:param current_index: No help available
		"""
		param = Conversions.decimal_value_to_str(current_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:CINDex {param}')

	def get_value(self) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST \n
		Snippet: value: bool = driver.source.gprf.generator.listPy.get_value() \n
		No command help available \n
			:return: enable_list_mode: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable_list_mode: bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST \n
		Snippet: driver.source.gprf.generator.listPy.set_value(enable_list_mode = False) \n
		No command help available \n
			:param enable_list_mode: No help available
		"""
		param = Conversions.bool_to_str(enable_list_mode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST {param}')

	def clone(self) -> 'ListPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
