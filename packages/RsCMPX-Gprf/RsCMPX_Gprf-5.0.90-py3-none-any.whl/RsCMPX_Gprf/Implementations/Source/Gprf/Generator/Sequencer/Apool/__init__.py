from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApoolCls:
	"""Apool commands group definition. 32 total commands, 13 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apool", core, parent)

	@property
	def download(self):
		"""download commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_download'):
			from .Download import DownloadCls
			self._download = DownloadCls(self._core, self._cmd_group)
		return self._download

	@property
	def check(self):
		"""check commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_check'):
			from .Check import CheckCls
			self._check = CheckCls(self._core, self._cmd_group)
		return self._check

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_path'):
			from .Path import PathCls
			self._path = PathCls(self._core, self._cmd_group)
		return self._path

	@property
	def crcProtect(self):
		"""crcProtect commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_crcProtect'):
			from .CrcProtect import CrcProtectCls
			self._crcProtect = CrcProtectCls(self._core, self._cmd_group)
		return self._crcProtect

	@property
	def paratio(self):
		"""paratio commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_paratio'):
			from .Paratio import ParatioCls
			self._paratio = ParatioCls(self._core, self._cmd_group)
		return self._paratio

	@property
	def poffset(self):
		"""poffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import PoffsetCls
			self._poffset = PoffsetCls(self._core, self._cmd_group)
		return self._poffset

	@property
	def roption(self):
		"""roption commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_roption'):
			from .Roption import RoptionCls
			self._roption = RoptionCls(self._core, self._cmd_group)
		return self._roption

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import DurationCls
			self._duration = DurationCls(self._core, self._cmd_group)
		return self._duration

	@property
	def samples(self):
		"""samples commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_samples'):
			from .Samples import SamplesCls
			self._samples = SamplesCls(self._core, self._cmd_group)
		return self._samples

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import WaveformCls
			self._waveform = WaveformCls(self._core, self._cmd_group)
		return self._waveform

	@property
	def reliability(self):
		"""reliability commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_reliability'):
			from .Reliability import ReliabilityCls
			self._reliability = ReliabilityCls(self._core, self._cmd_group)
		return self._reliability

	@property
	def rmessage(self):
		"""rmessage commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rmessage'):
			from .Rmessage import RmessageCls
			self._rmessage = RmessageCls(self._core, self._cmd_group)
		return self._rmessage

	# noinspection PyTypeChecker
	def get_valid(self) -> enums.YesNoStatus:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:VALid \n
		Snippet: value: enums.YesNoStatus = driver.source.gprf.generator.sequencer.apool.get_valid() \n
		Queries whether the ARB file pool is valid. \n
			:return: valid: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:VALid?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	# noinspection PyTypeChecker
	def get_loaded(self) -> enums.YesNoStatus:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:LOADed \n
		Snippet: value: enums.YesNoStatus = driver.source.gprf.generator.sequencer.apool.get_loaded() \n
		Queries whether the ARB file pool is downloaded to the ARB RAM. \n
			:return: loaded: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:LOADed?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	def get_rrequired(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RREQuired \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.apool.get_rrequired() \n
		Queries the amount of RAM required by the ARB files in the pool. \n
			:return: ram_required: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RREQuired?')
		return Conversions.str_to_float(response)

	def get_rtotal(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RTOTal \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.apool.get_rtotal() \n
		Queries the amount of RAM available for ARB files. \n
			:return: ram_total: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RTOTal?')
		return Conversions.str_to_float(response)

	def set_file(self, arb_file: str) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:FILE \n
		Snippet: driver.source.gprf.generator.sequencer.apool.set_file(arb_file = 'abc') \n
		Adds an ARB file to the ARB file pool. \n
			:param arb_file: Path and filename Example: '@WAVEFORM/myARBfile.wv'
		"""
		param = Conversions.value_to_quoted_str(arb_file)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:FILE {param}')

	def set_remove(self, indices: List[int]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:REMove \n
		Snippet: driver.source.gprf.generator.sequencer.apool.set_remove(indices = [1, 2, 3]) \n
		Removes selected files from the ARB file pool. \n
			:param indices: Indices of the files to be removed. You can specify a single index or a comma-separated list of indices.
		"""
		param = Conversions.list_to_csv_str(indices)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:REMove {param}')

	def clear(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CLEar \n
		Snippet: driver.source.gprf.generator.sequencer.apool.clear() \n
		Removes all files from the ARB file pool. \n
		"""
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CLEar \n
		Snippet: driver.source.gprf.generator.sequencer.apool.clear_with_opc() \n
		Removes all files from the ARB file pool. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsCMPX_Gprf.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CLEar', opc_timeout_ms)

	def get_mindex(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:MINDex \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.apool.get_mindex() \n
		Queries the highest index of the ARB file pool. The pool contains files with the indices 0 to <MaximumIndex>. \n
			:return: maximum_index: Highest index. If the file pool is empty, NAV is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:MINDex?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'ApoolCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApoolCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
