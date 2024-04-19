from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SallCls:
	"""Sall commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sall", core, parent)

	def get_iq_folder(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SALL:IQFolder \n
		Snippet: value: str = driver.configure.gprf.measurement.canalyzer.sall.get_iq_folder() \n
		Selects a folder for storage of all buffer contents to files (I/Q data for all segments) . The default folder is
		@USERDATA/captureanalyzer. You can only select a subfolder of this default folder. All files within the selected folder
		are deleted when the capture buffer analyzer writes the result files. \n
			:return: folder_name: Name and path of the folder.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SALL:IQFolder?')
		return trim_str_response(response)

	def set_iq_folder(self, folder_name: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SALL:IQFolder \n
		Snippet: driver.configure.gprf.measurement.canalyzer.sall.set_iq_folder(folder_name = 'abc') \n
		Selects a folder for storage of all buffer contents to files (I/Q data for all segments) . The default folder is
		@USERDATA/captureanalyzer. You can only select a subfolder of this default folder. All files within the selected folder
		are deleted when the capture buffer analyzer writes the result files. \n
			:param folder_name: Name and path of the folder.
		"""
		param = Conversions.value_to_quoted_str(folder_name)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SALL:IQFolder {param}')

	def get_wt_folder(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SALL:WTFolder \n
		Snippet: value: bool = driver.configure.gprf.measurement.canalyzer.sall.get_wt_folder() \n
		Enables or disables saving of all buffer contents to files (I/Q data for all segments) . With <WriteToFolder> = ON, the
		files are stored when the capture buffer analyzer is started. \n
			:return: write_to_folder: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SALL:WTFolder?')
		return Conversions.str_to_bool(response)

	def set_wt_folder(self, write_to_folder: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SALL:WTFolder \n
		Snippet: driver.configure.gprf.measurement.canalyzer.sall.set_wt_folder(write_to_folder = False) \n
		Enables or disables saving of all buffer contents to files (I/Q data for all segments) . With <WriteToFolder> = ON, the
		files are stored when the capture buffer analyzer is started. \n
			:param write_to_folder: No help available
		"""
		param = Conversions.bool_to_str(write_to_folder)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SALL:WTFolder {param}')
