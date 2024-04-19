from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqFileCls:
	"""IqFile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqFile", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:IQFile \n
		Snippet: driver.configure.gprf.measurement.canalyzer.iqFile.set(filename = 'abc') \n
		Saves the I/Q data for the current step to the selected file. \n
			:param filename: Name and path of the target file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:CANalyzer:IQFile {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:IQFile \n
		Snippet: value: str = driver.configure.gprf.measurement.canalyzer.iqFile.get() \n
		Saves the I/Q data for the current step to the selected file. \n
			:return: filename_return: No help available"""
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:CANalyzer:IQFile?')
		return trim_str_response(response)
