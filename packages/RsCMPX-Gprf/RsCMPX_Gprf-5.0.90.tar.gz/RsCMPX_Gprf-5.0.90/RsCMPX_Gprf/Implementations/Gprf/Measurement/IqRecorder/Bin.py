from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BinCls:
	"""Bin commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bin", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:IQRecorder:BIN \n
		Snippet: value: List[float] = driver.gprf.measurement.iqRecorder.bin.read() \n
		Returns I/Q recorder results in binary format. For the number of values n, see method RsCMPX_Gprf.Configure.Gprf.
		Measurement.IqRecorder.Capture.set. \n
			:return: iq_samples: Binary block data. For a detailed description, see 'ASCII and binary data formats'."""
		response = self._core.io.query_bin_or_ascii_float_list(f'READ:GPRF:MEASurement<Instance>:IQRecorder:BIN?')
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:IQRecorder:BIN \n
		Snippet: value: List[float] = driver.gprf.measurement.iqRecorder.bin.fetch() \n
		Returns I/Q recorder results in binary format. For the number of values n, see method RsCMPX_Gprf.Configure.Gprf.
		Measurement.IqRecorder.Capture.set. \n
			:return: iq_samples: Binary block data. For a detailed description, see 'ASCII and binary data formats'."""
		response = self._core.io.query_bin_or_ascii_float_list(f'FETCh:GPRF:MEASurement<Instance>:IQRecorder:BIN?')
		return response
