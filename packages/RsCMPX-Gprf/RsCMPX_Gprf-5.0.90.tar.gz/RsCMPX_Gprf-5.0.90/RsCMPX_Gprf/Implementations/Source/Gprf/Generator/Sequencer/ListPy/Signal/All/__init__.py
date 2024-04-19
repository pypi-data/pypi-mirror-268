from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 7 total commands, 3 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	@property
	def cw(self):
		"""cw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cw'):
			from .Cw import CwCls
			self._cw = CwCls(self._core, self._cmd_group)
		return self._cw

	@property
	def off(self):
		"""off commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_off'):
			from .Off import OffCls
			self._off = OffCls(self._core, self._cmd_group)
		return self._off

	@property
	def dtone(self):
		"""dtone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtone'):
			from .Dtone import DtoneCls
			self._dtone = DtoneCls(self._core, self._cmd_group)
		return self._dtone

	def get_old(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:OLD \n
		Snippet: value: List[str] = driver.source.gprf.generator.sequencer.listPy.signal.all.get_old() \n
		No command help available \n
			:return: signal: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:OLD?')
		return Conversions.str_to_str_list(response)

	def set_old(self, signal: List[str]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:OLD \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.all.set_old(signal = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param signal: No help available
		"""
		param = Conversions.list_to_csv_quoted_str(signal)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:OLD {param}')

	def continue_py(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:CONTinue \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.all.continue_py() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:CONTinue')

	def continue_py_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:CONTinue \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.all.continue_py_with_opc() \n
		No command help available \n
		Same as continue_py, but waits for the operation to complete before continuing further. Use the RsCMPX_Gprf.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:CONTinue', opc_timeout_ms)

	def set_waveform(self, waveform: str) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:WAVeform \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.all.set_waveform(waveform = 'abc') \n
		No command help available \n
			:param waveform: No help available
		"""
		param = Conversions.value_to_quoted_str(waveform)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL:WAVeform {param}')

	def get_value(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL \n
		Snippet: value: List[str] = driver.source.gprf.generator.sequencer.listPy.signal.all.get_value() \n
		Defines the signal types for all sequencer list entries. A complete list of all supported strings can be queried using
		method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.Signal.Catalog.value. \n
			:return: signal: Comma-separated list of strings, one string per list entry
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL?')
		return Conversions.str_to_str_list(response)

	def set_value(self, signal: List[str]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.all.set_value(signal = ['abc1', 'abc2', 'abc3']) \n
		Defines the signal types for all sequencer list entries. A complete list of all supported strings can be queried using
		method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.Signal.Catalog.value. \n
			:param signal: Comma-separated list of strings, one string per list entry
		"""
		param = Conversions.list_to_csv_quoted_str(signal)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL {param}')

	def clone(self) -> 'AllCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AllCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
