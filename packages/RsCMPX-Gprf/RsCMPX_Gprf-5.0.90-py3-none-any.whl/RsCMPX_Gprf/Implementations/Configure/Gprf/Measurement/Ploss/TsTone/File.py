from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FileCls:
	"""File commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def get_open(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:OPEN \n
		Snippet: value: str = driver.configure.gprf.measurement.ploss.tsTone.file.get_open() \n
		Selects a Touchstone file characterizing the 'open'. \n
			:return: filename: Path and filename, e.g. '@USERDATA/MyOpenFile.s1p'
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:OPEN?')
		return trim_str_response(response)

	def set_open(self, filename: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:OPEN \n
		Snippet: driver.configure.gprf.measurement.ploss.tsTone.file.set_open(filename = 'abc') \n
		Selects a Touchstone file characterizing the 'open'. \n
			:param filename: Path and filename, e.g. '@USERDATA/MyOpenFile.s1p'
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:OPEN {param}')

	def get_short(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:SHORt \n
		Snippet: value: str = driver.configure.gprf.measurement.ploss.tsTone.file.get_short() \n
		Selects a Touchstone file characterizing the 'short'. \n
			:return: filename: Path and filename, e.g. '@USERDATA/MyShortFile.s1p'
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:SHORt?')
		return trim_str_response(response)

	def set_short(self, filename: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:SHORt \n
		Snippet: driver.configure.gprf.measurement.ploss.tsTone.file.set_short(filename = 'abc') \n
		Selects a Touchstone file characterizing the 'short'. \n
			:param filename: Path and filename, e.g. '@USERDATA/MyShortFile.s1p'
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:SHORt {param}')

	def get_match(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:MATCh \n
		Snippet: value: str = driver.configure.gprf.measurement.ploss.tsTone.file.get_match() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:MATCh?')
		return trim_str_response(response)

	def set_match(self, filename: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:MATCh \n
		Snippet: driver.configure.gprf.measurement.ploss.tsTone.file.set_match(filename = 'abc') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:TSTone:FILE:MATCh {param}')
